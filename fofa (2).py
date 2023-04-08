import re
import time

import requests
import base64
from concurrent.futures import ThreadPoolExecutor
b = input('请输入指令：')
base = base64.encodebytes(b.encode('utf-8'))
base_1 = str(base)
de = input("页数：")
obj = re.compile(r"b'(?P<bas>.*?)\\n'", re.S)
for iis in obj.finditer(base_1):
    ifs = iis.group('bas')
def fn(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Cookie": f"i18n_redirected=zh; Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1679551459,1679580178,1679661913; _ga_CX7MDY134G=GS1.1.1679567396.2.0.1679567396.0.0.0; _ga=GA1.1.356989473.1679551460; _ga_9GWBD260K9=GS1.1.1679661913.2.1.1679663836.0.0.0; __fcd=2IoGQRvQSkf4CBee51YBzDfr; is_flag_login=0; befor_router=%2Fresult%3Fqbase64%3DdGl0bGU9IuWQjuWPsCI%253D; isRedirectLang=1; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1679663478; baseShowChange=false; viewOneHundredData=false; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTA5NTcyLCJtaWQiOjEwMDA2NjExMiwidXNlcm5hbWUiOiJuZXZlcndpbiIsImV4cCI6MTY3OTkyMjM1N30.Pf94mFhwd4epsJTrSh59vpVw6VltBYjhXJJ7DdZqNkL7poI2r83Bgk4bbUXlrHeFZh-MLBCKv8prN4ONt6dqog; user=%7B%22id%22%3A109572%2C%22mid%22%3A100066112%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22neverwin%22%2C%22nickname%22%3A%22neverwin%22%2C%22email%22%3A%220810abc0810%40gmail.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%2221a081cecd0c1eb0b931e4ce770dc7b4%22%2C%22rank_name%22%3A%22%E9%AB%98%E7%BA%A7%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A2%2C%22company_name%22%3A%22neverwin%22%2C%22coins%22%3A35%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1679663157%2C%22data_limit%22%3Anull%2C%22fpoint_upgrade%22%3Afalse%7D"
        }
    resp = requests.get(url, headers=header)
    obj_1 = re.compile(r'<span class="hsxa-host"><a href="(?P<web>.*?)" target="_blank">', re.S)
    for it in obj_1.finditer(resp.text):
        print(it.group('web'))


with ThreadPoolExecutor(2) as f:
    for iss in range(1, int(de)):
        f.submit(fn, f"https://fofa.info/result?qbase64={ifs}&page={iss}&page_size=20")

