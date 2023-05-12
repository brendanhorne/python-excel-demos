import os
import shutil
import pandas as pd
import numpy as np

dataframe = pd.read_excel('example.xlsx', dtype="str")
data = dataframe.to_numpy()
columns = dataframe.columns.to_list()
document_numbers = data[:,0]
document_titles = data[:,1]
document_paths = data[:,2]

# set the directory path to read
# dir_path = os.path.normpath(r"C:/Users/vid5zgs/OneDrive - Major Transport Infrastructure Authority/Interface Management/01. Interface Coordination/02. Disruption Management/03. Disruptions Dashboard\Admin\Brendan - Test")
# for testing use
dir_path = os.path.join(os.path.dirname(__file__),"folder")

# use the listdir() method to get a list of files in the directory

output_folder = "output"
new_directory = os.path.join(dir_path, output_folder)

# create new folder
try:
    os.mkdir(new_directory)
except FileExistsError:
    print('Folder already exists!')

# copy files
files = os.listdir(dir_path)
for file in files:
    if file == output_folder: 
        continue
    print(file)
    if file in document_paths:
        index = np.where(document_paths == file)[0]
        document_number = document_numbers[index][0]
        document_title = document_titles[index][0]
        original_file = os.path.join(dir_path, file)
        new_filename = rf"{document_number} - {document_title}.txt"
        new_file = os.path.join(new_directory, new_filename)
        try:
            shutil.copy(original_file, new_file)
        except FileExistsError:
            print('File already exists!')
        # os.unlink(original_file) # remove originals?
