import cv2

vidcap = cv2.VideoCapture('.mp4') # insert string with video's file name

success,image = vidcap.read()

count = 0

while success:
  cv2.imwrite("frames/%d.jpg" % count, image)     # save frame inside the folder "frames" as .jpg file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1