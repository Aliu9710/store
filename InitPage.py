# -*- codeing = utf-8 -*-
# @time : 2021/10/12 15:46
# @Author : 张刘生
# @File : InitPage.py
# @Software: PyCharm
import xlrd


# 打开工作簿
wb = xlrd.open_workbook(filename="HKR.xlsx", encoding_override=True)
# 获取所有工作簿选项卡个数
# 获取第1个选项卡
st0 = wb.sheet_by_index(0)
# 获取有多少行
rows0 = st0.nrows
#获取列
cols0=st0.ncols
#获取第2个选项卡
st1 = wb.sheet_by_index(1)
# 获取有多少行
rows1 = st1.nrows
#获取列
cols1=st1.ncols
#创建空的成功列表
login_success_data =[]
#开始循环读取差
for i in range(1,rows0):
    ctype=st0.cell(i,0).ctype
    no = st0.cell(i,0).value
    if ctype == 2:
        no = str(int(no))

    ctype = st0.cell(i,1).ctype
    no1 =st0.cell(i,1).value
    if ctype == 2 :
        no1 =str(int(no1))


    ctype = st0.cell(i,2).ctype
    no2 = st0.cell(i,1).value
    if ctype == 2:
        no2 = str(int(no2))

    data1 ={'username':no,
            'password':no1,
            'expect':no2
    }
    login_success_data.append(data1)


#创建空的失败用列
login_error_data = []
# 开始循环读取差
for i in range(1, rows0):
    ctype = st1.cell(i, 0).ctype
    no3 = st1.cell(i, 0).value
    if ctype == 2:
        n03 = str(int(no3))

    ctype = st1.cell(i, 1).ctype
    no4 = st1.cell(i, 1).value
    if ctype == 2:
        no4 = str(int(no4))

    ctype = st1.cell(i, 2).ctype
    no5 = st1.cell(i, 1).value
    if ctype == 2:
        no5 = str(int(no5))

    data2 = {'username': no3,
            'password': no4,
            'expect': no5
        }
    login_error_data.append(data2)
class InitPage:
    login_success_data=login_success_data
    login_error_data=login_error_data



    '''
class InitPage:
    login_success_data =[
        {"username":"jason","password":"1234567","expect": "Student Login"},
        {"username": "不再爱了","password":"1234567","expect": "Student Login"}
    ]
    #错误用户
    login_error_data = [
        # id : msg_uname
        {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]

'''















