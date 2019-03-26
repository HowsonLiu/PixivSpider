import requests
import http.cookiejar as cj

se = requests.session()
se.cookies = cj.LWPCookieJar()

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'referer': '',
}

def get_html_response(url, headers):
    """ get指定url """
    try:
        res = se.get(url, headers=headers)
        if res.status_code != 200:
            print('GET ' + url + ' 失败, 状态码: ' + str(url.status_code))
            return None
    except:
        print('GET ' + url + ' 错误')
        return None
    return res


def post_data(url, data, headers):
    """ post data 到指定url"""
    try:
        res = se.post(url, data=data, headers=headers)
        if res.status_code != 200:
            print('POST ' + url + ' 失败, 状态码: ' + str(res.status_code))
            return None
    except:
        print('POST ' + url + ' 错误')
        return None
    return res
