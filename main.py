import csv
from tkinter import *
from tkinter import filedialog as fd

def add(event):
    ind=item_source.curselection()
    for i in ind:
        item_project.insert(END, item_source.get(i))
        num.insert(END, 1)

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
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.csv"),
                   ("All files", "*.*")))
    root.title(file_name)
    s = zip(item_project.get(0,END),num.get(0,END),note.get(0,END))
    with open(file_name+'.csv', "w", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(s)

root = Tk()
root.title("Формирование спецификации проекта")
root.geometry("1300x700+0+0")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

item_source = Listbox(yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED)
item_project=Listbox(yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED)
num=Listbox(yscrollcommand=scrollbar.set, width=7)
note=Listbox(yscrollcommand=scrollbar.set, width=30)

FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\ТМЦ.csv'
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        item_source.insert(END, row[0])

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
root.bind('s',save_file)

item_source.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=item_source.yview)
item_project.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=item_project.yview)
num.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=num.yview)
note.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=note.yview)
root.mainloop()