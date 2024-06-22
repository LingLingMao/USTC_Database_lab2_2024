import tkinter as tk  
import database_script as ds

root = tk.Tk()
root.title('HOMO-MIX学生宿舍维修申报系统')
root.geometry("800x650")

def update_text(text):
    text.delete(1.0, "end")
    text.insert("insert", "单号\t\t工号\t楼栋 房间 状态\t维修内容\t申请人学号\t\n")
    ds.query_repair()
    for row in ds.pub_out:
        text.insert("insert", str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\t" + str(row[5]) + "\t" + str(row[6]) + "\t\n")
    while len(ds.pub_out) > 0:
        ds.pub_out.pop()

def on_button1_click():
    ds.pub_in.append(entry1.get())
    ds.pub_in.append(entry2.get())
    ds.pub_in.append(entry3.get())
    ds.pub_in.append(entry4.get())
    ds.pub_in.append(entry5.get())
    ds.pub_in.append(entry6.get())
    ds.pub_in.append(entry7.get())
    ds.insert_repair()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

def on_button2_click():
    ds.pub_in.append(entry1.get())
    ds.delete_repair()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

# 输入框
label1 = tk.Label(root, text="单号")
label1.place(x=50, y=50)
entry1 = tk.Entry(root)
entry1.place(x=100, y=50)
label2 = tk.Label(root, text="工号")
label2.place(x=50, y=100)
entry2 = tk.Entry(root)
entry2.place(x=100, y=100)
label3 = tk.Label(root, text="楼栋")
label3.place(x=50, y=150)
entry3 = tk.Entry(root)
entry3.place(x=100, y=150)
label4 = tk.Label(root, text="房间")
label4.place(x=50, y=200)
entry4 = tk.Entry(root)
entry4.place(x=100, y=200)
label5 = tk.Label(root, text="状态")
label5.place(x=50, y=250)
entry5 = tk.Entry(root)
entry5.place(x=100, y=250)
label6 = tk.Label(root, text="维修内容")
label6.place(x=50, y=300)
entry6 = tk.Entry(root)
entry6.place(x=100, y=300)
label7 = tk.Label(root, text="学号")
label7.place(x=50, y=350)
entry7 = tk.Entry(root)
entry7.place(x=100, y=350)

# 按钮
button1 = tk.Button(root, text="申报", command=on_button1_click)
button1.place(x=50, y=400)
button2 = tk.Button(root, text="撤销申报", command=on_button2_click)
button2.place(x=50, y=450)

# 输出框
text = tk.Text(root)
text.place(x=300, y=50)
update_text(text)

root.mainloop()
