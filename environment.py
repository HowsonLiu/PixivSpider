import os
import configparser
import base64

class Environment:
    """执行环境，包括p站账号密码和保存路径"""

    save_path = None
    account = None
    password = None
    account_encryp = None
    password_encryp = None

    ini_path = r'./setup.ini'
    cookies_path = r'./cookies.txt'
    binput = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Environment, cls).__new__(cls)
        return cls.instance

    def load_ini(self):
        if os.path.exists(self.ini_path):
            cfg = configparser.ConfigParser()
            cfg.read(self.ini_path)
            self.save_path = cfg['setting']['save_path']
            self.account_encryp = cfg['pixiv']['account']
            self.password_encryp = cfg['pixiv']['password']

    def save_ini(self):
        ini_file = open(self.ini_path, 'w')
        ini_str = '''
[setting]
; 保存路径
save_path = {save_path}
[pixiv]
; 账号
account = {account}
; 密码
password = {password}
'''
        ini_file.write(ini_str.format(save_path=self.save_path, account=self.account_encryp,
                                      password=self.password_encryp))
        ini_file.close()

    def encrpy_account_and_password(self):
        if self.binput:
            if self.account is not None:
                self.account_encryp = base64.b64encode(self.account.encode('utf-8')).decode("utf-8")
            if self.password is not None:
                self.password_encryp = base64.b64encode(self.password.encode('utf-8')).decode("utf-8")

    def decrpy_account_and_password(self):
        if self.account_encryp is not None:
            self.account = base64.b64decode(self.account_encryp.encode('utf-8'))
        if self.password_encryp is not None:
            self.password = base64.b64decode(self.password_encryp.encode('utf-8'))

    def check_save_path(self):
        """确保保存路径可用"""
        if self.save_path is None:
            self.save_path = input('请输入保存的路径：')
        while not os.path.exists(self.save_path):
            self.save_path = input('保存的路径不存在，请重新输入：')

    def set_account_and_password(self):
        self.account = input('输入Pixiv账号：')
        self.password = input('输入密码：')
        self.binput = True

    def load_cookies(self, se):
        try:
            se.cookies.load(filename=self.cookies_path, ignore_discard=True)
        except:
            pass

    def save_cookies(self, se):
        se.cookies.save(filename=self.cookies_path, ignore_discard=True, ignore_expires=True)

    def get_photo_name_save_path(self, photo_name):
        """根据图片名字和保存路径拼接处图片本地保存地址"""
        return os.path.join(self.save_path, photo_name)


env = Environment()
