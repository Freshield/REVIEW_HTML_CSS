#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: test_http.py
@Time: 2019-01-28 23:04
@Last_update: 2019-01-28 23:04
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import requests

payload = {'name':'yy', 'age':'28'}
proxies = {'http':'127.0.0.1:8000'}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
# ret = requests.get(url="http://www.bing.com/")
# ret = requests.post("http://httpbin.org/post", data=payload)
ret = requests.get('http://127.0.0.1:8000/test_http',timeout = 1)
print(ret.status_code)