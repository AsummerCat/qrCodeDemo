# -*- coding: utf-8 -*-

'''
导入包
conda install -c conda-forge qrcode
python图像处理包
conda install -c conda-forge pillow

'''
import qrcode
from PIL import Image, ImageDraw


def showQrCode():
    img = qrcode.make('http://www.linjingc.top')
    # img <qrcode.image.pil.PilImage object at 0x1044ed9d0>

    with open('test.png', 'wb') as f:
        img.save(f)


if __name__ == '__main__':
    showQrCode()
