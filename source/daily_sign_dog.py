import json
import os
import requests

cookie = os.environ.get("DOG_COOKIE")
# account = os.environ.get("DOG_ACCOUNT")
# password = os.environ.get("DOG_PASSWORD")
account = "wDog233"
password = "112233"

# 登录URL
loginUrl = "https://sssvv8.com/api/v5/account/login"
# 签到URL
checkinUrl = "https://sssvv8.com/api/v5/account/checkin"
# 签到状态URL
statusUrl = "https://sssvv8.com/api/v5/account/info"
# token
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36";
# 账号密码
params = {"account": account, "password": password}

headers = {"Content-Type": "application/json;charset=UTF-8",
           "User-Agent": userAgent}

response = requests.post(url=loginUrl, headers=headers, data=json.dumps(params))
res = json.loads(response.text)
print(res)
if res["code"] == 0:
    # 登陆成功
    print(response.headers.get("set-cookie"))
