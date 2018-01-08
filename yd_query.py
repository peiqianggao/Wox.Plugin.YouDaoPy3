# -*- coding: utf-8 -*-

import hashlib
import random

import requests

import settings


def query(search):
    salt = random.randint(1, 65536)
    sign = hashlib.md5((settings.ydAppId + search + str(salt) + settings.ydAppSecret).encode()).hexdigest()
    try:
        response = requests.get(settings.ydApiUrl.format(settings.ydAppId, requests.utils.quote(search), salt, sign))
        if response.status_code == requests.codes.ok:
            json_res = response.json()
            err_code = json_res.get('errorCode')
            if err_code != '0':
                return None
            # parse content
            res_list = list()
            url = None
            trs = json_res.get('translation')
            basic = json_res.get('basic')
            web = json_res.get('web')
            webdict = json_res.get('webdict')
            if trs:
                if basic:
                    pron = basic.get('us-phonetic')
                for tr in trs:
                    if tr not in res_list:
                        res_list.append(['{} {}'.format(tr, pron), '<<< Click To Copy Word >>>'])
            if basic:
                res_list.append(['; '.join(basic.get('explains')), '基本词典'])
            if web:
                for w in web:
                    key = w.get('key')
                    res_list.append(['; '.join(w.get('value')), '网络释义: {}'.format(key)])
            if webdict:
                url = webdict.get('url')

            return res_list, url

    except Exception:
        return None


if __name__ == '__main__':
    print(query('good'))
