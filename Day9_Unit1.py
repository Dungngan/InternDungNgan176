import magic
import os
import sys

def Check_Len_Command (Commands):
    if len(Commands) < 2:
        print('Not have path of folder/file')
        sys.exit()  

def Check_Type_File(Commands):  
    for i in range(len(Commands)):
        if i > 0:
            input= Commands[i]                               #file input
            if (os.path.isdir(input)):                  #Check directory is True
                print(input , ':\t', 'directory')
            elif (os.path.isfile(input)):               #Check file is True
                print(input,':\t',magic.from_file(input))
            else: 
                print(input , ':\t', 'Not exist')

if __name__ == '__main__':
    arg = sys.argv
    Check_Len_Command(arg) 
    #print(len(arg))
    Check_Type_File(arg)

# python .\Day_9_Unit_1_file.py 
# python .\Day_9_Unit_1_file.py khongtontai
# python .\Day_9_Unit_1_file.py .\day1_Mutations.py khongtontai 

# python .\Day_9_Unit_1_file.py .\find_the_flag\ 
# python .\Day_9_Unit_1_file.py .\day1_Mutations.py
# python .\Day_9_Unit_1_file.py .\day1_Mutations.py .\find_the_flag\