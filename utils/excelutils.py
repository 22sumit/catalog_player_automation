import xlrd

def read_excel(path,sh_name,row,col):
    book=xlrd.open_workbook(path)
    sheet=book.sheet_by_name(sh_name)
    return sheet.cell_value(row, col)