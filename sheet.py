import xlrd


def get_sheet(file_name):
    wb = xlrd.open_workbook(file_name)
    sheets = wb.sheet_names()
    return wb.sheet_by_name(sheets[0])


def get_names(sheet=get_sheet("files.xlsx")):
    names = []
    for r in range(sheet.nrows):
        if r == 0:
            continue
        new_name = sheet.cell_value(r, 0).strip()
        names.append(new_name)
    return names


def search_name(name, names=get_names(), sheet=get_sheet("files.xlsx")):
    """
    get name info

    ---
    """
    reply = ""
    for n in range(len(names)):
        if names[n].lower() == name.lower():
            for c in range(sheet.ncols):
                reply = (str(sheet.cell_value(0, c)) +
                         " هي "+str(sheet.cell_value(n+1, c)))
            return reply

    reply = ("آسف ، اسمك ليس في القائمة")
    return reply
