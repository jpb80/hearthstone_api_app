#!/usr/bin/env python
# coding=utf-8

import logging as log
import os
import sys

import requests

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
token_url = 'https://us.battle.net/oauth/token'
data = {'grant_type': 'client_credentials'}


def get_access_token():
    """
     Retrieves access token from hearthstone api using clientId and
     clientSecret.
    """
    log.info("Retrieve access token from api")
    try:
        access_token_response = requests.post(token_url, 
                                              data=data, 
                                              verify=False, 
                                              allow_redirects=False, 
                                              auth=(client_id, client_secret))
        access_token_response.raise_for_status()
    except requests.RequestException as re:
        log.exception("Error occurred getting access token: %s", re)
    log.info("Succesfully retireved access token")
    return access_token_response.json()['access_token']


def main():
    access_token = get_access_token()
    log.debug("access_token: %s", access_token)


if __name__ == '__main__':
    main()
