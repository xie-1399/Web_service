######################################
# Django 模块
######################################
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse

######################################
# 第三方模块
######################################
from pure_pagination import PageNotAnInteger, Paginator

######################################
# 系统模块
######################################
import json
import datetime

######################################
# 自建模块
######################################
from utils.login_check import LoginStatusCheck
from .Degree_information import go_search
from .forms import *
from .models import *


######################################
# 就业情况统计
######################################
class CompanyPlatformListView(LoginStatusCheck, View):
    def get(self, request):
        title = '就业情况统计'
        # platforms1=Total.objects.filter(is_province_employ="本省").count()
        # platforms2=Total.objects.filter(is_province_employ="西部").count()
        # platforms3=Total.objects.filter(is_province_employ="东部").count()
        # platforms4=Total.objects.filter(is_province_employ="中部").count()
        #print(platforms1,platforms2,platforms3,platforms4)
        ym_lists=['2012','2013','2014','2015',]
        tr_lists = [324,229,451,579]
        province=[781,125,482,160]
        # 对取到的数据进行分页，记得定义每页的数量
        context = {
            'title': title,
            'ym_lists': ym_lists,
            'tr_lists':tr_lists,
        }
        return render(request, 'platform-management/platform_analy.html', context=context)


######################################
# 就业分布地图模块
######################################
class OpsPlatformListView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        title = '就业分布地图'
        platforms_shan = Total.objects.filter(unit_location__startswith="山东").count()
        platforms_bei = Total.objects.filter(unit_location__startswith="北京").count()
        platforms_tian = Total.objects.filter(unit_location__startswith="天津").count()
        platforms_shang = Total.objects.filter(unit_location__startswith="上海").count()
        platforms_chong = Total.objects.filter(unit_location__startswith="重庆").count()
        platforms_hebei = Total.objects.filter(unit_location__startswith="河北").count()
        platforms_henan = Total.objects.filter(unit_location__startswith="河南").count()
        platforms_yun = Total.objects.filter(unit_location__startswith="云南").count()
        platforms_liao = Total.objects.filter(unit_location__startswith="辽宁").count()
        platforms_hei = Total.objects.filter(unit_location__startswith="黑龙江").count()
        platforms_hunan = Total.objects.filter(unit_location__startswith="湖南").count()
        platforms_an = Total.objects.filter(unit_location__startswith="安徽").count()
        platforms_xin = Total.objects.filter(unit_location__startswith="新疆").count()
        platforms_jiang = Total.objects.filter(unit_location__startswith="江苏").count()
        platforms_zhe = Total.objects.filter(unit_location__startswith="浙江").count()
        platforms_jiangxi = Total.objects.filter(unit_location__startswith="江西").count()
        platforms_hubei = Total.objects.filter(unit_location__startswith="湖北").count()
        platforms_guangxi = Total.objects.filter(unit_location__startswith="广西").count()
        platforms_gan = Total.objects.filter(unit_location__startswith="甘肃").count()
        platforms_shanxi = Total.objects.filter(unit_location__startswith="山西").count()
        platforms_nei = Total.objects.filter(unit_location__startswith="内蒙古").count()
        platforms_shan_xi = Total.objects.filter(unit_location__startswith="陕西").count()
        platforms_ji = Total.objects.filter(unit_location__startswith="吉林").count()
        platforms_fu= Total.objects.filter(unit_location__startswith="福建").count()
        platforms_gui= Total.objects.filter(unit_location__startswith="贵州").count()
        platforms_guangdong = Total.objects.filter(unit_location__startswith="广东").count()
        platforms_qinghai = Total.objects.filter(unit_location__startswith="青海").count()
        platforms_xizang = Total.objects.filter(unit_location__startswith="西藏").count()
        platforms_sichuan = Total.objects.filter(unit_location__startswith="四川").count()
        platforms_ningxia = Total.objects.filter(unit_location__startswith="宁夏").count()
        platforms_hainan = Total.objects.filter(unit_location__startswith="海南").count()
        platforms_taiwan = Total.objects.filter(unit_location__startswith="台湾").count()
        platforms_xiang = Total.objects.filter(unit_location__startswith="香港").count()
        platforms_ao = Total.objects.filter(unit_location__startswith="澳门").count()
        context = {
            'title': title,
            'platforms_shan':platforms_shan,
            'platforms_bei':platforms_bei,
            'platforms_tian':platforms_tian,
            'platforms_shang':platforms_shang,
            'platforms_chong':platforms_chong,
            'platforms_hebei' :platforms_hebei,
            'platforms_henan' :platforms_henan,
            'platforms_yun':platforms_yun,
            'platforms_liao':platforms_liao,
            'platforms_hei' :platforms_hei,
            'platforms_hunan' :platforms_hunan,
            'platforms_an' :platforms_an,
            'platforms_xin' :platforms_xin,
            'platforms_jiang' :platforms_jiang,
            'platforms_zhe' :platforms_zhe,
            'platforms_jiangxi' :platforms_jiangxi,
            'platforms_hubei' :platforms_hubei,
            'platforms_guangxi' :platforms_guangxi,
            'platforms_gan' :platforms_gan,
            'platforms_shanxi' :platforms_shanxi,
            'platforms_nei':platforms_nei,
            'platforms_shan_xi' :platforms_shan_xi,
            'platforms_ji' :platforms_ji,
            'platforms_fu':platforms_fu,
            'platforms_gui':platforms_gui,
            'platforms_guangdong' :platforms_guangdong,
            'platforms_qinghai' :platforms_qinghai,
            'platforms_xizang':platforms_xizang,
            'platforms_sichuan':platforms_sichuan,
            'platforms_ningxia':platforms_ningxia,
            'platforms_hainan' :platforms_hainan,
            'platforms_taiwan' :platforms_taiwan,
            'platforms_xiang' :platforms_xiang,
            'platforms_ao' :platforms_ao,
        }
        return render(request, 'platform-management/platform_list.html', context=context)


