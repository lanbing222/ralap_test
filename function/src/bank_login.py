#coding=utf-8
#登陆认证模块
from  collections import defaultdict
def bank_login_fun():
    bank_info_dict=defaultdict(list)
    with open("../database/indent_ID.txt",'r') as f:
        line=f.readlines()
    f.close()
    for bank_line in line:    
        if len(bank_line)==0:continue
        bank_name=bank_line.split()[0]
        bank_info_dict[bank_name].append(bank_line.split()[1])
        bank_info_dict[bank_name].append(bank_line.split()[2])
    
    login_times=0
    while True:
        if login_times > 2 : break
        bank_login_name=raw_input("please input your name:").strip()
        if len(bank_login_name) == 0: 
            login_times=login_times+1
            continue
        if bank_info_dict.has_key(bank_login_name):
            bank_login_passwd=raw_input("password:").strip()
            if bank_login_passwd==bank_info_dict[bank_login_name][0]:
                print "congraduation"
                return 1
        else:
            print "sorry ,your name is not exist,please check!!" 
            return 0
        login_times=login_times+1
bank_login_fun()
