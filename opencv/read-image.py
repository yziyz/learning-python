import cv2

if __name__ == '__main__':
    # 以灰度模式读取图片"180px-Beethoven.jpg"
    img = cv2.imread('180px-Beethoven.jpg', cv2.IMREAD_GRAYSCALE)
    # 显示
    cv2.imshow('image', img)
    # 等待"ESC"键，关闭所有窗口
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
