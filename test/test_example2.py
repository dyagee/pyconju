from pyconju.csv import Csv as merger
import os

#assuming the files are in the same directory as test_example2.py
path = os.getcwd()
#print(path)

fileList = ["file1.csv","file2.csv"]
merger.merge_csv(fileList,path)