import json
import csv
import os
import sys
import magic

def json_to_csv (file_path,csv_name) :
    #open the JSON file in reading mode and open the CSV file in write mode
    try:
        json_file=open(file_path,'r')
        csv_file=open(csv_name,'w')
        json_data_to_python_dict=json.load(json_file)
        write=csv.writer(csv_file)
        #use keys() and values() to write the dictionary keys 
        #and dictionary values in different rows into the CSV file respectively
        write.writerow(json_data_to_python_dict.keys())
        write.writerow(json_data_to_python_dict.values())
        json_file.close()
        csv_file.close()
    except Exception as e:
        print(e)

def csv_to_json(csv_file_path, json_file_path):
    try:
        jsondict = {}  
        with open(csv_file_path) as csvfile:  
            csv_data = csv.DictReader(csvfile)#Converting the csv data into dictionary
            jsondict["data"]=[]  #Declare a list in jsondict for a key
            for rows in csv_data:  
                print(rows)#Just for reference
                jsondict["data"].append(rows)  #Appending all the csv rows
        with open(json_file_path, 'w') as jsonfile:  
            #Dumping the data into jsonfile.json
            jsonfile.write(json.dumps(jsondict, indent = 4))  #indent is used for pretty printing
    except Exception as e:
        print(e)

def Check_Len_Command (Commands):
    if len(Commands) < 2:
        print('Not have path of folder/file')
        sys.exit() 
    elif  len(Commands)> 2:
        print('Too many arguments')
        sys.exit()     

def Check_Type_File(Commands):  
    for i in range(len(Commands)):
        if i > 0:
            input= Commands[i]                               #file iput
            if (os.path.isdir(input)):                  #Check directory is True
                print(input , ':\t', 'directory')
            elif (os.path.isfile(input)):               #Check file is True
                print(input,':\t',magic.from_file(input))
                sys.exit()
            else: 
                print(input , ':\t', 'Not exist')
                sys.exit()
if __name__ =='__main__' : 
    arg = sys.argv
    Check_Len_Command(arg)
    path =arg[1]
    
    # path =r"C:\3 codeearn\basic python\lab_FSOFT\LAB_FSOFT_PYTHON_TRAINNING\find_the_json_csv"
    # Change the directory
    os.chdir(path)
    for file in os.listdir():
        if file.endswith(".json"):
            new_file = file.split('.')[0]+'.csv'
            json_to_csv(file ,new_file)
            os.remove(file)   
        elif file.endswith(".csv"):
            newFile = file.split('.')[0]+'.json'
            csv_to_json(file ,newFile)
            os.remove(file)

            

        
