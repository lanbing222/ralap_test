#coding=utf-8
#调整余额
import pickle
def adjustment_account(indent_id,change_card_limit):  
    adjustment_bank_info_file=file("../database/bank_info.db",'r')
    bank_info_dict=pickle.load(adjustment_bank_info_file)
    adjustment_bank_info_file.close()
    if bank_info_dict.has_key(indent_id):
        bank_info_dict[indent_id][0]=int(bank_info_dict[indent_id][0])+int(change_card_limit)
        bank_info_dict[indent_id][1]=int(bank_info_dict[indent_id][1])+int(change_card_limit)
        print "you account is %s" % bank_info_dict[indent_id][0]
        print "you rest account is %s" % bank_info_dict[indent_id][1]
    adjustment_bank_info_file=file("../database/bank_info.db",'w')
    adjustment_bank_info_file.write(pickle.dumps(bank_info_dict))
    adjustment_bank_info_file.close()
    print bank_info_dict
adjustment_account('1',1000)
