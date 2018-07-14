import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import imutils

path1 = './room_a/'
path2 = './room_b/'
path3 = './room_c/'
path = [path1, path2, path3]
path = './room_1_45/'
# path=''
# print(p)
# stitcher = cv2.createStitcher(False)
# pic1 = cv2.imread(p + "1.jpg")
# pic2 = cv2.imread(p + "2.jpg")
# # result1 = stitcher.stitch((pic1, pic2))
# # pic3 = cv2.imread(p + "3.jpg")
# # pic4 = cv2.imread(p + "4.jpg")
# # result2 = stitcher.stitch((pic3, pic4))
# result = stitcher.stitch((result1,result2))
#
# cv2.imwrite(p + "result.jpg", result[1])


def test1():
    for p in path:
        for filename in os.listdir(p):
            # print(filename)

            img1 = cv2.imread('result.jpg',cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(p+filename,cv2.IMREAD_GRAYSCALE)

            hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
            hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

            sc = cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL)
            print(filename,':',sc)

def test2():

    stitcher = cv2.createStitcher(False)
    # ======================================================
    # pic1 = cv2.imread(path+"1.jpg")
    # pic2 = cv2.imread(path+"2.jpg")
    # result12=stitcher.stitch((pic1,pic2))
    # cv2.imshow("Result12", result12[1])
    #
    # pic3 = cv2.imread(path+"3.jpg")
    # pic4 = cv2.imread(path+"4.jpg")
    # result34=stitcher.stitch((pic3,pic4))
    # cv2.imshow("Result34", result34[1])
    #
    # pic5 = cv2.imread(path+"5.jpg")
    # pic6 = cv2.imread(path+"6.jpg")
    # result56=stitcher.stitch((pic5,pic6))
    # cv2.imshow("Result56", result56[1])
    #
    # pic7 = cv2.imread(path+"7.jpg")
    # pic8 = cv2.imread(path+"8.jpg")
    # result78=stitcher.stitch((pic7,pic8))
    # cv2.imshow("Result78", result78[1])

    # result1234=stitcher.stitch((result12[1],result34[1]))
    # result5678=stitcher.stitch((result56[1],result78[1]))
    # result = stitcher.stitch((result1234[1],result5678[1]))
    #======================================================
    # vis = np.concatenate((pic1, pic2, pic3, pic4), axis=1)
    pic1 = cv2.imread(path+"4.jpg")
    pic2 = cv2.imread(path+"5.jpg")
    # pic1 = imutils.resize(pic1, width=519, height=389)
    # pic2 = imutils.resize(pic2, width=519, height=389)
    result = stitcher.stitch((pic1, pic2))
    # cv2.imshow("pic1", pic1)
    # cv2.imshow("pic2", pic2)
    cv2.imshow("Result",result[1])
    cv2.imwrite(path+"45.jpg", result[1])
    cv2.waitKey(0)

if __name__ == '__main__':
    test2()