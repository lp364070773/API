class global_var:
    id = 0  # id
    module = 1  # 模块
    url = 2  # url
    run = 3  # 是否运行
    request_type = 4 # 请求类型
    request_header = 5  # 是否携带header
    case_depend = 6  # case依赖
    response_data_depend = 7  # 依赖的返回数据
    data_depend = 8  #  数据依赖
    request_data = 9  # 请求数据
    expect_result = 10  # 预期结果
    reality_result = 11  # 实际结果
 
 
def get_id():
    return global_var.id
 
def get_module():
    return global_var.module
 
def get_url():
    return global_var.url
 
def get_run():
    return global_var.run
 
def get_request_type():
    return global_var.request_type
 
def get_request_header():
    return global_var.request_header
 
def get_case_depend():
    return global_var.case_depend
 
def get_response_data_depend():
    return global_var.response_data_depend
 
def get_data_depend():
    return global_var.data_depend
 
def get_request_data():
    return global_var.request_data
 
def get_expect_result():
    return global_var.expect_result
 
def get_reality_result():
    return global_var.reality_result