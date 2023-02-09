import requests
from requests.adapters import HTTPAdapter
from urllib3.exceptions import ConnectTimeoutError, NewConnectionError

rs = requests.Session()
rs.mount('http://', HTTPAdapter(max_retries=1))

for i in range(2, 256):
    ip = i
    ss=''
    ourl = f'http://192.168.200.{ip}'
    try:
        ss = rs.post(url=ourl, timeout=0.05)
    except (ConnectionError, ConnectTimeoutError, requests.exceptions.ConnectTimeout,
            ConnectionRefusedError, NewConnectionError):
        print(f'服务器地址 {ourl} 不可用')
    if str(ss) == '<Response [200]>':
        print(f'寻址完毕，服务器当前位置：{ourl.replace("http://", "")}')
        break
