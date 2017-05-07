#-*-coding: utf-8 -*-
 
import codecs
u = u'怒焰裂谷'
ll = [u]  
#f = codecs.open('test1.txt', 'w', encoding='UTF-8')
f = open('test1.txt', 'w')
f.write(u)
f.write('%s'%ll)
f.write('['+'%s'%u+']')
f.write('['+'%r'%u+']')
   
f.close()