import pandas as pd
import os
import random as r

class Csv :
    def merge_csv(fileList:list, path:str):
        csv_files =[]

        for fil in fileList:
            if fil[-3:] == 'csv':
                csv_files.append(fil)
        
        data =[]
        if len(csv_files) !=0:
            for file in csv_files:
                dt = pd.read_csv(os.path.join(path,file),header=0,index_col=None)
                data.append(dt)
            if len(data) != 0:
                df = pd.concat(data)
                #create a dataFrame
                dframe =pd.DataFrame(df)
                dframe = dframe.iloc[:,2:]
                hashed = r.randint(1000,9999)
                hashed = str(hashed)
                merged_file = f"merged_{hashed}.xlsx"
                dframe.to_csv(os.path.join(path,merged_file ),index=False)
