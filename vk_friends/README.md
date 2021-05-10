# Portfolio website. VK API 🌐

## What's that and why it's existing 🤔

<details>
    <summary>What is VK</summary>
    VK - is a Russian social network, something like Facebook.
</details>

#### Why?
Sometimes you go to some **X**'s page to check someone's profile. \
Some **X** don't specify their current cities (where they live ATM) and home cities (where they were born). \
And that drove me mad.

#### Solution 💡
Most of the time, **X** will have an open friends list, \
and his friends can indeed specify their current/home cities. \
You can collect **X**'s friends data and, with a certain degree of probability, \
you can draw a conclusion: because **X** will have more friends from his home/current city.

## How to use 📄
`vk/` - base endpoint \
`vk/cities/` - vk api endpoint

| Parameters           | Description             |
|-------------------   |-------------------------|
|`user`  (arbitrary)   | id (`int`) or screen_name (`str`) of VK user |
|`lang`  (optional)    | response language from VK server (e.g. 'ru', 'en'), default = 'ru'|
|`forced`(arbitrary)   | force translation to `lang` value (using Google Translate library)|


```bash
~$ curl vk/cities/
{
  "message": "Welcome to VK Friends API",
  "available requests": {...}
}

# Pavel Durov
~$ curl vk/cities?user=1
{
  "code": 204,
  "content": [
    {
      "message": "User https://vk.com/id1 has no friends."
    }
  ]
}

# Me
~$ curl vk/cities?user=wannfight
{
  "code": 200,
  "content": [
    {
      "user": "https://vk.com/****",
      "current_city": "Санкт-Петербург",
      "home_city": "Ленинград"
    },
    {
      "user": "https://vk.com/****",
      "current_city": "Тихвин",
      "home_city": "Тихвин"
    },
    ...
  ]
} 
```

## Plans 📝
1. Make frontend part of this api
2. Optimization of time (when `forced` is passed can take aa lot of time)
