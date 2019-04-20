# _*_ encoding:utf-8 _*_

from users.models import EmailVerifyRecord
from Mxonline.settings import EMAIL_FROM

from random import Random
from django.core.mail import send_mail


def random_str(randomlength=8):
    str =''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMnNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == "register":
        email_tltle = "颖风教育网注册激活链接"
        email_boby = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_tltle, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_tltle = "颖风教育网密码重置链接"
        email_boby = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_tltle, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_tltle = "颖风教育网邮箱修改验证码"
        email_boby = "你的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_tltle, email_boby, EMAIL_FROM, [email])
        if send_status:
            pass
