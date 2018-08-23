from django.db import models

# Create your models here.

"""
用户表User，在用户表里需要保存下面的信息：

用户名
密码
邮箱地址
性别
创建时间
"""

class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField('性别', max_length=32, choices=gender, default='男')
    c_time = models.DateField(auto_now_add=True)
    has_confirmed = models.BooleanField('邮件确认', default=False)  # 邮件确认，

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

# 邮件确认（确认码）
class ConfirmString(models.Model):
    code = models.CharField('注册码', max_length=256)
    user = models.OneToOneField('User', verbose_name='用户', on_delete=models.CASCADE)
    c_time = models.DateTimeField('确认创建时间', auto_now_add=True)

    def __str__(self):
        return self.user.name + ': ' + self.code
    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'
