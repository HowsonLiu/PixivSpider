from environment import env
import login
from myhttp import *
from iddownloader import IDDownloader

login = login.Login()

env.load_ini()
env.check_save_path()
env.load_cookies(se)
if not login.test_if_login():
    print("Cookies过期")
    env.decrpy_account_and_password()
    login.login(env.account, env.password)
    while not login.test_if_login():
        env.set_account_and_password()
        login.login(env.account, env.password)
    env.save_cookies(se)
    env.encrpy_account_and_password()
env.save_ini()
while True:
    id = input("输入Pixiv图片ID:")
    iddownloader = IDDownloader(id)
