'''发送http请求'''
import requests


class HttpRequest():
    '''封装http请求'''
    '''# 传递参数要根据请求头部传，如为"Content-Type": "application/json"格式，就得用json=来传递参数，其他如表单就用data='''

    def send_request(self, method, url, data=None,  **kwargs):
        method = str(method).upper()
        try:
            if method == 'GET':
                res = requests.get(url, params=data, **kwargs)
            elif method == 'POST':
                res = requests.post(url, data=data,  **kwargs)
            else:
                print('请求方式不存在')
        except Exception as e:
            print('请求出错了{}'.format(e))
            raise e

        return res
     # 获取响应
    def get_respond(self):
        return self.res

    # 获取响应头
    def get_respond_head(self):
        head = self.res.headers
        return head

    # 获取响应体
    def get_respond_body(self):
        if self.res.content:
            respond = self.res.text
            return respond