######################################
# Django 模块
######################################
from django.db import models
from django.db.models import Q

######################################
# 系统模块
######################################
import datetime

######################################
# 自定义模块
######################################
from users.models import UserProfile


######################################
# 平台表
######################################
class PlatformInfo(models.Model):
    name = models.CharField(verbose_name='平台名称', max_length=30)
    logo = models.CharField(verbose_name='logo', max_length=100, blank=True, null=True)
    url = models.CharField(verbose_name='url', max_length=200)
    belong = models.PositiveSmallIntegerField(verbose_name='隶属', choices=((1, '公司平台'), (2, '运维平台'), (3, '其它平台')))
    is_public = models.BooleanField(verbose_name='公开', default=True)
    add_user = models.ForeignKey(UserProfile, verbose_name='添加人', related_name='pl_user', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = '平台表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


######################################
# 平台用户表
######################################
class PlatformUserInfo(models.Model):
    platform = models.ForeignKey(PlatformInfo, verbose_name='平台', related_name='pu_plat', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='平台名称', max_length=30, blank=True, null=True)
    password = models.CharField(verbose_name='平台密码', max_length=50, blank=True, null=True)
    user = models.ForeignKey(UserProfile, verbose_name='用户', related_name='pu_user', on_delete=models.CASCADE)
    update_user = models.ForeignKey(UserProfile, related_name='platform_update_user', verbose_name='修改人',on_delete=models.CASCADE)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '平台用户表'
        verbose_name_plural = verbose_name

#####################################
#添加主要信息数据表
#####################################
class Total(models.Model):
    stu_num = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    train_mode_num = models.IntegerField(blank=True, null=True)
    train_mode = models.CharField(max_length=255, blank=True, null=True)
    unit_code = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    unit_subordinate_code = models.IntegerField(blank=True, null=True)
    unit_subordinate = models.CharField(max_length=255, blank=True, null=True)
    unit_properties_code = models.IntegerField(blank=True, null=True)
    unit_properties = models.CharField(max_length=255, blank=True, null=True)
    unit_location_code = models.IntegerField(blank=True, null=True)
    unit_location = models.CharField(max_length=255, blank=True, null=True)
    unit_address = models.CharField(max_length=255, blank=True, null=True)
    unit_contact = models.CharField(max_length=255, blank=True, null=True)
    unit_telephone = models.CharField(max_length=255, blank=True, null=True)
    unit_postcode = models.IntegerField(blank=True, null=True)
    file_forward_address = models.CharField(max_length=255, blank=True, null=True)
    breach_contract1 = models.CharField(max_length=255, blank=True, null=True)
    breach_contract2 = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    direct_unit = models.CharField(max_length=255, blank=True, null=True)
    origin_location = models.CharField(max_length=255, blank=True, null=True)
    origin_location_code = models.IntegerField(blank=True, null=True)
    sign_flag = models.IntegerField(blank=True, null=True)
    remark1 = models.CharField(max_length=255, blank=True, null=True)
    remark2 = models.CharField(max_length=255, blank=True, null=True)
    remark3 = models.CharField(max_length=255, blank=True, null=True)
    remark4 = models.CharField(max_length=255, blank=True, null=True)
    graduate_direction_code = models.CharField(max_length=255, blank=True, null=True)
    graduate_direction = models.CharField(max_length=255, blank=True, null=True)
    is_one_employ = models.IntegerField(blank=True, null=True)
    is_province_employ = models.CharField(max_length=255, blank=True, null=True)
    is_teacher_employ = models.CharField(max_length=255, blank=True, null=True)
    report_certificate = models.IntegerField(blank=True, null=True)
    entrance_department = models.CharField(max_length=50, blank=True, null=True)
    entrance_major = models.CharField(max_length=50, blank=True, null=True)
    school_system = models.IntegerField(blank=True, null=True)
    double_select = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    province_net = models.IntegerField(blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    unit_type_code = models.IntegerField(blank=True, null=True)
    unit_type = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'total'

    def __str__(self):
        return '%s - %s' % (self.platform.name, self.username)



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Total(models.Model):
    stu_num = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    train_mode_num = models.IntegerField(blank=True, null=True)
    train_mode = models.CharField(max_length=255, blank=True, null=True)
    unit_code = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    unit_subordinate_code = models.IntegerField(blank=True, null=True)
    unit_subordinate = models.CharField(max_length=255, blank=True, null=True)
    unit_properties_code = models.IntegerField(blank=True, null=True)
    unit_properties = models.CharField(max_length=255, blank=True, null=True)
    unit_location_code = models.IntegerField(blank=True, null=True)
    unit_location = models.CharField(max_length=255, blank=True, null=True)
    unit_address = models.CharField(max_length=255, blank=True, null=True)
    unit_contact = models.CharField(max_length=255, blank=True, null=True)
    unit_telephone = models.CharField(max_length=255, blank=True, null=True)
    unit_postcode = models.IntegerField(blank=True, null=True)
    file_forward_address = models.CharField(max_length=255, blank=True, null=True)
    breach_contract1 = models.CharField(max_length=255, blank=True, null=True)
    breach_contract2 = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    direct_unit = models.CharField(max_length=255, blank=True, null=True)
    origin_location = models.CharField(max_length=255, blank=True, null=True)
    origin_location_code = models.IntegerField(blank=True, null=True)
    sign_flag = models.IntegerField(blank=True, null=True)
    remark1 = models.CharField(max_length=255, blank=True, null=True)
    remark2 = models.CharField(max_length=255, blank=True, null=True)
    remark3 = models.CharField(max_length=255, blank=True, null=True)
    remark4 = models.CharField(max_length=255, blank=True, null=True)
    graduate_direction_code = models.CharField(max_length=255, blank=True, null=True)
    graduate_direction = models.CharField(max_length=255, blank=True, null=True)
    is_one_employ = models.IntegerField(blank=True, null=True)
    is_province_employ = models.CharField(max_length=255, blank=True, null=True)
    is_teacher_employ = models.CharField(max_length=255, blank=True, null=True)
    report_certificate = models.IntegerField(blank=True, null=True)
    entrance_department = models.CharField(max_length=50, blank=True, null=True)
    entrance_major = models.CharField(max_length=50, blank=True, null=True)
    school_system = models.IntegerField(blank=True, null=True)
    double_select = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    province_net = models.IntegerField(blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    unit_type_code = models.IntegerField(blank=True, null=True)
    unit_type = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total'
