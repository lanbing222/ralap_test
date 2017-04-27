import os
import sys
dict_list={}
with open("database/name.txt","r") as f:
    name_list=f.readlines()
    for name in name_list:
        wo=name.split()[0]
        dict_list[wo]=name.split()[1]
f.close()
print dict_list
# with open("src/name.txt",'a') as f:
#     f.writelines(name_list)
# user_name=raw_input("Please input your name:")
# if user_name in name_list:
#     user_passwd=raw_input("password:")
#     if user_passwd.split() == name_list[user_name][0]:
#         print "welcome "