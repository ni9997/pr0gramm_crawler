# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:29:43 2020

@author: Niklas
"""

import requests
import base64
from PIL import Image
from io import BytesIO


def main():
    getCaptcha()
def connect():
    return

def getPost(postID):
    return

def getCaptcha():
    req = requests.get("https://pr0gramm.com/api/user/captcha")
    if req.status_code == 200:
        token = req.json()
        captcha = req.json().get("captcha")
        png_captcha = Image.open(BytesIO(base64.b64decode(captcha.split(",")[1])))
        png_captcha.show()
    else:
        raise
        

if __name__ == "__main__":
    main()