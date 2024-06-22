import tkinter as tk  
import database_script as ds

root = tk.Tk()
root.title('HOMO-MIX维修人员办公系统')
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
    ds.update_repair()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

# 输入框
label1 = tk.Label(root, text="单号")
label1.place(x=50, y=50)
entry1 = tk.Entry(root)
entry1.place(x=100, y=50)

# 按钮
button1 = tk.Button(root, text="已处理", command=on_button1_click)
button1.place(x=50, y=100)

# 输出框
text = tk.Text(root)
text.place(x=300, y=50)
update_text(text)

root.mainloop()

