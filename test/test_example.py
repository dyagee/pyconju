from pyconju.xls import Excel as merger
import os

#assuming the files are in the same directory as test_example.py
path = os.getcwd()
print(path)

fileList = ["file1.xls","file2.xls"]
merger.merge_xls(fileList,path) 