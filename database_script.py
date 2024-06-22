import mysql.connector  

pub_in = [] # 临时存放输入框的数据
pub_out = [] # 临时存放输出框的数据

'''
def connect_to_database():  
    # 创建数据库连接  
    cnx = mysql.connector.connect(user='root', password='031006',  
                                  host='localhost', database='sys')  
    cursor = cnx.cursor()  
  
    # 执行一个查询  
    query = ("SELECT * FROM Student")  
    cursor.execute(query)  
  
    # 获取查询结果  
    results = cursor.fetchall()  
    for row in results:  
        print(row)  
  
    # 关闭连接  
    cursor.close()  
    cnx.close()  
'''

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insert_student():
    # 创建数据库连接  
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')  
    cursor = cnx.cursor()  

    # 执行一个插入
    if pub_in[6] == '':
        blob = 'NULL'
    else:
        blob = convertToBinaryData("./photos/"+pub_in[6])
    add_student = ("INSERT INTO Student values (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(add_student, (pub_in[0], pub_in[1], pub_in[2], pub_in[3], pub_in[4], pub_in[5], blob))
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def delete_student():
    # 创建数据库连接  
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个删除
    delete_student = ("DELETE FROM Student WHERE Student.s_id = '" + str(pub_in[0]) + "'")
    cursor.execute(delete_student)
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()


def update_student():
    delete_student()
    insert_student()

def query_student():
    # 创建数据库连接  
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')  
    cursor = cnx.cursor()  
  
    # 执行一个查询  
    query = ("SELECT * FROM Student")  
    cursor.execute(query)  
  
    # 获取查询结果  
    results = cursor.fetchall()  
    for row in results:  
        pub_out.append(row)
  
    # 关闭连接  
    cursor.close()  
    cnx.close()  

def query_student_image():
    # 创建数据库连接  
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个查询
    query = ("SELECT * FROM Student WHERE Student.s_id = '" + str(pub_in[0]) + "'")
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()
    for row in results:
        pub_out.append(row)

    # 关闭连接
    cursor.close()
    cnx.close()

def query_visitor():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个查询
    query = ("SELECT * FROM Visitor")
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()
    for row in results:
        pub_out.append(row)

    # 关闭连接
    cursor.close()
    cnx.close()

def insert_visitor():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个插入
    add_visitor = ("INSERT INTO Visitor values (%s, %s, %s, %s, %s, %s)")
    cursor.execute(add_visitor, (pub_in[0], pub_in[1], pub_in[2], pub_in[3], pub_in[4], pub_in[5]))
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def delete_visitor():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个删除
    delete_visitor = ("DELETE FROM Visitor WHERE Visitor.v_id = '" + str(pub_in[0]) + "'")
    cursor.execute(delete_visitor)
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def update_visitor():
    delete_visitor()
    insert_visitor()

def query_repair():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个查询
    query = ("SELECT Repair.r_id, Repair.r_man_id, Repair.r_build, Repair.r_dorm, Repair_state(Repair.r_state), Repair.r_content, Repair.r_stu_id FROM Repair")
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()
    for row in results:
        pub_out.append(row)

    # 关闭连接
    cursor.close()
    cnx.close()

def insert_repair():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个插入
    add_repair = ("INSERT INTO Repair values (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(add_repair, (pub_in[0], pub_in[1], pub_in[2], pub_in[3], pub_in[4], pub_in[5], pub_in[6]))
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()
    
def delete_repair():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个删除
    delete_repair = ("call delete_repair('"+pub_in[0]+"')")
    cursor.execute(delete_repair)
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def update_repair():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个更新
    update = ("update Repair set Repair.r_state = %s where Repair.r_id = %s")
    cursor.execute(update, ('T', pub_in[0]))
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()


def query_dk():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个查询
    query = ("SELECT * FROM DormKeeper")
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()
    for row in results:
        pub_out.append(row)

    # 关闭连接
    cursor.close()
    cnx.close()

def insert_dk():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个插入
    if pub_in[5] == '':
        blob = 'NULL'
    else:
        blob = convertToBinaryData("./photos/"+pub_in[5])
    add_dk = ("INSERT INTO DormKeeper values (%s, %s, %s, %s, %s, %s)")
    cursor.execute(add_dk, (pub_in[0], pub_in[1], pub_in[2], pub_in[3], pub_in[4], blob))
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def delete_dk():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个删除
    delete_dk = ("DELETE FROM DormKeeper WHERE DormKeeper.dk_id = '" + str(pub_in[0]) + "'")
    cursor.execute(delete_dk)
    cnx.commit() # 提交事务

    # 关闭连接
    cursor.close()
    cnx.close()

def update_dk():
    delete_dk()
    insert_dk()
    
def query_dk_image():
    # 创建数据库连接
    cnx = mysql.connector.connect(user='root', password='031006', host='localhost', database='sys')
    cursor = cnx.cursor()

    # 执行一个查询
    query = ("SELECT * FROM DormKeeper WHERE DormKeeper.dk_id = '" + str(pub_in[0]) + "'")
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()
    for row in results:
        pub_out.append(row)

    # 关闭连接
    cursor.close()
    cnx.close()