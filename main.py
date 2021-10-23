import csv
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

root = Tk()
root.title("Управление закупками")
root.geometry("1300x700+0+0")

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# create a treeview
tree = ttk.Treeview(root)
tree.heading('#0', text='Закупки', anchor='w')

FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\Спецификации.csv'
date = []
i1 = 0
i2 = 0
i3 = 0
i = 0
with open(FILENAME, "r", newline="", encoding='utf-8') as file1:
    reader1 = csv.reader(file1)
    for row1 in reader1:
        tree.insert('', tk.END, text=row1[0], iid=i, open=True)
        i1 = i
        i += 1
        with open(row1[0]+'.csv', 'r', newline="", encoding='utf-8') as file2:
            reader2 = csv.reader(file2)
            for row2 in reader2:
                tree.insert(i1, tk.END, text=row2[0]+' - '+row2[1]+' шт.', iid=i, open=False)
                i2 = i
                i += 1
                with open(row2[0]+'.csv', 'r', newline="", encoding='utf-8') as file3:
                    reader3 = csv.reader(file3)
                    for row3 in reader3:
                        tree.insert(i2, tk.END, text=row3[0]+' \t '+row3[1]+' шт. \t '+row3[2], iid=i, open=False)
                        i += 1


# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

root.mainloop()


def change_num_item_project(event):
    ind = item_project.curselection()
    d = 0
    if event.char == '+':
        d = 1
    elif event.char == '-':
        d = -1
    elif event.char == '*':
        d = 10
    elif event.char == '/':
        d = -10
    else:
        pass
    if ind == ():
        l = num.size()
        ind = range(l - 1, l)
    for i in ind:
        n = int(num.get(i))
        if n + d > 0:
            num.delete(i)
            num.insert(i, n + d)


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
