import pandas as pd
import os
import random as r

class Excel:
    def merge_xls(fileList:list, path:str):
        excel_files =[]

        for fil in fileList:
            if fil[-3:] == 'xls':
                excel_files.append(fil)
        
        data =[]
        if len(excel_files) !=0:
            for file in excel_files:
                dt = pd.read_excel(os.path.join(path,file),engine='xlrd',header=0,index_col=None)
                data.append(dt)
            if len(data) != 0:
                df = pd.concat(data)
                #create a dataFrame
                dframe =pd.DataFrame(df)
                dframe = dframe.iloc[:,1:]
                hashed = r.randint(1000,9999)
                hashed = str(hashed)
                merged_file = f"merged_{hashed}.xlsx"
                dframe.to_excel(os.path.join(path,merged_file ),engine="openpyxl",index=False)
