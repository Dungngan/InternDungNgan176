import os
import sys

def Check_Len_Command (Commands):
    if len(Commands) < 2:
        print('Not have path of folder/file')
        sys.exit()  

def List_File_In_Folder (input_path):
    print(input_path,':')
    for file in os.listdir(input_path):
        print(file)   

def ls_File_Folder(Commands):                          #list files in folder
    for i in range(len(Commands)):
        if i > 0:
            input= Commands[i]                               #file iput
            if (os.path.isdir(input)):                  #Check directory is True
                List_File_In_Folder(input)
            elif (os.path.isfile(input)):               #Check file is True
                print(input,'is a file ')
            else: 
                print(input , ':\t', 'Not exist')

if __name__ == '__main__':
    arg = sys.argv
    Check_Len_Command(arg)
    ls_File_Folder(arg)

# python .\Day_9_Unit_2_cut.py  
# python .\Day_9_Unit_2_cut.py khongcofile
# python .\Day_9_Unit_2_cut.py khongcofile .\find_the_flag\

#python .\Day_9_Unit_2_cut.py .\find_the_flag\
#python .\Day_9_Unit_2_cut.py .\cat.jpg 
#python .\Day_9_Unit_2_cut.py .\find_the_flag\ .\cat.jpg 