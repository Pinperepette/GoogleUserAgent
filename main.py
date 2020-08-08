#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, session, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def avvio():
    return render_template('index.html')

@app.route('/googlebot', methods=['POST', 'GET'])
def googlebot():
    if request.method == 'POST': 
        url = request.form['url']
        headers = {'User-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; http://www.google.com/bot.html)'}
        r = requests.get(url, headers=headers)    
        soup = BeautifulSoup(r.text , "lxml")
        t = soup.find('main').text
        title = soup.find('title').text
        return render_template('testo.html', cursor=t, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
