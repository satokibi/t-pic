# -*- coding: utf-8 -*-

import config
from lib import *
import json


def search_user( screen_name, key_dict ):
    url = "https://api.twitter.com/1.1/users/show.json"
    params = {
            "screen_name" : screen_name,
            "include_entities" : False,
            }

    twitter = create_oauth_session( key_dict )
    response = twitter.get( url, params = params )
    return response


if __name__ == "__main__":
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    oauth_key_dict = {
            "consumer_key": CK,
            "consumer_secret": CS,
            "access_token": AT,
            "access_token_secret": ATS,
            }


    print("検索したいid を入力してください")
    print(">> ", end="")
    input_str = input()

    response = search_user( input_str, oauth_key_dict ) 

    if response.status_code == 200:
        user = json.loads( response.text )
        # print( user )
        print( "     id: {}".format( user["screen_name"] ) )
        print( "   name: {}".format( user["name"] ) )
        print( "img_url: {}".format( user["profile_image_url"] ) )
    else:
        print("##ERROR## status_code: {}".format( response.status_code ) )

