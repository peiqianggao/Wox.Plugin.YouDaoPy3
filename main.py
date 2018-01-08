# -*- coding: utf-8 -*-
import os
import webbrowser

import pyperclip
from wox import Wox, WoxAPI

import yd_query

result_template = {
    'Title': '{}',
    'SubTitle': '{}',
    'IcoPath': 'images/youdao.ico',
    'JsonRPCAction': {
        'method': 'copy_to_clipboard',
        'parameters': ['{}'],
    }
}

RANDOM_STR = "0123456789_AaBbCcDdEeFfGgHhIiJjKkLlMmNn0123456789OoPpQqRrSsTtUuVvWwXxYyZz0123456789"


class WoxPluginYouDaoPy3(Wox):
    def query(self, query=None):
        results = list()
        if not query:
            results.append({
                'Title': '请输入查询词汇',
                'SubTitle': 'yd 你要查的词',
                'IcoPath': 'images/youdao.ico'}
            )
            return results

        res = yd_query.query(query)
        if res:
            res_list, url = res
            results.append({
                'Title': '{}'.format(res_list[0][0]),
                'SubTitle': '{}'.format(res_list[0][1]),
                'IcoPath': 'images/youdao.ico',
                'JsonRPCAction': {
                    'method': 'copy_to_clipboard',
                    'parameters': ['{}'.format(res_list[0][0].split()[0])],
                }}
            )

            for r in res_list[1:]:
                results.append({
                    'Title': '{}'.format(r[0]),
                    'SubTitle': '{}'.format(r[1]),
                    'IcoPath': 'images/youdao.ico',
                    'JsonRPCAction': {
                        'method': 'copy_to_clipboard',
                        'parameters': ['{}'.format(r[0])],
                    }
                }
                )

            if url:
                results.append({
                    'Title': '{}'.format('点击打开查询页面'),
                    'SubTitle': '{}'.format(url),
                    'IcoPath': 'images/youdao.ico',
                    'JsonRPCAction': {
                        'method': 'openUrl',
                        'parameters': ['{}'.format(url)],
                    }
                })

        return results

    def openUrl(self, url):
        # webbrowser.open(url)
        webbrowser.open_new_tab(url)
        WoxAPI.change_query(url)

    def copy_to_clipboard(self, value):
        """
        Copies the given value to the clipboard.
        WARNING:Uses yet-to-be-known Win32 API and ctypes black magic to work.
        """
        try:
            pyperclip.copy(value)
        except IOError:
            command = 'echo ' + value + '| clip'
            os.system(command)
        return None


if __name__ == "__main__":
    WoxPluginYouDaoPy3()
