# Create your views here.
#coding=utf-8

from django.shortcuts import render_to_response
from app.models import *
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required()

def def_info(req):
    action=req.GET.get('action')
    username=req.session["username"]
    sid=int(req.GET.get('sid'))
    obj=cust_login_log.objects
    error=""
    status=""
    if action == "select":

        if sid == 0:
            #type_obj=obj.all()
            type_obj=obj.order_by('-login_time')[0:1000]
            length_obj=len(type_obj)
            th_list=["用户ID","登录时间","登录ip","创建者ID","创建时间","更新者ID","更新时间"]
            return render_to_response("log_info.html",locals())

    elif action =="delete":
        data=req.POST["data"]
        n_data=data.split(",")
        for i in n_data:
            try:
                print i
                obj.get(id=i).delete()
                status=u"删除成功"
            except Exception,Ex:
                error=error+str(Ex)
        r_json={"status":status,"error":error}
        return HttpResponse(json.dumps(r_json))

    elif action == "update":
        data=req.POST["data"]
        n_data=data.split(",")

        try:
            obj.filter(id=sid).update(name=n_data[0],a_name=n_data[1],status=n_data[2],remarks=n_data[3])
            status=u"修改成功"
        except Exception,ex:
            error=error+str(ex)
        r_json={"status":status,"error":error}
        return HttpResponse(json.dumps(r_json))

    elif action == "add":
        data=req.POST["data"]
        n_data=data.split(",")
        try:
            obj.create(name=n_data[0],a_name=n_data[1],status=n_data[2],remarks=n_data[3])
            status="增加成功"
        except Exception,ex:
            error=error+str(ex)
        r_json={"status":status,"error":error}
        return HttpResponse(json.dumps(r_json))

    else:
        r_json={"status":status,"error":"no type"}
        return HttpResponse(json.dumps(r_json))