######################################
# 编辑平台用户列表
######################################
class EditPlatformUserView(LoginStatusCheck, View):
    def post(self, request):
        try:
            pu_id = request.POST.get('pu_id', '')
            if pu_id != '':
                pu = PlatformUserInfo.objects.get(id=int(pu_id))
                pu.username = request.POST.get('username', '')
                pu.password = request.POST.get('password', '')
                pu.update_user = request.user
                pu.save()
            else:
                platform_id = int(request.POST.get('platform_id'))
                pu = PlatformUserInfo()
                pu.platform_id = platform_id
                pu.username = request.POST.get('username', '')
                pu.password = request.POST.get('password', '')
                pu.user = request.user
                pu.update_user = request.user
                pu.save()
            return HttpResponse('{"status":"success", "msg":"修改用户成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"修改用户失败！"}', content_type='application/json')


######################################
# 其它平台列表
######################################
class OtherPlatformListView(LoginStatusCheck, View):
    def get(self, request):
        # 页面选择
        web_chose_left_1 = 'platform'
        web_chose_left_2 = 'other'
        web_chose_middle = ''
        title = '数据中心'
        #total_infors = Total.objects.all()
        platforms= Total.objects.all()
        #platforms=PlatformInfo.objects.filter(belong=3).filter(add_user=request.user)
        #搜索
        keyword = request.GET.get('keyword', '')
        if keyword != '':
            platforms = platforms.filter(Q(stu_num__icontains=keyword) | Q(sex__icontains=keyword)| Q(major__icontains=keyword)| Q(department__icontains=keyword)|Q(unit__icontains=keyword)|Q(year__icontains=keyword))
        platform_nums = platforms.count()

        #判断页码
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对取到的数据进行分页，记得定义每页的数量
        p = Paginator(platforms, 13, request=request)
        # 分页处理后的 QuerySet
        platforms = p.page(page)

        context = {
            'web_chose_left_1': web_chose_left_1,
            'web_chose_left_2': web_chose_left_2,
            'web_chose_middle': web_chose_middle,
            'title': title,
            'platforms': platforms,
            'platform_nums': platform_nums,
            # 'total_infors':totals_infors,
        }
        return render(request, 'platform-management/user_platform_list.html', context=context)


