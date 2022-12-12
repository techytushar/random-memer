#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Tushar Mittal (chiragmittal.mittal@gmail.com)
Flask API to return random meme images
"""

import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def get_new_memes():
    """Scrapers the website and extracts image URLs

    Returns:
        imgs [list]: List of image URLs
    """
    url = 'https://www.memedroid.com/memes/tag/programming'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    divs = soup.find_all('div', class_='item-aux-container')
    imgs = []
    for div in divs:
        img = div.find('img')['src']
        if img.startswith('http') and img.endswith('jpeg'):
            imgs.append(img)
    return imgs


def serve_pil_image(pil_img):
    """Stores the downloaded image file in-memory
    and sends it as response

    Args:
        pil_img: Pillow Image object

    Returns:
        [response]: Sends image file as response
    """
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.after_request
def set_response_headers(response):
    """Sets Cache-Control header to no-cache so GitHub
    fetches new image everytime
    """
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/", methods=['GET'])
def return_meme():
    img_url = random.choice(get_new_memes())
    res = requests.get(img_url, stream=True)
    res.raw.decode_content = True
    img = Image.open(res.raw)
    return serve_pil_image(img)
