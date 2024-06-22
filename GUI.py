import tkinter as tk  
import os

root = tk.Tk()  
root.title("HOMO-MIX学生宿舍管理系统")  
root.geometry("300x200")  
label = tk.Label(root, text="请选择您的身份：")  
label.pack()

def on_button1_1_click():
    os.system("python dk_GUI1.py")
    
def on_button1_2_click():
    os.system("python dk_GUI2.py")

def on_button1_click():  
    tk1 = tk.Toplevel(root)
    tk1.title("宿管")
    tk1.geometry("300x200")
    label1 = tk.Label(tk1, text="宿管操作页面")
    label1.pack()
    botton1_1 = tk.Button(tk1, text="学生信息管理", command=on_button1_1_click)
    botton1_1.pack()
    botton1_2 = tk.Button(tk1, text="访客记录管理", command=on_button1_2_click)
    botton1_2.pack()

def on_button2_click():
    os.system("python stu_GUI.py")

def on_button3_click():
    os.system("python rp_GUI.py")

def on_button4_click():
    os.system("python super_GUI.py")

# 创建一个按钮，并指定点击时调用的函数  
button1 = tk.Button(root, text="我是宿管", command=on_button1_click)  
button1.pack()
botton2 = tk.Button(root, text="我是学生", command=on_button2_click)
botton2.pack()
botton3 = tk.Button(root, text="我是维修工", command=on_button3_click)
botton3.pack()
botton4 = tk.Button(root, text="我是管理员", command=on_button4_click)
botton4.pack()
botton5 = tk.Button(root, text="退出", command=root.quit)
botton5.pack()
# 开始Tkinter的事件循环  
root.mainloop()