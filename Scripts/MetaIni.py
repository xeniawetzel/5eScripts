# Made a GUI to start off my JSON files with the correct structure and meta data and  which I can fill in.

import tkinter as tk
from tkinter import ANCHOR, ttk
import sys
from turtle import width

input_window = tk.Tk()

meta_objects_sources = ["json", "abbreviation", "full", "url", "authors", "convertedBy", "version", "targetSchema"]
meta_objects_dateAdded = ["dateAdded*"]
meta_objects_dateLastModified = ["dateLastModified*"]
meta_objects = [meta_objects_sources,meta_objects_dateAdded,meta_objects_dateLastModified]

row_num = 0
lbl_list = []
ent_list = []
for list in meta_objects:
    for i in range(0,len(list)):
        lbl = ttk.Label(text=list[i])
        lbl_list.append(lbl)
        ent = ttk.Entry()
        ent_list.append(ent)
        lbl.grid(row=row_num, column=0,padx=5, pady=5)
        ent.grid(row=row_num, column=1,padx=5, pady=5)
        row_num=row_num+1

def print_entry():
    finished_file = open(r'.\jsonFile.json', 'w')
    finished_file.write('{')
    text = '"_meta": {\n\t\t"sources": [\n\t\t\t{\n\t\t\t\t"json": "'+ent_list[0].get()+'",\n\t\t\t\t"abbreviation": "'+ent_list[1].get()+'",\n\t\t\t\t"full": "'+ent_list[2].get()+'",\n\t\t\t\t"url": "'+ent_list[3].get()+'",\n\t\t\t\t"authors": [\n\t\t\t\t\t"Willy Abeel",\n\t\t\t\t\t"Leon Barillaro",\n\t\t\t\t\t"Gabe Hicks",\n\t\t\t\t\t"Sadie Lowry"\n\t\t\t\t],\n\t\t\t\t"convertedBy": [\n\t\t\t\t\t"'+ent_list[5].get()+'"\n\t\t\t\t],\n\t\t\t\t"version": "'+ent_list[6].get()+'",\n\t\t\t\t"targetSchema": "'+ent_list[7].get()+'"\n\t\t\t}\n\t\t],\n\t\t"dateAdded": '+ent_list[8].get()+',\n\t\t"dateLastModified": '+ent_list[9].get()+'\n}'
    finished_file.write(text)
    finished_file.write('}')


ok_button  = ttk.Button(text="OK", command=print_entry)
ok_button.grid(row=row_num+1,column=1,padx=5, pady=5)

tk.mainloop()
