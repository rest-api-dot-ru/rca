# coding: utf-8

import requests
from lxml import html
import validators
from flask import Flask
from flask import request
from flask import jsonify
from rca import errors

__author__ = 'vanzhiganov'


rca = Flask(__name__)
rca.config.from_object('config')


@rca.route('/')
def index():
    # check mandatory args
    if 'url' not in request.args:
        return jsonify(errors.MISSING_PARAMETER_URL)

    if not validators.url(request.args['url']):
        return jsonify(errors.INVALID_PARAMETER_URL)

    url = request.args['url']
    response = requests.get(url)
    parsed_body = html.fromstring(response.text)

    data = dict()
    # mandatory: url
    data['url'] = url
    # mandatory: finalurl
    # optional: title
    data['title'] = (parsed_body.xpath('//title/text()')[0])
    # optional: content
    data['content'] = dict()
    for df in parsed_body.xpath('//h1/text()'):
        data['content']['h1'] = df.strip()
    for df in parsed_body.xpath('//h2/text()'):
        data['content']['h2'] = df.strip()
    for df in parsed_body.xpath('//h3/text()'):
        data['content']['h3'] = df.strip()

    data['content']['content'] = ''
    for df in parsed_body.xpath('//div/text()'):
        if df.strip() != "":
            data['content']['content'] = data['content']['content'] + " " + df.strip()

    for df in parsed_body.xpath('//p/text()'):
        if df.strip() != "":
            data['content']['content'] = data['content']['content'] + " " + df.strip()
    # optional: img
    # Парсим ссылки с картинками
    images = parsed_body.xpath('//img/@src')
    if len(images) > 0:
        data['img'] = []
        for img in images:
            data['img'].append(img)

    # optional: video
    # TODO: video
    # optional: mime
    data['mime'] = response.headers['Content-Type'].split(';')[0]
    # optional: confidence

    data['links'] = []
    for df in parsed_body.xpath('//a/@href'):
        if df:
            data['links'].append(df)

    return jsonify(data)
