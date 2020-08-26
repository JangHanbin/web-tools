import requests
import urllib3

from tagiter import TagSheet


def tag_finder(url, query, pre_param, cookies=None, headers=None):

    allows = list()
    tag_sheet = TagSheet()

    for tag in tag_sheet.tags():
        res = requests.get(url=url, headers=headers, cookies=cookies, data={query: pre_param.format(tag)})
        print('{0} : {1}'.format(tag, res.status_code))
        if res.status_code ==200:
            allows.append(tag)


    return allows


if __name__=='__main__':
    cookies = {
        'session': 'SIfHdj3b5GRcbylYWdfJPw5aC6XxwPb8',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://ac441f9e1eabc51780911cf1002f0086.web-security-academy.net/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    tag_finder(url='https://ac441f9e1eabc51780911cf1002f0086.web-security-academy.net/',query='search',pre_param='<{0}>', headers=headers,cookies=cookies)

