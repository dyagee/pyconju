# PyConju 

A python package for merging multiple files into a single file. File types supported include: .xlsx, .xls, and .csv.

`PDF` support coming soon!


## Installation on Windows
---
### 1. Create a Project folder
```
mkdir project-folder
cd project-folder
```
### 2. Create a virtual environment
```
python -m venv venv
```
### 3. Activate the virtual environment
```
./venv/Scripts/activate
```
### 4. Install package from PyPi
```
pip install pyconju
``` 

### 5. Usage / Examples

### Example 1
```python
from pyconju.xlsx import Excelx
```
```python
# Initialize object
merger = Excelx()
path = "path/to/files/to/merge"
fileList = ["file1.xlsx","file2.xlsx","file3.xlsx"]
merger.merge_xlsx(fileList,path)
```

###  Example 2
```python
from pyconju.xls import Excel
```
```python
# Initialize object
merger = Excel()
path = "path/to/files/to/merge"
fileList = ["file1.xls","file2.xls","file3.xls"]
merger.merge_xls(fileList,path)
```

###  Example 3
```python
from pyconju.csv import Csv
```
```python
# Initialize object
merger = Csv()
path = "path/to/files/to/merge"
fileList = ["file1.xlsx","file2.xlsx","file3.xlsx"]
merger.merge_csv(fileList,path)
```
## Contributing
You are welcome to contribute to the repo as you like

## Authors and acknowledgment
Agee Aondo

Email: ageeaondo45@gmail.com

Website: https://linktr.ee/dyagee

## License
See LICENSE file