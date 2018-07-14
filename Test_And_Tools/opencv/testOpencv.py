import cv2

stitcher = cv2.createStitcher(False)
foo = cv2.imread("1.jpg")
bar = cv2.imread("2.jpg")
result = stitcher.stitch((foo,bar))

cv2.imwrite("result.jpg", result[1])


# import cv
#
#
#
# def compute_histogram(src, h_bins = 30, s_bins = 32):
#     #create images
#     hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
#     hplane = cv.CreateImage(cv.GetSize(src), 8, 1)
#     splane = cv.CreateImage(cv.GetSize(src), 8, 1)
#     vplane = cv.CreateImage(cv.GetSize(src), 8, 1)
#
#     planes = [hplane, splane]
#     cv.CvtColor(src, hsv, cv.CV_BGR2HSV)
#     cv.Split(hsv, hplane, splane, vplane, None)
#
#     #compute histogram  (why not use v_plane?)
#     hist = cv.CreateHist((h_bins, s_bins), cv.CV_HIST_ARRAY,
#             ranges = ((0, 180),(0, 255)), uniform = True)
#     cv.CalcHist(planes, hist)      #compute histogram
#     cv.NormalizeHist(hist, 1.0)    #normalize hist
#
#     return hist
#
# src1 = cv2.imread("1.jpg", cv.CV_LOAD_IMAGE_COLOR)
# src2 = cv.LoadImage("2.jpg", cv.CV_LOAD_IMAGE_COLOR)
# hist1= compute_histogram(src1)
# hist2= compute_histogram(src2)
# sc= cv.CompareHist(hist1, hist2, cv.CV_COMP_BHATTACHARYYA)
# print (sc)