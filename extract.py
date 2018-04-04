import xlrd, urllib.request, webbrowser

book = xlrd.open_workbook('cik_list.xlsx')
sheet = book.sheet_by_name('cik_list_ajay')

# read header values into the list
keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
print(sheet.ncols)
print(keys)

dict_list = []
for row_index in range(1, sheet.nrows):
    d = {keys[col_index]: sheet.cell(row_index, col_index).value
         for col_index in range(sheet.ncols)}
    dict_list.append(d)

print (dict_list)

links = []
for i in dict_list:
    for j in i:
        if j == "SECFNAME":
            links.append("https://www.sec.gov/Archives/"+i[j])

print(links)

file = []
data = urllib.request.urlopen('https://www.sec.gov/Archives/edgar/data/3662/0000950170-98-000413.txt')
for line in data:
    file.append(line)
    # if line == "Management's Discussion and Analysis":
    #     print(line)

# f = open("data.txt", "w+")
# f.write(str(file) + "\n")
# f.close()