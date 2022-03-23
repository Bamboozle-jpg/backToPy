import cv2
vidcap = cv2.VideoCapture('DoYouRemember.mp4')
success,image = vidcap.read()
count = 0
howMany = 1
while success:
    if (howMany%5 == 0):
        cv2.imwrite("vidImagesTwo/frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print('Read a new frame: ', success, howMany)
        count += 1
        howMany = 0
    else :
        success,image = vidcap.read()
        count += 1
    howMany += 1
