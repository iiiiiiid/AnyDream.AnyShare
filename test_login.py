import json
import requests

url_login = "http://47.117.114.2:9000/user/login?"


class TestUserLogin(object):
    def test_login_success(self):
        json = {
            'username': 'li.si@aishu.cn',
            'password': '1234'
        }
        response = requests.post(url=url_login, json=json)
        print(response.json())
        res = response.json()["message"]
        assert res == "登陆成功"

    def test_error_password_login_failed(self):
        json = {
            'username': 'li.si@aishu.cn',
            'password': '123334'
        }
        response = requests.post(url=url_login, json=json)
        print(response.json())
        res = response.json()["message"]
        assert res == "账号密码不匹配"

    def test_error_username_login_failed(self):
        json = {
            'username': 'li.si123@aishu.cn',
            'password': '1234'
        }
        response = requests.post(url=url_login, json=json)
        print(response.json())
        res = response.json()["message"]
        assert res == "该账号不存在"
