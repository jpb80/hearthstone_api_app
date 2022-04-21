#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import render_template


import logging
import json
import os
from operator import itemgetter
import sys

import requests

import auth

access_token = ""
blizzard_api_base = "https://us.api.blizzard.com"
app = Flask(__name__)
log = logging.getLogger(__name__)
#LOGLEVEL = os.environ['LOGLEVEL']
LOGLEVEL = 20


def setup_logging():
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=LOGLEVEL, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def get_auth_headers():
    return {'Authorization': 'Bearer ' + access_token}


@app.before_first_request
def before_first_request_func():
    global access_token
    access_token = auth.get_access_token()


@app.route('/get_mage_cards')
def get_mage_cards():
    params = {
                "locale":"en_US",
                "class":"mage",
                "manaCost":"7",
                "rarity":"legendary",
                "page":"1",
                "pageSize":"10",
                "sort":"id%3Aasc"
             }              
    return render_template('cards.html.j2', 
                           items=get_cards(params=params))


@app.route('/healthz')
def healthcheck():
    return {'status': 'success'}


def send_request(url, params=None):
    """
    Use the requests library to call the hearthstone public api.
    """
    try:
        log.info("Sending request to endpoint: %s.", url)
        log.debug("Url parameters: %s", params)
        response = requests.get(url, params=params, headers=get_auth_headers())
        response.raise_for_status()
    except requests.exceptions.RequestException as request_exception:
        log.exception("Requests exception: %s", request_exception)
    log.debug("Response from api: %s", response)
    return response


def get_cards(params):
    log.info("Making request to hearthstone api")
    response = send_request(url=f'{blizzard_api_base}/hearthstone/cards',
                            params=params)
    log.debug("get_cards response: %s", response)
    response_json = response.json()
    cards_list = response_json['cards']
    sorted_cards = sorted(cards_list, key=itemgetter('id'))
    return sorted_cards


if __name__ == '__main__':
    setup_logging()
    log.info("Hearthstone app! :)")
    app.run(host='0.0.0.0', port='8080', debug=False)
