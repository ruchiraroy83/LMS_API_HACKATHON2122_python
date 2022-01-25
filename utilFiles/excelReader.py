import requests
from behave import *
import pandas as pd

def excelReader(filepath,sheetName,Rownumber):
    import xlrd

    # To open Workbook
    wb = xlrd.open_workbook(filepath)
    sheet = wb.sheet_by_name(sheetName)

    # to get the no of coulumns
    for column in range(sheet.ncols):
        thecell = sheet.cell(Rownumber, column)


def excelWriter(filepath,sheetName):
    import xlrd
    book = xlrd.open_workbook(filepath, formatting_info=True)
    sheet = book.sheet_by_name(sheetName)
