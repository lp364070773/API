from utils.op_excel import operationExcel
from utils.op_json import operationJson
from data import data_conf
 
class getData(object):
    def __init__(self):
        self.op_excel = operationExcel()
 
    def get_case_lines(self):
        """获取表格行数"""
        return self.op_excel.get_rows()
 
    def get_is_run(self, x):
        """获取case是否运行"""
        flag = None
        y = data_conf.get_run()
        run_value = self.op_excel.get_cell_value(x, y)
        if run_value == 'yes':
            flag = True
        else:
            flag = False
        return flag
 
    def get_is_header(self, x):
        """是否携带header"""
        y = data_conf.get_request_header()
        header = self.op_excel.get_cell_value(x, y)
        if header == 'yes':
            return data_conf.get_header_value()
        else:
            return None
 
    def get_request_method(self, x):
        """获取请求方式"""
        y = data_conf.get_request_type()
        request_method = self.op_excel.get_cell_value(x, y)
        return request_method
 
    def get_request_url(self, x):
        """获取请求地址"""
        y = data_conf.get_url()
        request_url = self.op_excel.get_cell_value(x, y)
        return request_url
 
    def get_request_data(self, x):
        """获取请求数据"""
        y = data_conf.get_request_data()
        request_data = self.op_excel.get_cell_value(x, y)
        if request_data == '':
            return None
        return request_data
 
    def get_data_for_json(self, x):
        """通过excel中的关键字去获取json数据"""
        op_json = operationJson()
        data = op_json.get_key_words(self.get_request_data(x))
        return data
 
    def get_expect_data(self, x):
        """获取预期结果数据"""
        y = data_conf.get_expect_result()
        expect_data = self.op_excel.get_cell_value(x, y)
        if expect_data == '':
            return None
        return expect_data