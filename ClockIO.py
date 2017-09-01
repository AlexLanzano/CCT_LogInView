from Tkinter import *
from tkFont import Font
import MySQLdb
root = Tk()

db =MySQLdb.connect(host = "",
                   user = "",
                   passwd = "",
                   db = "",
                   port = )

cur = db.cursor()

root.wm_title("Working Projects")
root.titleFont = Font(family = "Georgia", size = 35, weight = "bold")
root.h2Font = Font(family = "CenturyGothic", size = 30, weight = "bold")
root.textFont = Font(family = "CenturyGothic", size = 25, weight = "bold")

group1 = []
group2 = []

print(group1)
cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 1 AND isclockedon = 1") #Need to add check for currently here
for mana in cur.fetchall():
    group1.append(str(mana)[1:-3])

cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 0 AND isclockedon = 1")
for u in cur.fetchall():
    group2.append(str(u)[1:-3])

usercurprojects = []
managercurprojects = []

#Color Scheme
#background
bgcolor = "#000000"
#foreground
fgcolor = "#1d2120"
#H1 text
h1color = "#00d800"
#H2 text
h2color = "#00d800"
#ListBox color
listColor = "#4e5452"
#ListBox Highlight Color
hlcolor = "#00d800"

group1sel = 0
group2sel = 0

wwidth = 1000
wheight = 500

root.geometry("1000x500")
root.configure(background = bgcolor)

group1names = []
group2names = []

#Populating ManagerID list
cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 1 AND isclockedon = 1")
for mana in cur.fetchall():
    group1.append(str(mana)[1:-3])

#Populating UserID list
cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 0 AND isclockedon = 1")
for u in cur.fetchall():
    group2.append(str(u)[1:-3])

#Populating UserName list
for ids in group2:
    cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
    username = str(cur.fetchone())[2:-3]
    cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
    username = username + " " + str(cur.fetchone())[2:-3]
    group2names.append(username)
#Populating ManagerName list
for ids in group1:
    cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
    mananame = str(cur.fetchone())[2:-3]
    cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
    mananame = mananame + " " + str(cur.fetchone())[2:-3]
    group1names.append(mananame)
#Current Managers Available

Label(root, text = "Managers Available", bg = bgcolor, fg = h1color, font = root.titleFont).pack()
first = Frame(root)
first.pack()
first.configure(background = fgcolor)
managers = Listbox(first, width = wwidth/20, height = wheight/50, exportselection = 0,bg = listColor, selectbackground = hlcolor)
for i in range(len(group1names)):
    managers.insert(i+1,group1names[i])
managers.select_set(group1sel)
managers.see(group1sel)
managers.grid(column=0, row=0, rowspan=3, padx = 10, pady = 10)

#Manager Project List Box
if(len(group1) > 0):
    cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
    firstmananame = str(cur.fetchone())[2:-3]
    cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
    lastmananame = str(cur.fetchone())[2:-3]
    mananame = firstmananame + " " + lastmananame

    cur.execute("SELECT project FROM cctprojects WHERE cctid = '%s'"% (group1[group1sel],))
    for proj in cur.fetchall():
        managercurprojects.append(str(proj)[2:-3])

if(len(group1) > 0):
    managerspro = Label(first, text = mananame + "'s Current Projects", bg = fgcolor, fg = h2color, font = root.h2Font, width = wwidth/25)
    managerspro.grid(column=1, row = 0)
    managersprolist = Text(first, width = wwidth/25, height = 5, bd = 5, bg = fgcolor, fg = h2color, font = root.textFont, state = NORMAL, highlightthickness = 0)
    managersprolist.tag_configure("center", justify = "center")
    #cur.execute("SELECT count(*) FROM cctprojects WHERE isadmin = 0")
    for i in range(len(managercurprojects)):
        managersprolist.insert(str(i)+".0",managercurprojects[i] + "\n", "center")
    managersprolist.configure(state= DISABLED)
    managersprolist.grid(column=1, row=1, rowspan=1,  sticky = N)

#Current Users Available

Label(root, text = "Current Users", bg = bgcolor, fg = h1color, font = root.titleFont).pack()
second = Frame(root)
second.pack()
second.configure(background = fgcolor)
#usertitle = Label(second, text = "user List", bg = "#767a7f", fg = "orange")
#usertitle.grid(column=0, row = 0, sticky = W+E)
users = Listbox(second, width = wwidth/20, height = wheight/45, exportselection = 0, bg = listColor, selectbackground = hlcolor)
for i in range(len(group2names)):
    users.insert(i+1,group2names[i])
users.select_set(group2sel)
users.see(group2sel)
users.grid(column=0, row=0, rowspan=3, padx = 10, pady = 10)

