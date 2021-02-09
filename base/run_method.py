
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
        S = requests.Session()
        if header is not None:
            res = S.post(url=url, data=data, headers=header,verify=False)
            # res = requests.post(url=url, data=data, headers=header,verify=False).json()
        else:
            res = S.post(url=url, data=data,verify=False)
            # res = requests.post(url=url, data=data,verify=False).json()
         
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        return res,cookies
        # if res.status_code == 200:
            
        #     for cookie in res.cookies:
        #         list_cookie= list_cookie.append(cookie)
        # print(list_cookie)    
        # return res


      
 
    def run_main(self, url, method, data=None, header=None):
        res = None
        if method.lower() == 'post':
            res = self.post_main(url, data, header)
        elif method.lower() == 'get':
            res = self.get_main(url, data, header)
        else:
            return "what ?????"
        return res

    def get_cookie():
        pass
       
if __name__ == '__main__':
    r = RunMain()
    data = {"logincode": "卢鹏",
        "pwd": "123456",
        "kindtype": "1",
        "operate": "login"}
    res = r.post_main('http://192.168.200.200:89/PageService/SystemManage/UserManage.ashx',data)
    print(res.cookies)