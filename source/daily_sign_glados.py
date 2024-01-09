import json
import requests
from requests.exceptions import HTTPError


class GlaDosJob:

    def __init__(self):
        self.checkin_url = "https://glados.rocks/api/user/checkin"
        self.status_url = "https://glados.rocks/api/user/status"
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

    def sign_in_job_handler(self, sign_user_info):
        sign_user_info_json_object = json.loads(sign_user_info)

        for user, authorization_json_object in sign_user_info_json_object.items():
            authorization = authorization_json_object['authorization']
            cookie = authorization_json_object['cookie']
            token = authorization_json_object['token']
            self.check_in(token, authorization, self.user_agent, cookie, user)

    def check_in(self, token, authorization, user_agent, cookie, user):
        headers = {
            "user-agent": user_agent,
            "cookie": cookie,
            "authorization": authorization
        }

        before_days = self.get_left_day_by_status(user)

        data = {'token': token}
        try:
            checkin_resp = requests.post(self.checkin_url, headers=headers, data=data)
            checkin_resp.raise_for_status()

            result = checkin_resp.json()
            message = result.get('message')
            code = result.get('code')

            if code == 0:
                after_days = self.get_left_day_by_status(user)
                points = result.get('points')
                print(f'{user}签到成功！之前{before_days}天，之后{after_days}天，今天获取点数：{points}')
            elif code == 1:
                print(f'{user}已成功签到，当前重复签到')
            else:
                print(f'{user}签到失败！message：{message}')
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

    def get_left_day_by_status(self, user):
        headers = {
            "user-agent": self.user_agent,
            "cookie": self.cookie,
            "authorization": self.authorization
        }
        try:
            status_resp = requests.get(self.status_url, headers=headers)
            status_resp.raise_for_status()

            status_body = status_resp.json()
            status_data = status_body.get('data')

            if status_data is None:
                print(f'{user}签到失败！message：{status_body.get("message")}')
                return 0

            return status_data.get('leftDays')
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return 0


# 使用示例
if __name__ == '__main__':
    gla_dos_job = GlaDosJob()
    # 假设这里有一个从哪里来的sign_user_info字符串
    sign_user_info = '{"user1":{"authorization":"Bearer xxx","cookie":"_ga=xxx; _gid=xxx; _gat=1","token":"xxx"}}'
    gla_dos_job.sign_in_job_handler(sign_user_info)
