# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from myhttp import *

class Login:
    """登陆"""

    login_url = r'https://accounts.pixiv.net/login?lang=en&source=pc&view_type=page&ref=wwwtop_accounts_index'
    post_url = r'https://accounts.pixiv.net/api/login?lang=en'
    test_url = 'https://www.pixiv.net/'
    # post avgs
    data = {
        'pixiv_id': '',
        'password': '',
        'captcha': '',
        'g_recaptcha_response': '',
        'source': 'pc',
        'ref': 'wwwtop_accounts_index',
        'return_to': 'https://www.pixiv.net/',
        'post_key': ''
    }

    def test_if_login(self):
        """ 判断是否登录 """
        try:
            res = get_html_response(self.test_url, HEADERS)
            soup = BeautifulSoup(res.text, 'lxml')
            login_flag = soup.body.get('class')
            if login_flag:
                return False
        except:
            print('无法检验是否登录，可能网页更新，建议退出')
            return False
        return True

    def login(self, account, password):
        self.data['pixiv_id'] = account
        self.data['password'] = password
        login_res = get_html_response(self.login_url, HEADERS)
        post_key = self.get_post_key(login_res)
        if post_key is None:
            return
        self.data['post_key'] = post_key
        post_data(self.post_url, self.data, HEADERS)

    def get_post_key(self, res):
        """ 获取post_key，用于登录 """
        try:
            soup = BeautifulSoup(res.text, 'lxml')
            post_key = soup.find('input').get('value')
        except:
            print('PostKey获取错误，可能网页更新，建议退出')
            return None
        return post_key
