import openpyxl
import csv
import pandas as pd

excel = openpyxl.load_workbook("attendance.xlsx")
sheet = excel.active
col = csv.writer(
    open(
        "attendance.csv",
        "w",
        newline="",
    )
)
for r in sheet.rows:
    col.writerow([cell.value for cell in r])
