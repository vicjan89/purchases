import csv
import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

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



def view_sum(event):
    file_name = item_source.curselection()
    progects=[]
    items=[]
    sum_items=[]
    with open(item_source.get(file_name[0])+'gp.csv', "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            progects.append(row)
    with open('??????.csv', 'r', newline="", encoding='utf-8') as file:
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
    root.title("?????????????? ???????????????????????? ???????????? ????????????????")
    item_source.delete(0, END)
    item_project.delete(0, END)
    num.delete(0, END)
    note.delete(0, END)

    directory = r'C:\Users\????????????\PycharmProjects\purchases'
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

root = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

note = ttk.Notebook(root)

f_prg = ttk.Frame(note)
note.add(f_prg, text = '???????????????????????? ????????????????')
scrollbar = Scrollbar(f_prg)
item_source = Listbox(f_prg, yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
item_project = Listbox(f_prg, yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
note.pack(side = 'left', fill = 'both')
FILENAME = r'C:\Users\????????????\PycharmProjects\purchases\??????.csv'
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

f_gp = ttk.Frame(note)
note.add(f_gp, text = '???????????? ????????????????')
directory = r'C:\Users\????????????\PycharmProjects\purchases'
files = os.listdir(directory)
for f in files:
    if f[-4:]=='.csv' and f[-6:-4]!='gp' and f[0:3]!='??????':
         f=f[0:-4]
         item_source.insert(END,f)

scrollbar = Scrollbar(f_gp)
prg_source = Listbox(f_gp, yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
prg_to_group = Listbox(f_gp, yscrollcommand=scrollbar.set, width=80, selectmode=EXTENDED, exportselection=0)
scrollbar.pack(side=RIGHT, fill=Y)

prg_source.bind('<space>', add)
prg_source.bind('+', change_num_item_project)
prg_source.bind('-', change_num_item_project)
prg_source.bind('*', change_num_item_project)
prg_source.bind('/', change_num_item_project)
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

f_sumgp = ttk.Frame(note)
note.add(f_sumgp, text = '?????????? ???????????????????? ?????? ????????????')

prefix_file_to_save=''

root.title("???????????????????? ??????????????????")
root.geometry("1300x700+0+0")
root.mainloop()