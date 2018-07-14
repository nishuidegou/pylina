import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from panorama import Stitcher
import imutils

path1 = './room_a/'
path2 = './room_b/'
path3 = './room_c/'
path = [path1, path2, path3]


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


def test_hist():
    for p in path:
        for filename in os.listdir(p):
            # print(filename)

            img1 = cv2.imread('result.jpg',cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(p+filename,cv2.IMREAD_GRAYSCALE)

            hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
            hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

            sc = cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL)
            print(filename,':',sc)

def test_concatenate():

    stitcher = cv2.createStitcher(False)
    pic1 = cv2.imread("./room_c/1.jpg")
    pic2 = cv2.imread("./room_c/2.jpg")
    pic3 = cv2.imread("./room_c/3.jpg")
    pic4 = cv2.imread("./room_c/4.jpg")
    # result = stitcher.stitch((pic1, pic2))
    vis = np.concatenate((pic1, pic2, pic3, pic4), axis=1)
    cv2.imwrite("./room_c/result.jpg", vis)

def test_keypoint1():
    imgA = cv2.imread("./room_a/1.jpg")
    imgB = cv2.imread("./room_1_45/1.jpg")

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    (kps, descs) = sift.detectAndCompute(gray, None)
    print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
    surf = cv2.xfeatures2d.SURF_create()
    (kps, descs) = surf.detectAndCompute(gray, None)
    print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))

def test_keypoint2():
    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    imageA = cv2.imread('./room_c/2.jpg')
    imageB = cv2.imread('./room_2_45/2.jpg')
    imageA = imutils.resize(imageA, width=400)
    imageB = imutils.resize(imageB, width=400)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    # show the images
    cv2.imshow("Image A", imageA)
    cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    # cv2.imwrite("1234.jpg", result)
    cv2.waitKey(0)

def test_edge():

    img = cv2.imread('./room_1_45/1.jpg', 0)
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def test_corner():


    img = cv2.imread('./room_1_45/1.jpg')
    # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img3 = img
    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create()

    # find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = cv2.drawKeypoints(img, kp, img3, color=(255, 0, 0),)

    # Print all default params
    # print("Threshold: ", fast.getInt('threshold'))
    # print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
    # print("neighborhood: ", fast.getInt('type'))
    # print("Total Keypoints with nonmaxSuppression: ", len(kp))

    cv2.imwrite('fast_true.png', img2)

    # Disable nonmaxSuppression
    # fast.setBool('nonmaxSuppression', 0)
    # kp = fast.detect(img, None)

    print("Total Keypoints without nonmaxSuppression: ", len(kp))

    # img3 = cv2.drawKeypoints(img, kp, img3, color=(255, 0, 0))
    #
    # cv2.imwrite('fast_false.png', img3)

if __name__ == '__main__':
    test_corner()