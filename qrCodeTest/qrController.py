# -*- coding: utf-8 -*-
from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO

'''
django具体实现类
传输data 图片流 返回html页面
'''

def generate_qrcode(request, data):
    img = qrcode.make(data)

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response