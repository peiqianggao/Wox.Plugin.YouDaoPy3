# -*- coding: utf-8 -*-

import yd_query


def query(query):
    results = list()
    if not query:
        results.append({
            'Title': '请输入查询词汇',
            'SubTitle': 'yd word',
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
                    'parameters': ['{}'.format(res_list[0][0].split()[0])],
                }
            })

    return results


if __name__ == '__main__':
    print(query('Good'))
