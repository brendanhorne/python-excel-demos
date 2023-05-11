from tkinter import filedialog
import daff
import pandas as pd
from tablepyxl import tablepyxl
import re

old_file = filedialog.askopenfilename()
new_file = filedialog.askopenfilename()

df_old = pd.read_excel(old_file, "Sheet1")
df_new = pd.read_excel(new_file, "Sheet1")
df_old = df_old.fillna(value="")
df_new = df_new.fillna(value="")
old_headers = df_old.columns.to_list()
new_headers = df_new.columns.to_list()
old_data = df_old.values.tolist()
new_data = df_new.values.tolist()
old_data.insert(0,old_headers)
new_data.insert(0,new_headers)
table1 = daff.PythonTableView(old_data)
table2 = daff.PythonTableView(new_data)
flags = daff.CompareFlags()
# flags.columns_to_ignore = []
flags.show_unchanged = True
flags.always_show_order = True
flags.never_show_order = False
# flags.addPrimaryKey("Unique ID")
compare_table = daff.Coopy.compareTables(table1, table2, flags)
alignment = compare_table.align()
highlighter = daff.TableDiff(alignment, flags)

data_diff = []
table_diff = daff.PythonTableView(data_diff)
highlighter.hilite(table_diff)

diff2html = daff.DiffRender()
diff2html.render(table_diff)

table_diff_html = diff2html.html()
table_diff_html = re.sub(r"class=\"add\"", "style=\"background-color: #7fff7f;\"", table_diff_html)
table_diff_html = re.sub(r"class=\"remove\"", "style=\"background-color: #ff7f7f;\"", table_diff_html)
table_diff_html = re.sub(r"(?<=(th|td) )class=\"modify\"", "style=\"background-color: #7f7fff;\"", table_diff_html)
table_diff_html = re.sub(r"(?<=(th|td) )class=\"conflict\"", "style=\"background-color: #f00;\"", table_diff_html)
table_diff_html = re.sub(r"class=\"spec\"", "style=\"background-color: #aaa;\"", table_diff_html)
table_diff_html = re.sub(r"class=\"move\"", "style=\"background-color: #ffa;\"", table_diff_html)
table_diff_html = re.sub(r"class=\"null\"", "style=\"color: #888;\"", table_diff_html)
table_diff_html = re.sub(r"class=\"gap\"", "style=\"color: #888;\"", table_diff_html)

save_file = filedialog.asksaveasfilename()
tablepyxl.document_to_xl(table_diff_html, save_file)