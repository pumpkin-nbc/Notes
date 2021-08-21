# -*- coding: utf-8 -*-
# @Author  : Pumpkin
# @Time    : 2021/7/31 23:28
# @Software: PyCharm
# @File    : reptile_main.py
# @Mail    : a760329881@qq.com
import json

import Crypto.Cipher.AES
import requests
from Crypto.Cipher import AES
import base64

d = {"csrf_token": "",
     "cursor": "-1",
     "offset": "0",
     "orderType": "1",
     "pageNo": "1",
     "pageSize": "20",
     "rid": "R_SO_4_1859245776",
     "threadId": "R_SO_4_1859245776"}

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"

i = "sOezohwl1I8tmKl1"


def encseckey_value():
    encSecKey = "4f9db66d4ea80985c908fcbe138a1720e77831ee63856a26dbdd0d8ed3607697f6e9036f1fbabf0eb769f4c1289e3f29265a2c642fbe0c45a518fa378901ca210f54f413f53d5608e3f61940af4b207431235bc68be0b639434ea57ec399514d722cee63e52021d61271ab7212b2f72a998798c033d7ca9a3fcff939a3e99e5f"

    return encSecKey


def jiami(data, key):
    iv = "0102030405060708".encode('UTF-8')
    aes = AES.new(key=key.encode('UTF-8'), mode=AES.MODE_CBC, iv=iv)
    bs = aes.encrypt(to_16(data).encode('UTF-8'))
    return str(base64.b64encode(bs),'utf-8')


def to_16(data):
    a = 16 - len(data) % 16
    data += chr(a)*a
    return data

def params_value(data, key, i):
    a = jiami(data, key)
    return jiami(a, i)



wangyiyun_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
data = {
    "params": params_value(json.dumps(d),g,i),
    "encSecKey": encseckey_value()}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

a = requests.post(url=wangyiyun_url, data=data, headers=headers)
a.close()
print(a.text)


"""
!function() {
    function a(16) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; 16 > d; d += 1)
            e = Math.random() * b.length, 随机数*
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {  d g
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) { i e f
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16); 返回一个随机的字符串 总共16位i="sOezohwl1I8tmKl1"
        return h.encText = b(d, g),
        h.encText = b(h.encText, i), 得到最终的enctext
        # h.encSecKey = c(i, e, f), encSecKey
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();
"""
