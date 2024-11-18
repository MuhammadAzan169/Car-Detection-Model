import os
def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write('negative' + filename + '\n')
# E:\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=positive/
# E:\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 200 -vec pos.vec
# E:\opencv\build\x64\vc15\bin\opencv_createsamples -vec pos.vec -w 24 -h 24 -show
# E:\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data model/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 200 -numNeg 100 -numStages 10