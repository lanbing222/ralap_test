#coding=utf-8
#查询余额
from  collections import defaultdict
def  check_my_account(): 
    cardID_info_dict=defaultdict(list)
    with open("../database/bank_info.txt",'r') as f:
        line=f.readlines()
    f.close()
    for bank_line in line:    
        if len(bank_line)==0:continue
        bank_name=bank_line.split()[0]
        cardID_info_dict[bank_name].append(bank_line.split()[1])
        cardID_info_dict[bank_name].append(bank_line.split()[2])
    print cardID_info_dict
    cardID=raw_input("input your cardID:").strip()
    if cardID_info_dict.has_key(cardID):
        print "your card' limitd is ",cardID_info_dict[cardID][0]
        print "your card' rest is ",cardID_info_dict[cardID][1]
        return cardID_info_dict[cardID][0],cardID_info_dict[cardID][1]
    else:
        print "your card is not exists"
#         return -1
#     my_cardID=int(raw_input("input you cardID:"))


check_my_account()