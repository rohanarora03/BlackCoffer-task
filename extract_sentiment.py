import xlrd

book = xlrd.open_workbook('LoughranMcDonald_MasterDictionary_2014.xlsx')
sheet = book.sheet_by_name('LoughranMcDonald_MasterDictiona')

# read header values into the list
keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
print(sheet.ncols)
print(keys)

neg_list = []
pos_list = []

for row_index in range(1, sheet.nrows):
    if sheet.cell(row_index, 7).value > 0:
        d = sheet.cell(row_index, 0).value
        neg_list.append(d)
    if sheet.cell(row_index, 8).value > 0:
        d = sheet.cell(row_index, 0).value
        pos_list.append(d)

# d = {sheet.cell(row_index, 0).value: sheet.cell(row_index, 7).value}

with open("pos.txt", "w+") as f:
    for i in pos_list:
        f.write(str(i)+ "\n")

with open("neg.txt", "w+") as g:
    for j in neg_list:
        g.write(str(j)+ "\n")