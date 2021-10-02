import csv
from tkinter import *

def add(event):
    ind=item_source.curselection()
    for i in ind:
        item_project.insert(END, s[i])
        num.insert(END, 1)

def del_item_project(event):
    ind=item_project.curselection()
    for i in ind:
        item_project.delete(i)
        num.delete(i)

def change_num_item_project(event):
    ind=item_project.curselection()
    print(event)
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
    for i in ind:
        n=num.get(i)
        if n+d>0:
            num.delete(i)
            num.insert(i,n+d)

FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\ТМЦ.csv'
s = []
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        s.append(row[0])


root = Tk()
root.title("Формирование спецификации проекта")
root.geometry("1300x700+0+0")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

item_source = Listbox(yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED)
item_project=Listbox(yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED)
num=Listbox(yscrollcommand=scrollbar.set, width=8)

for item in s:
    item_source.insert(END, item)

item_source.bind('<space>', add)
item_project.bind('<Delete>', del_item_project)
item_project.bind('+', change_num_item_project)
item_project.bind('-', change_num_item_project)
item_project.bind('*', change_num_item_project)
item_project.bind('/', change_num_item_project)

item_source.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=item_source.yview)
item_project.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=item_project.yview)
num.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=num.yview)
root.mainloop()