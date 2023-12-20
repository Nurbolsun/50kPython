from openpyxl import load_workbook

excel = load_workbook('report.xlsx')
page = excel["Sheet"]
print(page)

print(page["B1"].value)

page["A5"] = 'Среднее'
s = page["B2"].value + page["B3"].value + page["B4"].value
page["B5"] = s
excel.save('report.xlsx')

print(page["B5"].value)