######################################
# 添加就业数据信息
######################################
class AddOtherPlatformView(LoginStatusCheck, View):
    def post(self, request):
        try:
            stu_num = request.POST.get("stu_num")
            sex= request.POST.get("sex")
            major=request.POST.get("major")
            department=request.POST.get("department")
            unit=request.POST.get("unit")
            unit_address=request.POST.get("unit_address")
            education=request.POST.get("education")
            year=request.POST.get("year")
            if (stu_num != "") and (sex != "")and (major != "")and (department != "")and (unit != "")and (unit_address != "")and (education != "")and (year != ""):
                plat_obj = Total()
                plat_obj.stu_num = stu_num
                plat_obj.sex = sex
                plat_obj.major= major
                plat_obj.department = department
                plat_obj.unit = unit
                plat_obj.unit_address = unit_address
                plat_obj.education = education
                plat_obj.year = year
                plat_obj.save()
                return HttpResponse('{"status":"success", "msg":"添加就业信息成功！"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"failed", "msg":"填写错误！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"未知错误！"}', content_type='application/json')

######################################
# 删除就业数据信息
######################################
class DeletePlatformUserView(LoginStatusCheck, View):
    def post(self, request):
        try:
            check_list = request.POST.getlist("msg_delete")
            print(check_list)
            if len(check_list):
                for each in check_list:
                    print(each)
                    each_infor = Total.objects.get(id=int(each))
                    each_infor.delete()
            # context={
            #     "status":"success",
            #     "msg":"删除成功",
            # }
            #return  render(request,'platform-management/user_platform_list.html',context=context)
            return HttpResponse('{"status":"success", "msg":"删除成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"删除失败！"}', content_type='application/json')

######################################
# 更改就业数据信息
######################################
class UpdatePlatformUserView(LoginStatusCheck, View):
    def post(self, request):
        global each_infor
        try:
            check_list = request.POST.getlist("msg_update") #先要拿到选中的对应的数据库中的数据
            print(check_list)
            if len(check_list):
                for each in check_list:
                    each_infor = Total.objects.get(id=int(each))
                    each_infor.stu_num=request.POST.get("english_name")
                    each_infor.sex=request.POST.get("mobile")
                    each_infor.major=request.POST.get("wechat")
                    each_infor.department=request.POST.get("qq")
                    each_infor.unit=request.POST.get("address_more")
                    each_infor.unit_address=request.POST.get("unit_address_more")
                    each_infor.education=request.POST.get("education_more")
                    each_infor.department=request.POST.get("year_more")
                    each_infor.save()
            print("......................................................................")
            context={
                "status":"success",
                "msg":"修改成功",
                "each_infor":each_infor,
            }
            render(request,'platform-management/user_platform_list.html',context=context)
            #return HttpResponse('{"status":"success", "msg":"修改成功！"}', content_type='application/json')
        except Exception as e:
            return HttpResponse('{"status":"failed", "msg":"修改失败！"}', content_type='application/json')

class PredictPlatformUserView(LoginStatusCheck, View):
    def get(self, request):
            return render(request,'users/Predict.html',locals())
    def post(self,request):
        zhuanye_1=request.POST.get("zhuanye_1")
        zhuanye_2=request.POST.get("zhuanye_2")
        year=request.POST.get("year")
        datas=go_search(zhuanye_1,zhuanye_2,year)
        context={
            'datas':datas,
        }
        print(datas)
        return render(request,'users/Predict.html',context=context)