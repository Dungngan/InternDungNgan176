import re
import os.path
from traceback import print_tb
# FILE_NAME = []
# path = "/home/dungngan/Desktop/Project Python/find_the_flag"
# dirs = os.listdir(path)
# for file in os.walk(path):
#     print(file)
path = "find_the_flag"
for file_open in os.walk(path):
    for file in sorted(file_open[2]):
        fileopen = open(f'{path}/{file}','r')
        data = fileopen.read()       
        if re.search("This",data):
            print (data)