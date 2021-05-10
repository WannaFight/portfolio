import os

from googletrans import Translator
import vk
import vk.exceptions

VK_TOK = os.getenv('VK_TOKEN', '')
API_V = 5.122


def get_response(target_id: str, lang: str, forced: bool):
    """
    :param target_id: vk id of target https://vk.com/ID
    :param lang: language to translate to
    :param forced: forced translation to :param lang:

    :returns: JSON with results {'code': code, 'content': [...]}
    """
    session = vk.Session(access_token=VK_TOK)
    api = vk.API(session, lang=lang, v=API_V)
    tr = Translator()
    resp_json = {'code': 200, 'content': []}

    # Catching VK API exceptions,
    try:
        target_id = api.users.get(user_ids=target_id)[0]['id']
        friends_data = api.friends.get(user_id=target_id,
                                       fields=['city', 'home_town'])['items']
    except vk.exceptions.VkAPIError as e:
        resp_json['code'] = e.code
        resp_json['content'].append({'message': e.message})

        return resp_json

    # User with no friends
    if not friends_data:
        text = f"User https://vk.com/id{target_id} has no friends."
        resp_json['code'] = 204
        resp_json['content'].append({'message': text})

        return resp_json

    # If forced translation is True
    # creating an array of translated city names to destination language
    # cities and home towns from friends_data
    if forced:
        # to save time of translations we do:
        # 1. create a list of names
        # 2. convert it to str with '; ' as separator and translate
        # 3. split by '; '
        final_cities = tr.translate('; '.join(
            [user.get('city', {}).get('title', 'Not specified') for user in
             friends_data]), dest=lang).text.split('; ')

        final_homes = tr.translate('; '.join(
            [home if (home := user.get('home_town', '')) else 'Not specified'
             for user in friends_data]), dest=lang).text.split('; ')

        resp_json['content'] = [{"user": f"https://vk.com/id{user.get('id')}",
                                 'current_city': final_cities[i],
                                 'home_city': final_homes[i]} for i, user in
                                enumerate(friends_data)]

        return resp_json

    # if no need to force translate to dest language
    else:
        resp_json['content'] = [{'user': f"https://vk.com/id{user['id']}",
                                 'current_city': user.get("city", {}).get(
                                     "title", "Not specified"),
                                 'home_city': home if (
                                     home := user.get("home_town", ""))
                                 else "Not specified"}
                                for user in friends_data]

        return resp_json
