import csv
import os
from tkinter import *
from tkinter import filedialog as fd

root = Tk()
scrollbar = Scrollbar(root)
item_source = Listbox(yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
item_project = Listbox(yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
num = Listbox(yscrollcommand=scrollbar.set, width=7, exportselection=0)
note = Listbox(yscrollcommand=scrollbar.set, width=30, exportselection=0)
prefix_file_to_save=''

def add(event):
    ind=item_source.curselection()
    for i in ind:
        item_project.insert(END, item_source.get(i))
        num.insert(END, 1)
        note.insert(END,' ')

def del_item_project(event):
    ind=item_project.curselection()
    for i in reversed(ind):
        item_project.delete(i)
        num.delete(i)
        note.delete(i)

def change_num_item_project(event):
    ind=item_project.curselection()
    d=0
    if event.char == '+':
        d=1
    elif event.char == '-':
        d=-1
    elif event.char == '*':
        d=10
    elif event.char == '/':
        d = -10
    else:
        pass
    if ind == ():
        l = num.size()
        ind = range(l-1,l)
    for i in ind:
        n=int(num.get(i))
        if n+d>0:
            num.delete(i)
            num.insert(i,n+d)

def open_file(event):
    file_name = fd.askopenfilename()
    root.title(file_name)
    item_project.delete(0,END)
    num.delete(0,END)
    note.delete(0,END)
    with open(file_name, "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            item_project.insert(END, row[0])
            num.insert(END, row[1])
            note.insert(END,row[2])

def save_file(event):
    global prefix_file_to_save
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.csv"),
                   ("All files", "*.*")))
    if file_name[-4:]=='.csv':
        file_name=file_name[0:-4]
    file_name=file_name+prefix_file_to_save+'.csv'
    prefix_file_to_save = ''
    root.title(file_name)
    s = zip(item_project.get(0,END),num.get(0,END),note.get(0,END))
    with open(file_name, "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(s)

def save_group(event):
    global prefix_file_to_save
    prefix_file_to_save='gp'
    save_file(event)

def project():

    root.title("Формирование спецификации проекта")

    item_source.delete(0,END)
    item_project.delete(0,END)
    num.delete(0,END)
    note.delete(0,END)
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

    root.title("Формирование группы проектов")
    item_source.delete(0,END)
    item_project.delete(0,END)
    num.delete(0,END)
    note.delete(0,END)

    directory = r'C:\Users\Виктор\PycharmProjects\purchases'
    files = os.listdir(directory)
    for f in files:
        if f[-4:]=='.csv' and f[-6:-4]!='gp' and f[0:3]!='ТМЦ':
            f=f[0:-4]
            item_source.insert(END,f)

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
    progects=[]
    items=[]
    sum_items=[]
    with open(item_source.get(file_name[0])+'gp.csv', "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            progects.append(row)
    with open('ТМЦ.csv', 'r', newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row[0])
    for prg in progects:
        with open(prg[0]+'.csv', 'r', newline="", encoding='utf-8') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0] in sum_items:
                    i=sum_items.index(row[0])
                    print(i)
                    sum_items[i][1]+=1
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

root.title("Управление закупками")
root.geometry("1300x700+0+0")

main_menu = Menu()
main_menu.add_cascade(label="Проекты", command=project)
main_menu.add_cascade(label="Группы проектов", command=group_projects)
main_menu.add_cascade(label="Спецификация группы объектов", command=sum_group_projects)
root.config(menu=main_menu)

root.mainloop()