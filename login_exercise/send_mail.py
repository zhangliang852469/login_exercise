#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if __name__ == '__main__':
    subject, from_email, to = '来自张亮的测试邮件', 'zhang852469@sina.com', 'mhui0913@sina.com'
    text_content = '张亮测试python的邮件模块'
    html_content = '<p>欢迎访问<a href = "http://www.bossapp.cn" target=blank>www.bossapp.cn</a>这里是BOSS商学的官网</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# if __name__ == '__main__':
#
#     send_mail(
#         '来自www.liujiangblog.com的测试邮件',
#         '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
#         'zhang852469@sina.com',
#         ['710567585@qq.com'],
#     )