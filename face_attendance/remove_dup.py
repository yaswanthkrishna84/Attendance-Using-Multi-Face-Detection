import pandas as pd
from pyexcel.cookbook import merge_all_to_a_book
import glob

data = pd.read_csv("attendance.csv")
data.drop_duplicates(subset="name", keep="last", inplace=True)
df = data
df.to_csv("Final_attendance.csv")
merge_all_to_a_book(
    glob.glob("Final_attendance.csv"),
    "Final_attendance.xlsx",
)
