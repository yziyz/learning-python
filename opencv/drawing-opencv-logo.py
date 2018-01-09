"""
绘制OpenCV的logo (https://opencv.org/assets/theme/logo.png)

参考https://gist.github.com/heliy/9e8d026ee279f9412d3d
"""

import math

import cv2
import numpy as np

from opencv.drawing import show_and_wait_esc

if __name__ == '__main__':
    r1 = 70
    r2 = 30

    angle = 60

    d = 170
    h = int(d / 2 * math.sqrt(3))

    # 三元组(B, G, R)
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    white = (255, 255, 255)

    # 二元组
    dot_red = (256, 128)
    dot_green = (dot_red[0] - int(d / 2), dot_red[1] + h)
    dot_blue = (dot_red[0] + int(d / 2), dot_red[1] + h)

    img = np.zeros((512, 512, 3), np.uint8)
    # 填充白色
    img.fill(255)

    cv2.circle(img, dot_red, r1, red, -1)
    cv2.circle(img, dot_green, r1, green, -1)
    cv2.circle(img, dot_blue, r1, blue, -1)

    cv2.circle(img, dot_red, r2, white, -1)
    cv2.circle(img, dot_green, r2, white, -1)
    cv2.circle(img, dot_blue, r2, white, -1)

    cv2.ellipse(img, dot_red, (r1, r1), angle, 0, angle, white, -1)
    cv2.ellipse(img, dot_green, (r1, r1), 360 - angle, 0, angle, white, -1)
    cv2.ellipse(img, dot_blue, (r1, r1), 360 - 2 * angle, angle, 0, white, -1)

    show_and_wait_esc(img)
