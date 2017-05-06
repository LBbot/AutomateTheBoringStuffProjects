import re
import glob

list_of_files = glob.glob('.\\textfilesforRegexsearchmultipletxts\\*.txt')

lb_regex = re.compile(r"(LB)")

for filez in list_of_files:
    my_file = open(filez, "r")
    filereader = my_file.read()
    print(lb_regex.findall(filereader))
    my_file.close()
    # ALTERNATE SHORTER WAY but no close?:
    # data_list = open(filez, "r").readlines()
    # print(lb_regex.findall(str(data_list)))
