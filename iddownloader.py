from myhttp import *
import re
from environment import env

class IDDownloader:
    url = r'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'
    save_path = None
    headers = None

    def __init__(self, id):
        self.url = self.url.format(id)
        self.headers = HEADERS
        res = get_html_response(self.url, self.headers)
        img_url = self.find_img_url(res)
        if img_url is None:
            return
        self.save_path = env.get_photo_name_save_path(str(id) + img_url[-4:])
        self.download(img_url)

    def find_img_url(self, res):
        """ 返回大图url """
        regex = r'original":"(.+?)"},'
        # regex = r'regular":"(.+?)",'
        pattern = re.compile(regex, flags=re.M | re.S)
        try:
            link = pattern.search(res.text)
            if not link:
                return None
        except:
            print('大图地址获取错误')
            return None
        return link.group(1).replace(r'\\'[:-1], "")

    def download(self, img_url):
        """ 下载图片 """
        self.headers['referer'] = self.url
        res = get_html_response(img_url, self.headers)
        try:
            assert res
            with open(self.save_path, 'wb') as f:
                f.write(res.content)
        except:
            print('图片下载失败 ' + self.url)
