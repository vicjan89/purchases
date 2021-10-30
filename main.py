import csv
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

i = 0
num_edit = 0

def edit_item(event):
    num_edit = int(tree.selection()[0])
    text.set(data[num_edit][2])
    num.set(data[num_edit][3])
    note.set(data[num_edit][4])

def set_item(event):
    num_edit = int(tree.selection()[0])
    data[num_edit][2] = text.get()
    data[num_edit][3] = num.get()
    data[num_edit][4] = note.get()
    if data[0] == '':
        prefix = ''
    else:
        prefix = ' шт.'
    tree.item(num_edit, text = data[num_edit][2]+'\t'+data[num_edit][3]+prefix+'\t'+data[num_edit][4])

def save():
    FILENAME1 = r'C:\Users\Виктор\PycharmProjects\purchases\Закупки.csv'
    with open(FILENAME1, "w", newline="", encoding='utf-8') as file1:
        writer1 = csv.writer(file1)
        writer1.writerows(data)

def edit():
    pass

def myhelp():
    pass

root = Tk()
root.title("Управление закупками")
root.geometry("1300x700+0+0")

main_menu = Menu(root)
menu_file = Menu(main_menu, tearoff = 0)
menu_file.add_command(label = "Сохранить Ctrl+S", command = save)
main_menu.add_cascade(label="Файл", menu = menu_file)
main_menu.add_command(label="Правка")
main_menu.add_command(label="Помощь")
root.config(menu=main_menu)

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# create a treeview
tree = ttk.Treeview(root)
tree.heading('#0', text='Группы проектов', anchor='w')

FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\Спецификации.csv'
data = []
i1 = 0
i2 = 0
i3 = 0

with open(FILENAME, "r", newline="", encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    for row1 in reader1:
        data.append(['', i, row1[0], row1[1], row1[2]])
        i1 = i
        i += 1
        with open(row1[0]+'.csv', 'r', newline="", encoding='utf-8') as file2:
            reader2 = csv.reader(file2)
            for row2 in reader2:
                data.append([i1,i, row2[0],row2[1], row2[2]])
                i2 = i
                i += 1
                with open(row2[0]+'.csv', 'r', newline="", encoding='utf-8') as file3:
                    reader3 = csv.reader(file3)
                    for row3 in reader3:
                        data.append([i2, i, row3[0], row3[1], row3[2]])
                        i += 1
for item in data:
    if item[0] == '':
        prefix = ''
    else:
        prefix = ' шт.'
    tree.insert(item[0], item[1],iid=item[1],text=item[2]+'\t'+item[3]+prefix+'\t'+item[4])

tree.bind("<<TreeviewSelect>>", edit_item)
text=StringVar()
edit_text = Entry(textvariable=text)
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
root.mainloop()





def project():
    root.title("Формирование спецификации проекта")

    item_source.delete(0, END)
    item_project.delete(0, END)
    num.delete(0, END)
    note.delete(0, END)
    FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\ТМЦ.csv'
    with open(FILENAME, "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            item_source.insert(END, row[0])

    scrollbar.pack(side=RIGHT, fill=Y)

    item_source.bind('<space>', add)
    item_source.bind('+', change_num_item_project)
    item_source.bind('-', change_num_item_project)
    item_source.bind('*', change_num_item_project)
    item_source.bind('/', change_num_item_project)
    item_project.bind('<Delete>', del_item_project)
    item_project.bind('+', change_num_item_project)
    item_project.bind('-', change_num_item_project)
    item_project.bind('*', change_num_item_project)
    item_project.bind('/', change_num_item_project)
    root.bind('o', open_file)
    root.bind('s', save_file)

    item_source.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_source.yview)
    item_project.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_project.yview)
    num.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=num.yview)
    note.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=note.yview)


def group_projects():
    directory = r'C:\Users\Виктор\PycharmProjects\purchases'
    files = os.listdir(directory)
    for f in files:
        if f[-4:] == '.csv' and f[-6:-4] != 'gp' and f[0:3] != 'ТМЦ':
            f = f[0:-4]
            item_source.insert(END, f)

    scrollbar.pack(side=RIGHT, fill=Y)

    item_source.bind('<space>', add)
    item_source.bind('+', change_num_item_project)
    item_source.bind('-', change_num_item_project)
    item_source.bind('*', change_num_item_project)
    item_source.bind('/', change_num_item_project)
    item_project.bind('<Delete>', del_item_project)
    item_project.bind('+', change_num_item_project)
    item_project.bind('-', change_num_item_project)
    item_project.bind('*', change_num_item_project)
    item_project.bind('/', change_num_item_project)
    root.bind('o', open_file)
    root.bind('s', save_group)

    item_source.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_source.yview)
    item_project.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_project.yview)
    num.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=num.yview)
    note.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=note.yview)


def view_sum(event):
    file_name = item_source.curselection()
    progects = []
    items = []
    sum_items = []
    with open(item_source.get(file_name[0]) + 'gp.csv', "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            progects.append(row)
    with open('ТМЦ.csv', 'r', newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row[0])
    for prg in progects:
        with open(prg[0] + '.csv', 'r', newline="", encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] in sum_items:
                    i = sum_items.index(row[0])
                    print(i)
                    sum_items[i][1] += 1
                else:
                    sum_items.append(row)
    for s in sum_items:
        print(s)
        item_project.insert(END, s[0])
        num.insert(END, s[1])


def sum_group_projects():
    root.title("Сводная спецификация группы проектов")
    item_source.delete(0, END)
    item_project.delete(0, END)
    num.delete(0, END)
    note.delete(0, END)

    directory = r'C:\Users\Виктор\PycharmProjects\purchases'
    files = os.listdir(directory)
    for f in files:
        if f[-6:] == 'gp.csv':
            f = f[:-6]
            item_source.insert(END, f)

    scrollbar.pack(side=RIGHT, fill=Y)

    item_source.bind('<space>', view_sum)
    root.bind('o', open_file)
    root.bind('s', save_file)

    item_source.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_source.yview)
    item_project.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=item_project.yview)
    num.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=num.yview)
    note.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=note.yview)
