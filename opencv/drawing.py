import cv2
import numpy as np


def show_and_wait_esc(img: np.ndarray):
    """
    等待"ESC"键，关闭所有窗口
    :return: None
    """
    cv2.imshow("image", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # 创建一个512*512的黑色图片
    img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
    # 绘制蓝色线段
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), thickness=2)
    # 绘制绿色矩形
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), thickness=2)
    # 绘制椭圆
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    # 绘制圆形
    cv2.circle(img=img, center=(256, 256), radius=32, color=(0, 0, 255), thickness=-1)
    # 绘制多边形
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 255))
    # 绘制文字
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    # 显示图片
    show_and_wait_esc(img)
