import os
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = ' '.join(sys.argv[1:])
        # print(directory)
    else:
        directory = os.getcwd()


    os.chdir(directory)
    all_list = os.listdir()
    # print(os.getcwd())
    # print(all_list)

    file_name = input("Enter name of file: ")
    r = re.compile("%s\d*.\w+" % file_name)
    file_list = list(filter(r.match, all_list))
    #print(file_list)
    for file in file_list:
        a = re.compile("%s" % file_name)
        new_name = a.sub('myproject', file)
        #print(new_name)
        os.rename(file, new_name)
    #print(all_list)
#print(directory)