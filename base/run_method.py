
import requests,urllib3
from urllib3.exceptions import InsecureRequestWarning
#禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)
 
class RunMain(object):
 
    def get_main(self, url, data=None, header=None):
        res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header,verify=False)
            # res = requests.get(url=url, data=data, headers=header,verify=False).json()
        else:
            res = requests.get(url=url, data=data,verify=False)
            # res = requests.get(url=url, data=data,verify=False).json()
        return res
 
    def post_main(self, url, data, header=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header,verify=False)
            # res = requests.post(url=url, data=data, headers=header,verify=False).json()
        else:
            res = requests.post(url=url, data=data,verify=False)
            # res = requests.post(url=url, data=data,verify=False).json()
        return res
 
 
    def run_main(self, url, method, data=None, header=None):
        res = None
        if method.lower() == 'post':
            res = self.post_main(url, data, header)
        elif method.lower() == 'get':
            res = self.get_main(url, data, header)
        else:
            return "what ?????"
        return res