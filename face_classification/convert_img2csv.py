# coding: utf-8
from PIL import Image
import numpy
import os
import csv

root = 'C:/Users/Administrator/PycharmProjects/face_emotion_recog/emotion/fer2013'
FileList = os.listdir(root)
LEN = len(FileList)
Mat = []

#csv.writer(open('fer2013.csv', 'w+'), lineterminator='\n').writerows(['emotion', 'pixels', 'Usage'])
csvfile = open('fer2013.csv', 'w')
writer = csv.writer(csvfile,lineterminator='\n', dialect = ("excel"))
header = ['emotion', 'pixels', 'Usage']
writer.writerow(header)


def img2vector(filename):
    img = Image.open(filename)
    img_ndarray = numpy.asarray(img, dtype='int')
    returnVect = numpy.ndarray.flatten(img_ndarray)
    returnVect = returnVect.tolist()
    return returnVect

for i in range(LEN):
    if i==0:
        FileName = 'train'
    else:
        FileName = 'test'

    fileName = (root + '/' + FileName)
    fileList = os.listdir(fileName)
    LEN_ = len(fileList)

    for j in range(LEN_):
        fileName_ = (fileName + '/' + fileList[j])
        fileList_ = os.listdir(fileName_)
        LEN__ = len(fileList_)

        print(FileName,fileList[j])
        for k in range(LEN__):
            imgName = (fileName_ + '/' + fileList_[k])
            img = Image.open(imgName).convert('L')
            img_ndarray = numpy.asarray(img, dtype='int')
            Vect = numpy.ndarray.flatten(img_ndarray)
            vector_str = ' '.join(str(num) for num in Vect)
            #vect_str = ' '.join(Vect)
            #Vect = Vect.tolist()
            # #data = [fileList[j],Vect,FileList[i]]
            # Mat.append(fileList[j])
            # Mat.append(str(Vect))
            # Mat.append(FileList[i])
            #writer = csv.writer(csvfile,dialect = ("excel"))
            if FileName=='test':
                lastName = 'PublicTest'
            else:
                lastName = 'Training'
            data = [fileList[j], vector_str, lastName]
            writer.writerow(data)

print("write over...")