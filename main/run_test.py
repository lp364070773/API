import os , sys , json ,requests

sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))

from base.run_method import RunMain
from data.data_get import getData
 
 
class RunTest(object):
    def __init__(self):
        self.runmain = RunMain()
        self.data = getData()
 
    def run(self):
        res = None
        row_counts = self.data.get_case_lines()  # 获取excel表格行数
        # print(row_counts) 
        for row_count in range(1, row_counts):
            # print(row_count) 
            url = self.data.get_request_url(row_count)  # y行不变遍历获取x列的请求地址
            method = self.data.get_request_method(row_count)  # y行不变遍历获取x列的请求方式
            is_run = self.data.get_is_run(row_count)  # y行不变遍历获取x列的是否运行
            data = self.data.get_data_for_json(row_count)  # y行不变遍历获取x列的请求数据，这里面时三次调用，依次分别是get_data_for_json丶get_key_words丶get_request_data
            header = self.data.get_is_header(row_count)
            
            print('url:', url)
            print('method:', method)
            print('is_run:', is_run)
            print('data:', data)
            print('header:', header)
 
            if is_run:
                res = self.runmain.run_main(url,method,data,header)
                # print('type:',type(res))
                
                res_cookie = res[1]
                res = res[0]
                print(res_cookie) 
                print("*"*60+"分割线"+"*"*60)
        return res
 
 
if __name__ == '__main__':
    print('res:', RunTest().run())