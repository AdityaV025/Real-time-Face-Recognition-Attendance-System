"""Created by Enigma for Dexterix Hackathon 2018"""

#Importing all the modules
import xlwt
from datetime import datetime
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy
from pathlib import Path

'''style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('example.xls')
'''
def output(filename, sheet,num, name, present):
    my_file = Path('attendance_report/attendance_files/'+filename+str(datetime.now().date())+'.xls')
    if my_file.is_file():
        rb = open_workbook('attendance_report/attendance_files/'+filename+str(datetime.now().date())+'.xls')
        book = copy(rb)
        sh = book.get_sheet(0)
        # file exists
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    sh.write(0,0,datetime.now().date(),style1);


    col1_name = 'Name'
    col2_name = 'Present'


    sh.write(1,0,col1_name,style0)
    sh.write(1, 1, col2_name,style0)

    sh.write(num+1,0,name)
    sh.write(num+1, 1, present)
    
    fullname=filename+str(datetime.now().date())+'.xls'
    book.save('attendance_report/attendance_files/'+fullname)
    return fullname
