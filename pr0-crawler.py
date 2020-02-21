# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:29:43 2020

@author: Niklas
"""

import requests
import base64
from PIL import Image
from io import BytesIO
import pickle
import os

cookies = None

def main():
    cookies = login()
    
    

def getPost(postID):
    return

def login():
    
    if os.path.isfile("cookie.obj"):
        cookies = pickle.load(open("cookie.obj","rb"))
        return cookies
    else:
        req = requests.get("https://pr0gramm.com/api/user/captcha")
        if req.status_code == 200:
            token = req.json().get("token")
            captcha = req.json().get("captcha")
            png_captcha = Image.open(BytesIO(base64.b64decode(captcha.split(",")[1])))
            png_captcha.show()
            captcha_input = input("Captcha eingeben:\n")
            login_data = {'name' : "TEST_USERNAMe", 'password':"TEST_PASSWORD", 'captcha':captcha_input, 'token':token}
            login_req = requests.post("https://pr0gramm.com/api/user/login",data=login_data)  
            pickle.dump(login_req.cookies, open("cookie.obj","wb"))
            return login_req.cookies
        else:
            raise
            

if __name__ == "__main__":
    main()