#User Project List Box
if(len(group2) > 0):
    cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
    firstusername = str(cur.fetchone())[2:-3]
    cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
    lastusername = str(cur.fetchone())[2:-3]
    username = firstusername + " " + lastusername

    cur.execute("SELECT project FROM cctprojects WHERE cctid = '%s'"% (group2[group2sel],))
    for proj in cur.fetchall():
        usercurprojects.append(str(proj)[2:-3])
if(len(group2) > 0):

    userpro = Label(second, text = username + "'s Current Projects", bg = fgcolor, fg = h2color, font = root.h2Font, width = wwidth/25)
    userpro.grid(column=1, row = 0)
    usersprolist = Text(second, width = wwidth/25, height = 5, bd = 5, bg = fgcolor, fg = h2color, font = root.textFont, state = NORMAL, highlightthickness = 0)
    usersprolist.tag_configure("center", justify = "center")
    for i in range(len(usercurprojects)):
        usersprolist.insert(str(i)+".0",usercurprojects[i] + "\n","center")
    usersprolist.configure(state = DISABLED)
    usersprolist.grid(column=1, row=1, rowspan=1, sticky = N)
    userpro.grid(column=1, row = 0)

wwidth = root.winfo_width()
wheight = root.winfo_height()

def update():

    global group1sel,group2sel,wwidth,wheight, managerspro, userpro
    group1 = []
    group2 = []
    group1names = []
    group2names = []
    usercurprojects = []
    managercurprojects = []

    #Populating ManagerID list
    cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 1 AND isclockedon = 1")
    for mana in cur.fetchall():
        group1.append(str(mana)[1:-3])

    #Populating UserID list
    cur.execute("SELECT cctid FROM cctpeople WHERE isadmin = 0 AND isclockedon = 1")
    for u in cur.fetchall():
        group2.append(str(u)[1:-3])

    #Populating UserName list
    for ids in group2:
        cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (ids,))
        username = str(cur.fetchone())[2:-3]
        cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (ids,))
        username = username + " " + str(cur.fetchone())[2:-3]
        group2names.append(username)
    #Populating ManagerName list
    for ids in group1:
        cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (ids,))
        mananame = str(cur.fetchone())[2:-3]
        cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (ids,))
        mananame = mananame + " " + str(cur.fetchone())[2:-3]
        group1names.append(mananame)

    managers.delete(0,END)
    for i in range(len(group1names)):
        managers.insert(i+1,group1names[i])
    managers.select_set(group1sel)
    managers.see(group1sel)
    managers.config(width = wwidth/30, height = wheight/50)

    if(len(group1) > 0):
        cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
        firstmananame = str(cur.fetchone())[2:-3]
        cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group1[group1sel],))
        lastmananame = str(cur.fetchone())[2:-3]
        mananame = firstmananame + " " + lastmananame

        cur.execute("SELECT project FROM cctprojects WHERE cctid = '%s'"% (group1[group1sel],))
        for proj in cur.fetchall():
            managercurprojects.append(str(proj)[2:-3])

        print(managercurprojects)
        managerspro.config(text = mananame + "'s Current Projects")
        managersprolist.configure(state= NORMAL)
        managersprolist.delete("1.0",END)
        print("before")
        print(str(managersprolist.get("1.0",END)))
        managersprolist.config(width = wwidth/35, height = 5)
        for i in range(len(managercurprojects)):
            managersprolist.insert(str(i)+".0",managercurprojects[i] + "\n", "center")
        managersprolist.configure(state= DISABLED)
        print("after")
        print(str(managersprolist.get("1.0",END)))

    users.delete(0,END)
    for i in range(len(group2names)):
        users.insert(i+1,group2names[i])
    users.select_set(group2sel)
    users.see(group2sel)
    users.config(width = wwidth/30, height = wheight/45)

    print(len(group2))
    if(len(group2) > 0):
        for userid in group2:
            cur.execute("SELECT firstname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
            firstusername = str(cur.fetchone())[2:-3]
            cur.execute("SELECT lastname FROM cctpeople WHERE cctid = '%s'"% (group2[group2sel],))
            lastusername = str(cur.fetchone())[2:-3]
            username = firstusername + " " + lastusername

        cur.execute("SELECT project FROM cctprojects WHERE cctid = '%s'"% (group2[group2sel],))
        for proj in cur.fetchall():
            usercurprojects.append(str(proj)[2:-3])

        userpro.config(text = username + "'s Current Projects")
        usersprolist.configure(state= NORMAL)
        usersprolist.delete(1.0,END)
        for i in range(len(usercurprojects)):
            usersprolist.insert(str(i)+".0",usercurprojects[i] + "\n","center")
        usersprolist.config(width = wwidth/35, height = 5, state = DISABLED)
    if group1sel >= len(group1)-1:
        group1sel = 0
    else:
        group1sel += 1

    if group2sel >= len(group2)-1:
        group2sel = 0
    else:
        group2sel += 1

    wwidth = root.winfo_width()
    wheight = root.winfo_height()
    print("Update")
    root.after(5000,update)

root.after(0,update)
root.mainloop()
