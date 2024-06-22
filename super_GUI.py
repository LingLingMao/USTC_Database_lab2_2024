import tkinter as tk  
import database_script as ds
from PIL import Image, ImageTk
import io

root = tk.Tk()
root.title("HOMO-MIX宿管信息管理系统")
root.geometry("800x650")

def update_text(text):
    text.delete(1.0, "end")
    text.insert("insert", "工号\t姓名\t性别\t电话\t宿舍楼\n")
    ds.query_dk()
    for row in ds.pub_out:
        text.insert("insert", str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\t\n")
    while len(ds.pub_out) > 0:
        ds.pub_out.pop()

def on_button1_click():
    ds.pub_in.append(entry1.get())
    ds.pub_in.append(entry2.get())
    ds.pub_in.append(entry3.get())
    ds.pub_in.append(entry4.get())
    ds.pub_in.append(entry5.get())
    ds.pub_in.append(entry6.get())
    ds.insert_dk()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

def on_button2_click():
    ds.pub_in.append(entry1.get())
    ds.delete_dk()
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
    ds.update_dk()
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    update_text(text)

def on_button4_click():
    ds.pub_in.append(entry1.get())
    ds.query_dk_image()

    # 显示blob字段的二进制图片
    blob_data = ds.pub_out[0][5]
    image = Image.open(io.BytesIO(blob_data))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.place(x=500, y=400)
    while len(ds.pub_in) > 0:
        ds.pub_in.pop()
    while len(ds.pub_out) > 0:
        ds.pub_out.pop()

# 输入框
label1 = tk.Label(root, text="工号")
label1.place(x=50, y=50)
entry1 = tk.Entry(root)
entry1.place(x=100, y=50)
label2 = tk.Label(root, text="姓名")
label2.place(x=50, y=100)
entry2 = tk.Entry(root)
entry2.place(x=100, y=100)
label3 = tk.Label(root, text="性别")
label3.place(x=50, y=150)
entry3 = tk.Entry(root)
entry3.place(x=100, y=150)
label4 = tk.Label(root, text="电话")
label4.place(x=50, y=200)
entry4 = tk.Entry(root)
entry4.place(x=100, y=200)
label5 = tk.Label(root, text="宿舍楼")
label5.place(x=50, y=250)
entry5 = tk.Entry(root)
entry5.place(x=100, y=250)
label6 = tk.Label(root, text="照片名")
label6.place(x=50, y=300)
entry6 = tk.Entry(root)
entry6.place(x=100, y=300)

# 按钮
button1 = tk.Button(root, text="插入宿管信息", command=on_button1_click)
button1.place(x=50, y=350)
button2 = tk.Button(root, text="删除宿管信息", command=on_button2_click)
button2.place(x=50, y=400)
button3 = tk.Button(root, text="更新宿管信息", command=on_button3_click)
button3.place(x=50, y=450)
button4 = tk.Button(root, text="查询宿管照片", command=on_button4_click)
button4.place(x=50, y=500)

# 输出框
text = tk.Text(root)
text.place(x=300, y=50)
update_text(text)

root.mainloop()

