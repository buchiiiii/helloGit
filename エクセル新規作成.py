import openpyxl as px
book = px.Workbook()
book.save('sample-test.xlsx')
print('> エクセル新規作成')