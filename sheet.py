import xlrd



def get_names_from_sheet(file_name="./downloads/file.xlsx"):
    wb = xlrd.open_workbook(file_name)
    sheets = wb.sheet_names()
    sheet = wb.sheet_by_name(sheets[0])
    names = []
    for r in range(sheet.nrows):
        if r == 0:
            continue
        new_name = sheet.cell_value(r, 0).strip()
        names.append(new_name)
    return {
        'names':names,
        'sheet':sheet,
    }

def search_name(name, names, sheet,error_reply):
    """
    get name info
    ---
    """
    reply = ""
    for n in range(len(names)):
        if names[n].lower() == name.lower():
            for c in range(sheet.ncols):
                reply = (str(sheet.cell_value(0, c)) +" : "+str(sheet.cell_value(n+1, c)))
            return reply

    reply = error_reply
    return reply
