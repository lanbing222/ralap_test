#coding=UTF8
#check消费清单
import json
import codecs
import uniout
def check_bill(cardID,bill_date):
    cost_file=open("../database/costlog.db",'r')
    for cost_info in cost_file:
        if cost_info == '\n' or cost_info.isspace():
            continue
        cost_info_list=cost_info.split('\t')
        if  bill_date in cost_info_list[0] and int(cost_info_list[1]) == int(cardID) :
            print cost_info_list
#         print ''.join(cost_info),
#         print str(cost_info).decode('string_escape')
check_bill(1,'2017-04')   