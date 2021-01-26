import xlrd
 
data = xlrd.open_workbook("../test_data/rs.xls")
tables = data.sheets()[0]  # 获取表格数据对象
print(tables.nrows) # 打印表格行数
print(tables.cell_value(0,0))  # 打印excel表格数据，需要传递数据所在的坐标(x,y)
print(tables.cell_value(0,1))
print("*"*50+"封装前后数据对比"+"*"*50)
 
 
class operationExcel(object):
    def __init__(self, file_path="../test_data/rs.xls", sheet_id=0):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.data = self.get_data()
 
    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables
 
    def get_rows(self):
        """获取单元格的排数"""
        return self.data.nrows
 
    def get_cell_value(self, x=0, y=0):
        """获取某个单元格的数据"""
        return self.data.cell_value(x, y)
 
 
if __name__ == '__main__':
    print(operationExcel().get_rows())
    print(operationExcel().get_cell_value())
    print(operationExcel().get_cell_value(0,1))