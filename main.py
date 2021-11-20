import csv
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Levenshtein import ratio

i = 0
num_edit = 0
FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\Закупки.csv'
FILENAME_S = r'C:\Users\Виктор\PycharmProjects\purchases\ТМЦ.csv'
FILENAME_M = 'Остатки ТМЦ.csv'

def edit_item(event):
    num_edit = int(tree.selection()[0])
    edit_text.set(data[num_edit][2])
    num.set(data[num_edit][3])
    note.set(data[num_edit][4])

def set_item(event):
    num_edit = int(tree.selection()[0])
    data[num_edit][2] = edit_text.get()
    data[num_edit][3] = num.get()
    data[num_edit][4] = note.get()
    if data[num_edit][0] == '':
        prefix = ''
    else:
        prefix = ' шт.'
    tree.item(num_edit, text = data[num_edit][2]+'\t'+data[num_edit][3]+prefix+'\t'+data[num_edit][4])

def save():
    with open(FILENAME, "w", newline="", encoding='utf-8') as file1:
        writer1 = csv.writer(file1)
        writer1.writerows(data)

def insert():
    num_edit = int(tree.selection()[0])
    global i
    i += 1
    p = tree.parent(num_edit)
    iid = tree.insert(p, index=i, iid=i, text='new')
    data.append([p, i, 'new', 1, ''])
    tree.selection_set(iid)

def myhelp():
    pass

def juxtapose():
    with open(FILENAME_M, 'r', encoding='cp1251') as file:
        material = []
        reader = csv.reader(file, delimiter = ";")
        for row in reader:
            material.append(row)
    for i, m in enumerate(material):
        equa = []
        for s in item_source:
            equa.append(ratio(s, m[3]))
        ma = max(equa)
        if ma >0.5:
            material[i].append(item_source[equa.index(ma)])
        else:
            material[i].append('')
    jux = Tk()
    jux.title('Сопоставление материалов из базы и остатков ТМЦ')
    jux.geometry('1000x500+20+20')
    table = ttk.Treeview(jux, show='headings', columns=("#1", "#2"))
    table.heading("#1", text="Остатки ТМЦ")
    table.heading("#2", text="Материал из базы")
    ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=table.yview)
    table.configure(yscroll=ysb.set)
    for m in material:
        table.insert('', tk.END, values=(m[3], m[13]))
    table.pack(expand=True, fill=BOTH, side=LEFT)
    ysb.pack(expand=True, fill=Y, side=RIGHT)
    jux.mainloop()

root = Tk()
root.title("Управление закупками")
root.geometry("1300x300+0+0")

main_menu = Menu(root)
menu_file = Menu(main_menu, tearoff = 0)
menu_file.add_command(label = "Сохранить", command = save)
menu_file.add_command(label = "Сопоставить с остатками", command = juxtapose)
main_menu.add_cascade(label="Файл", menu = menu_file)
menu_edit = Menu(main_menu, tearoff = 0)
menu_edit.add_command(label = "Вставить", command = insert)
main_menu.add_cascade(label="Правка", menu = menu_edit)
main_menu.add_command(label="Помощь", command = myhelp)
root.config(menu=main_menu)

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# create a treeview
tree = ttk.Treeview(root)
tree.heading('#0', text='Группы проектов', anchor='w')

data = []

with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

for item in data:
    if item[0] == '':
        prefix = ''
    else:
        prefix = ' шт.'
    tree.insert(item[0], item[1],iid=item[1],text=item[2]+'\t'+item[3]+prefix+'\t'+item[4])
i = int(item[1])

tree.bind("<<TreeviewSelect>>", edit_item)
edit_text = ttk.Combobox(root)
edit_text.place(relx=0, y=1, relwidth=0.5)
num=StringVar()
edit_num = Spinbox(textvariable=num, from_ = 1.0 , to = 100000.0, increment = 1.0)
edit_num.place(relx=0.5, y=1, relwidth=0.1)
note=StringVar()
edit_note = Entry(textvariable=note)
edit_note.place(relx=0.6, y=1, relwidth=0.4)
tree.place(x=0, y=22, relheight=1, relwidth=1)
edit_text.bind('<Return>',set_item)
edit_num.bind('<Return>',set_item)
edit_note.bind('<Return>',set_item)

item_source = []
with open(FILENAME_S, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        item_source.append(row[0])
edit_text['values'] = item_source

root.mainloop()
