#!/usr/bin/env python3
'''
    api_test.py
    Grant Lee & Richard Yoon, 11/19/18

    Testing Spotify API and integrating authorization 
    code grant authentication system
'''

import subprocess
import sys
import argparse
import json
import urllib.request
import urllib.parse
import base64
import codecs
import webbrowser



def getToken():

    # Code for creating a base64 encoded
    base_url = 'https://accounts.spotify.com/authorize?client_id={0}&response_type={1}&redirect_uri={2}'
    client_id = 'a9c19b55cef14742aba314f3d27ae7d5'
    response_type = 'code' 
    redirect_uri = 'www.facebook.com'

    final_url = base_url.format(client_id, response_type, redirect_uri)

    request = urllib.request.Request(final_url)

    data_from_server = urllib.request.urlopen(request).read()
    decoded = data_from_server.decode("utf8")

    login_page  = open('login_page.html', 'w')
    login_page.write(decoded)
    login_page.close()

    webbrowser.open_new_tab('login_page.html')
    



    return decoded



def main(args):

    if args.request == 'id':
        print(getToken())


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Get information about a particular user!')

    request = parser.add_argument('request',
            help = 'test the api',
            choices = ['id']) 
    
    args = parser.parse_args()

    main(args)




    

