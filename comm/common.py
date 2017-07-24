import os
import readconfig
from xlrd import open_workbook
import xlrd
prodir=readconfig.prodir
localPath=os.path.join(prodir,"testCase")




def get_xls(xls_name,sheet_name):

    cls=[]
    xls_path=os.path.join(localPath,"case",xls_name)
    file = open_workbook(xls_path)
    sheet = file.sheet_by_name(sheet_name)


    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case':
            cls.append(sheet.row_values(i))
    return cls



