import cv2

if __name__ == '__main__':
    img = cv2.imread('180px-Beethoven.jpg', 0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
