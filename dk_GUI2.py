import tkinter as tk  
import database_script as ds
# from PIL import Image, ImageTk
# import io

root = tk.Tk()
root.title("HOMO-MIX访客记录管理系统")
root.geometry("800x650")

def update_text(text):
    text.delete(1.0, "end")
    text.insert("insert", "序列号\t访客姓名\t访客电话\t来访原因\t公寓楼栋\t来访时间\n")
    ds.query_visitor()
    for row in ds.pub_out:
        text.insert("insert", str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\t" + str(row[5]) + "\t\n")
    while len(ds.pub_out) > 0:
        ds.pub_out.pop()

def on_button1_click():
    ds.pub_in.append(entry1.get())
    ds.pub_in.append(entry2.get())
    ds.pub_in.append(entry3.get())
    ds.pub_in.append(entry4.get())
    ds.pub_in.append(entry5.get())
    ds.pub_in.append(entry6.get())
    ds.insert_visitor()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

def on_button2_click():
    ds.pub_in.append(entry1.get())
    ds.delete_visitor()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

def on_button3_click():
    ds.pub_in.append(entry1.get())
    ds.pub_in.append(entry2.get())
    ds.pub_in.append(entry3.get())
    ds.pub_in.append(entry4.get())
    ds.pub_in.append(entry5.get())
    ds.pub_in.append(entry6.get())
    ds.update_visitor()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

# 输入框
label1 = tk.Label(root, text="序列号")
label1.place(x=50, y=50)
entry1 = tk.Entry(root)
entry1.place(x=150, y=50)
label2 = tk.Label(root, text="访客姓名")
label2.place(x=50, y=100)
entry2 = tk.Entry(root)
entry2.place(x=150, y=100)
label3 = tk.Label(root, text="访客电话")
label3.place(x=50, y=150)
entry3 = tk.Entry(root)
entry3.place(x=150, y=150)
label4 = tk.Label(root, text="来访原因")
label4.place(x=50, y=200)
entry4 = tk.Entry(root)
entry4.place(x=150, y=200)
label5 = tk.Label(root, text="公寓楼栋")
label5.place(x=50, y=250)
entry5 = tk.Entry(root)
entry5.place(x=150, y=250)
label6 = tk.Label(root, text="来访时间")
label6.place(x=50, y=300)
entry6 = tk.Entry(root)
entry6.place(x=150, y=300)

# 按钮
button1 = tk.Button(root, text="插入记录", command=on_button1_click)
button1.place(x=50, y=350)
button2 = tk.Button(root, text="删除记录", command=on_button2_click)
button2.place(x=50, y=400)
button3 = tk.Button(root, text="更新记录", command=on_button3_click)
button3.place(x=50, y=450)

# 输出框
text = tk.Text(root)
text.place(x=300, y=50)
update_text(text)

root.mainloop()

