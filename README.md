# Portfolio website 👨‍💻

---
## What's inside 🔍
1. Integration of VK API ([local docs](/vk_friends), [official docs](https://vk.com/dev/docs)) 
2. Weather web app ([local docs](/weather), [official docs](https://www.weatherapi.com/docs/))

## Stack 📚
`Django` `Bulma` \
`VK API` `WeatherAPI`

## To run it locally 🏃‍♂️
1. Get API keys 
- [WeatherAPI](https://www.weatherapi.com/) ⛅
- [VK API](https://vkhost.github.io/) 🌐

2. Set environment variables
```bash
~$ export VK_TOKEN='secret_vk_token_123'
~$ export WEATHER_KEY='secret_weather_api_key'
```

3. Create virtual environment, install dependencies and RUN!
```bash
~$ cd SupremeWebsite
~$ python3 -m venv env
~$ . env/bin/activate
(env) ~$ pip install -r requirements.txt
(env) ~$ ./manage.py runserver
```

## Plans 📝
1. Finish [weather app](/weather) (backgrounds videos depending on weather condition)
2. Create local docs for apps
3. Host on Heroku + set custom domain
4. Switch to PostgreSQL