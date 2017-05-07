# -*- coding: UTF-8 -*- 
#消费日志打印
import codecs
import time
import io
from _codecs import encode
def cost_logging_func(cardID,cost_type,cost_goods,cost_value,cost_interest=0):
    cost_file=io.open("../database/costlog.db",'a',encoding='utf-8')
    time_local=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    if cost_type == 1:
        cost_type="采购"
    else:
        cost_type="取现"
    cost_info="%s\t%s\t%s\t%s\t%s\t%s\n" % (time_local,cardID,cost_type,cost_goods,cost_value,cost_interest)
    print cost_info
    cost_file.write(unicode(cost_info,"utf-8"))
    cost_file.flush()
    cost_file.close()
    
# cost_logging_func("2",2, "IPAD", 2000)