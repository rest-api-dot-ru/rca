# Overview of the API

In this section

- Request format
- Response format
- Error codes

## Request format

To get data about a web page, send an HTTP GET request of the following type:

`GET http://rca.rest-api.ru/?key=yourKEY&url=targetURL[&callback=yourFUNCTION][&full=1]`

Input data:

*Mabdatory*

- `key` - Unique API key. To get your free API key, please fill out a simple form.
- `url` - The URL that data is being requested for. The URL can be passed in any format (as a shortened link, as a URL
 with parameters, or others). The service will automatically expand it and canonize it, if necessary.

*Optional*

- `callback` - The name of your callback function.
- `img` - The mode for detecting images on the page:
    - best (default) — Detects one or several of the main images on the page (no more than four images).
    - no — Images will not be detected on the page.
- `content` - The mode for detecting the page's text description:
    - short (default) — Detects a short page summary (snippet).
    - full — Detects the full page text.
    - no — Page content is not detected.
- `full` - Add `full=1` if you want to get the full text of the page with links to images.



# Установка
## Установка LXML

Довольно часто возникают проблемы при установке Ixml, особенно в линуксе. Просто вначале надо установить зависимости:

```
apt-get install libxml2-dev libxslt-dev python-dev lib32z1-dev
```

а уже после можно выполнять команду `pip install lxml` в обычном режиме.

# Использование

