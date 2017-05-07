#coding=UTF8
#花销
# import time
import pickle
import costlog
def cost_charge_fun(cardID,cost_type,cost_goods,cost_value):
#     time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    card_myaccout_info=file("../database/bank_info.db",'r')
    card_myaccout_dict=pickle.load(card_myaccout_info)
    card_myaccout_info.close()
    if float(cost_value) < float(card_myaccout_dict[cardID][1]):
        if int(cost_type)==1:
            card_myaccout_dict[cardID][1]=float(card_myaccout_dict[cardID][1])-float(cost_value)
            costlog.cost_logging_func(cardID,cost_type,cost_goods,cost_value)
        else:
            cost_interest=float(cost_value)*0.05
            card_myaccout_dict[cardID][1]=float(card_myaccout_dict[cardID][1])-float(cost_value)-cost_interest
            costlog.cost_logging_func(cardID,cost_type,cost_goods,cost_value,cost_interest)
    else:
        print "your card number is not enough to pay this goods"
    card_myaccout_info=file("../database/bank_info.db",'w')
    card_myaccout_info.write(pickle.dumps(card_myaccout_dict))
    card_myaccout_info.close()
    
cost_charge_fun('1',1,"T-shit",2000)