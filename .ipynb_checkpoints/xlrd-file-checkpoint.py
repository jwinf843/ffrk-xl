import xlrd

file = ("Soul Breaks.xlsx")

workbook = xlrd.open_workbook(file) 

sheet = workbook.sheet_by_index(0) 

# print(sheet)
  
# For row 0 and column 0 
# print(sheet.cell_value(0, 2))

# // Print First Row
for column in range(sheet.ncols): 
    print(sheet.cell_value(0, column)) 
    
# // Print First Row as list
# sheet.cell_value(0, 0) 
row_1 = sheet.row_values(1)

print(row_1) 