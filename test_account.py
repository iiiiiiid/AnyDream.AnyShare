import json
import requests

url_account = "http://47.117.114.2:9000/user/username?"


class TestUserLogin(object):

    def test_get_username_success(self):
        para = {
            'username': 'li.si@aishu.cn',
            # 'password': '1234'
        }
        response = requests.get(url=url_account, params=para)
        print(response.json())
        res = response.json()["message"]
        assert res == "账号存在"
