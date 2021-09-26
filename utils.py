import os
import cv2

def generate_negative_file(folder_path):
    with open('neg.txt', 'w') as f:
        for filename in os.listdir(folder_path):
            f.write(folder_path + '\\' + filename + '\n')

def video2frames(video_path, output_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        cv2.imwrite(output_path + "\\frame%d.jpg" % count, image)  # save frame as JPEG file
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1
        print(count)
