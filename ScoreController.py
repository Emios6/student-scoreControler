# 简易学生管理系统
from typing import List, Dict
import sys

# 定义一个存放学生信息的工作列表
studentsList: List[Dict[str, str]] = []
# 存放密码信息
passwdListStu: List[Dict[str, str]] = []
passwdListTech: List[Dict[str, str]] = []
passwdListRoot: List[Dict[str, str]] = []

# 学生信息存放位置
file_path = 'C:\\Users\\wkb\\Desktop\\student.txt'
# 密码存放
file_path_passwd_stu = 'C:\\Users\\wkb\\Desktop\\password-stu.txt'
file_path_passwd_tech = 'C:\\Users\\wkb\\Desktop\\password-tech.txt'
file_path_passwd_root = 'C:\\Users\\wkb\\Desktop\\password-root.txt'
# 全局变量，记录登录人的ID
user = None


# 读取的密码
def readFilePasswd(path, wlist):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            fileList = file.readlines()
        # 将读取出来的信息转换为字典放到passwdList
        for i in range(1, len(fileList)):
            temList = fileList[i].split()
            tempdir = {
                "ID": temList[0],
                "passwd": temList[1]
            }
            wlist.append(tempdir)
    except IOError:
        print("Error: 没有找到文件或读取文件失败!")
    except Exception as e:
        print(f"发生异常: {str(e)}")


# 初始页面,输入账号和密码进行登录
def init():
    try:
        global user
        # 读取ID和密码
        readFilePasswd(file_path_passwd_stu, passwdListStu)
        readFilePasswd(file_path_passwd_tech, passwdListTech)
        readFilePasswd(file_path_passwd_root, passwdListRoot)
        find = 0
        ID = input("请输入用户名：")
        user = ID
        passwd = input("请输入密码：")
        for i in passwdListStu:
            if ID == i['ID'] and passwd == i['passwd']:
                find = 1
        for i in passwdListTech:
            if ID == i['ID'] and passwd == i['passwd']:
                find = 2
        for i in passwdListRoot:
            if ID == i['ID'] and passwd == i['passwd']:
                find = 3
        match find:
            case 0:
                print("您输入的用户名或密码有误，请检查后重新输入")
                init()
            case 1:
                print("登录成功！")
                menuStu()
            case 2:
                print("登陆成功！")
                menuTech()
            case 3:
                print("登陆成功！")
                menuRoot()
    except Exception as e:
        print(f"发生异常: {str(e)}")


# 读取文件中的学生信息
def readFile():
    try:
        # 读取文件信息
        with open(file_path, 'r', encoding='utf-8') as file:
            fileList = file.readlines()
    except IOError:
        print("Error: 没有找到文件或读取文件失败!")
    else:
        # 将读取出来的信息转为字典后存放到工作列表studentsList
        for i in range(1, len(fileList)):
            temList = fileList[i].split()
            tempdir = {
                "studentID": temList[0],
                "name": temList[1],
                "number": temList[2],
                "email": temList[3],
                "pythonScore": temList[4],
                "databaseScore": temList[5],
                "IOTScore": temList[6],
                "sumScore": temList[7]
            }
            studentsList.append(tempdir)


# 学生菜单
def menuStu():
    while True:
        try:
            print("-------------------------------")
            print("功能选择如下：")
            print("1.查询本人信息。")
            print("2.修改本人信息。")
            print("3.查询本人成绩。")
            print("4.查询总排名。")
            print("5.修改密码。")
            print("0.退出程序。")
            print("-------------------------------")
            flag = int(input("请输入选择的功能："))
            match flag:
                case 0:
                    saveFileStu()
                    print("欢迎下次使用！")
                    sys.exit()
                case 1:
                    queryStu()
                case 2:
                    modifyStuPerson()
                case 3:
                    queryScore()
                case 4:
                    rankStudents()
                case 5:
                    modifyPasswd(file_path_passwd_stu, passwdListStu, 1)
        except ValueError as e1:
            print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
            menuStu()
        except Exception as e:
            print(f"发生异常: {str(e)}")
            menuStu()


# 教师菜单
def menuTech():
    while True:
        try:
            print("-------------------------------")
            print("功能选择如下：")
            print("1.查询全体学生信息。")
            print("2.添加新的学生信息。")
            print("3.查询指定学生信息。")
            print("4.查询指定学生成绩。")
            print("5.查询指定科目的最高分和平均分。")
            print("6.查询总排名。")
            print("7.修改密码。")
            print("8.修改学生信息。")
            print("9.查看不及格学生信息。")
            print("0.退出程序并保存修改。")
            print("-------------------------------")
            flag = int(input("请输入选择的功能："))
            match flag:
                case 0:
                    saveFileStu()
                    print("欢迎下次使用！")
                    sys.exit()
                case 1:
                    displayStudents()
                case 2:
                    appendStudent(2)
                case 3:
                    showStudent(2)
                case 4:
                    showStudentScore(2)
                case 5:
                    showSubjectScore(2)
                case 6:
                    rankStudents()
                case 7:
                    modifyPasswd(file_path_passwd_tech, passwdListTech, 2)
                case 8:
                    modifyStudent(2)
                case 9:
                    failStudents()
        except ValueError as e1:
            print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
            menuTech()
        except Exception as e:
            print(f"发生异常: {str(e)}")
            menuTech()


# 管理员菜单
def menuRoot():
    while True:
        try:
            print("-------------------------------")
            print("功能选择如下：")
            print("1.查询全体学生信息。")
            print("2.添加新的学生信息。")
            print("3.查询指定学生信息。")
            print("4.修改指定学生信息。")
            print("5.删除指定学生信息。")
            print("6.查询指定学生成绩。")
            print("7.查询指定科目的最高分和平均分。")
            print("8.查询总排名。")
            print("9.修改密码。")
            print("10.添加新的用户。")
            print("11.查看不及格学生信息。")
            print("12.删除用户。")
            print("0.退出程序并保存修改。")
            print("-------------------------------")
            flag = int(input("请输入选择的功能："))
            match flag:
                case 0:
                    saveFileStu()
                    print("欢迎下次使用！")
                    sys.exit()
                case 1:
                    displayStudents()
                case 2:
                    appendStudent(3)
                case 3:
                    showStudent(3)
                case 4:
                    modifyStudent(3)
                case 5:
                    deleteStudent()
                case 6:
                    showStudentScore(3)
                case 7:
                    showSubjectScore(3)
                case 8:
                    rankStudents()
                case 9:
                    modifyRoot()
                case 10:
                    rootAppendUser()
                case 11:
                    failStudents()
                case 12:
                    deleteUser()
        except ValueError as e1:
            print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
            menuRoot()
        except Exception as e:
            print(f"发生异常: {str(e)}")
            menuRoot()


# 管理员可修改老师和学生的密码
def modifyRoot():
    try:
        global loc
        find = 0
        sel = int(input("请输入被修改人的身份：1.学生，2.老师，3.管理员:"))
        ID = input("请输入要修改的用户名：")
        match sel:
            case 1:
                for student in range(len(passwdListStu)):
                    if ID == passwdListStu[student]["ID"]:
                        find = 1
                        loc = student
                        break
                if find == 1:
                    passwd = input("请输入新的密码：")
                    passwdListStu[loc]['passwd'] = passwd
                    saveFilePasswd(file_path_passwd_stu, passwdListStu)
                    print("修改成功！")
                    sel1 = int(input("输入1继续进行修改，否则返回上一级！"))
                    if sel1 == 1:
                        modifyRoot()
                    else:
                        menuRoot()
                else:
                    print("您输入的用户不存在！")
            case 2:
                for tech in range(len(passwdListTech)):
                    if ID == passwdListTech[tech]["ID"]:
                        find = 1
                        loc = tech
                        break
                if find == 1:
                    passwd = input("请输入新的密码：")
                    passwdListTech[loc]['passwd'] = passwd
                    saveFilePasswd(file_path_passwd_tech, passwdListTech)
                    print("修改成功！")
                    sel1 = int(input("输入1继续进行修改，否则返回上一级！"))
                    if sel1 == 1:
                        modifyRoot()
                    else:
                        menuRoot()
                else:
                    print("您输入的用户不存在！")
            case 3:
                for root in range(len(passwdListRoot)):
                    if ID == passwdListRoot[root]["ID"]:
                        find = 1
                        loc = root
                        break
                if find == 1:
                    oldPasswd = input("请输入旧密码：")
                    if passwdListRoot[loc]['passwd'] == oldPasswd:
                        passwd = input("请输入新的密码：")
                        passwdListRoot[loc]['passwd'] = passwd
                        saveFilePasswd(file_path_passwd_root, passwdListRoot)
                        print("修改成功！")
                        sel1 = int(input("输入1继续进行修改，否则返回上一级！"))
                        if sel1 == 1:
                            modifyRoot()
                        else:
                            menuRoot()
                    else:
                        print("您输入的密码有误!\n")
                        print("请重试!\n")
                        modifyRoot()
                else:
                    print("您输入的用户不存在！")
    except ValueError as e1:
        print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
        modifyRoot()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        modifyRoot()


# 删除用户
def deleteUser():
    try:
        sel = int(input("请输入要删除的用户身份：1.学生，2.老师"))
        find = 0
        if sel == 1:
            studentID = input("请输入要删除的学生ID：")
            for i in range(len(passwdListStu) - 1, -1, -1):
                if passwdListStu[i]["ID"] == studentID:
                    find = 1
                    del passwdListStu[i]
                    print("删除成功！")
                    saveFilePasswd(file_path_passwd_stu,passwdListStu)
                    in1 = int(input("继续删除请输入1，否则返回主菜单："))
                    if in1 == 1:
                        deleteUser()
                    else:
                        menuRoot()
            if find == 0:
                print("您要删除的学生不存在！")
                in1 = int(input("输入1继续进行删除，否则返回主菜单："))
                if in1 == 1:
                    deleteUser()
                else:
                    menuRoot()
        if sel == 2:
            techID = input("请输入要删除的老师ID：")
            for i in range(len(passwdListTech) - 1, -1, -1):
                if passwdListTech[i]["ID"] == techID:
                    find = 1
                    del passwdListTech[i]
                    print("删除成功！")
                    saveFilePasswd(file_path_passwd_tech,passwdListTech)
                    in1 = int(input("继续删除请输入1，否则返回主菜单："))
                    if in1 == 1:
                        deleteUser()
                    else:
                        menuRoot()
            if find == 0:
                print("您要删除的教师不存在！")
                in1 = int(input("输入1继续进行删除，否则返回主菜单："))
                if in1 == 1:
                    deleteUser()
                else:
                    menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
        deleteUser()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        deleteUser()


# 查看不及格学生的信息
def failStudents():
    try:
        for student in studentsList:
            subjects = []
            if int(student['pythonScore']) < 60:
                subjects.append(f"python程序设计({student['pythonScore']}分)")
            if int(student['databaseScore']) < 60:
                subjects.append(f"数据库({student['databaseScore']}分)")
            if int(student['IOTScore']) < 60:
                subjects.append(f"物联网技术({student['IOTScore']}分)")
            if subjects:
                print(f"姓名：{student['name']} 不及格科目：{' '.join(subjects)}")
    except Exception as e:
        print(f"发生异常: {str(e)}")
        failStudents()


# 修改密码
def modifyPasswd(path, wlist, sel):
    global loc
    try:
        ID = input("请输入要修改的用户名：")
        find = 0
        for i in range(len(wlist)):
            if ID == wlist[i]["ID"]:
                find = 1
                loc = i
                break
        if find == 1:
            oldPasswd = input("请输入旧密码：")
            if wlist[loc]['passwd'] == oldPasswd:
                passwd = input("请输入新的密码：")
                wlist[loc]['passwd'] = passwd
                print("修改成功！")
                saveFilePasswd(path, wlist)
                match sel:
                    case 1:
                        menuStu()
                    case 2:
                        menuTech()
                    case 3:
                        menuRoot()
            else:
                print("您输入的密码有误!\n")
                print("请重试!\n")
                modifyPasswd(path, wlist, sel)
        else:
            print("您输入的用户不存在！")
            sel1 = eval(input("输入1重新进行修改"))
            if sel1 == 1:
                match sel:
                    case 1:
                        modifyPasswd(file_path_passwd_stu, passwdListStu, 1)
                    case 2:
                        modifyPasswd(file_path_passwd_tech, passwdListTech, 2)
                    case 3:
                        modifyPasswd(file_path_passwd_root, passwdListRoot, 3)
            else:
                match sel:
                    case 1:
                        menuStu()
                    case 2:
                        menuTech()
                    case 3:
                        menuRoot()
    except ValueError as ve:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(ve)}")
        modifyPasswd(path, wlist, sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        modifyPasswd(path, wlist, sel)


# 管理员可以增加新的学生用户和老师用户
def rootAppendUser():
    try:
        sel = eval(input("请输入被添加人的身份：1.学生，2.老师："))
        if sel == 1:
            appendUser(file_path_passwd_stu, passwdListStu)
        elif sel == 2:
            appendUser(file_path_passwd_tech, passwdListTech)
    except ValueError as e1:
        print(f"输入无效，请输入一个数字。错误信息：{str(e1)}")
        rootAppendUser()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        rootAppendUser()


# 添加用户
def appendUser(path, wlist):
    try:
        userID = input("请输入用户名：")
        # 添加学生信息之前先判断学生是否已经存在
        for i in wlist:
            if i["ID"] == userID:
                print("该用已经存在，不可添加!")
                break
        else:
            passwd = input("请输入用户的密码：")
            wlist.append({"ID": userID, "passwd": passwd})
            saveFilePasswd(path, wlist)
            print("添加成功！")
            sel1 = eval(input("输入1继续进行添加，否则返回上一级！"))
            if sel1 == 1:
                rootAppendUser()
            else:
                menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        appendUser(path, wlist)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        appendUser(path, wlist)


# 查询所有学生的信息
def displayStudents():
    try:
        print(f"学号------姓名----手机号-------邮箱-------Python--数据库---物联网技术-总成绩")
        for student in studentsList:
            print((f"{student['studentID']}\t {student['name']} \t{student['number']}\t "
                   f"{student['email']} \t{student['pythonScore']} \t\t{student['databaseScore']}\t\t "
                   f"{student['IOTScore']} \t{student['sumScore']}\n"))
    except Exception as e:
        print(f"发生异常: {str(e)}")
        displayStudents()


# 添加新的学生
def appendStudent(sel):
    try:
        studentID = input("请输入学生的学号：")
        # 添加学生信息之前先判断学生是否已经存在
        for i in studentsList:
            if i["studentID"] == studentID:
                print("该学生已经存在，不可添加!")
                print("如果想要修改该学生的信息，请输入1，输入其他则返回主页面:")
                flag = int(input())
                if flag == 1:
                    modifyStudent()
                    break
                else:
                    break
        else:
            name = input("请输入学生的姓名：")
            number = input("请输入学生的手机号：")
            email = input("请输入学生的邮箱:")
            pythonScore = input("请输入学生的Python程序设计成绩:")
            databaseScore = input("请输入学生的数据库成绩:")
            IOTScore = input("请输入学生的物联网技术成绩:")
            sum1 = int(pythonScore) + int(databaseScore) + int(IOTScore)
            sumScore = str(sum1)
            studentsList.append(
                {"studentID": studentID, "name": name, "number": number, "email": email, "pythonScore": pythonScore,
                 "databaseScore": databaseScore, "IOTScore": IOTScore, "sumScore": sumScore})
            print("添加成功！")
            sel1 = eval(input("输入1继续进行添加，否则返回上一级！"))
            if sel1 == 1:
                appendStudent(sel)
            else:
                match sel:
                    case 2:
                        menuTech()
                    case 3:
                        menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        appendStudent(sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        appendStudent(sel)


# 修改学生信息
def modifyStudent(sel):
    try:
        studentID = input("请输入要修改的学生的学号：")
        find = 0
        for i in studentsList:
            if i["studentID"] == studentID:
                find = 1
                print("1。修改姓名，2.修改手机号，3.修改邮箱")
                print("4。修改Python程序设计成绩，5.修改数据库成绩，6.修改物联网技术成绩。")
                print("输入0退出修改！")
                while True:
                    flag = int(input("请输入要修改的选项："))
                    match flag:
                        case 0:
                            break
                        case 1:
                            name = input("请输入学生的姓名：")
                            i["name"] = name
                        case 2:
                            number = input("请输入学生的手机号：")
                            i["number"] = number
                        case 3:
                            email = input("请输入学生的邮箱:")
                            i["email"] = email
                        case 4:
                            pythonScore = input("请输入学生的Python程序设计成绩:")
                            i["pythonScore"] = pythonScore
                        case 5:
                            databaseScore = input("请输入学生的数据库成绩:")
                            i["databaseScore"] = databaseScore
                        case 6:
                            IOTScore = input("请输入学生的物联网技术成绩:")
                            i["IOTScore"] = IOTScore
        if find == 0:
            print("该学生不存在！")
        sel1 = eval(input("输入1继续进行修改，否则返回上一级！"))
        if sel1 == 1:
            modifyStudent(sel)
        else:
            if sel == 2:
                menuTech()
            elif sel == 3:
                menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        modifyStudent(sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        modifyStudent(sel)


# 查单个学生信息
def showStudent(sel):
    try:
        studentID = input("请输入要查询的学生的学号：")
        find = 0
        for student in studentsList:
            if student["studentID"] == studentID:
                find = 1
                print(f"学号------姓名----手机号-------邮箱-------Python--数据库---物联网技术-总成绩")
                print((f"{student['studentID']}\t {student['name']} \t{student['number']}\t "
                       f"{student['email']} \t{student['pythonScore']} \t\t{student['databaseScore']}\t\t "
                       f"{student['IOTScore']} \t{student['sumScore']}\n"))
        if find == 0:
            print("您查找的学生不存在！")
        sel1 = eval(input("输入1继续进行修改，否则返回上一级！"))
        if sel1 == 1:
            showStudent(sel)
        else:
            match sel:
                case 2:
                    menuTech()
                case 3:
                    menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        showStudent(sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        showStudent(sel)


# 删除原有学生的信息记录
def deleteStudent():
    try:
        studentID = input("请输入要删除的学生的学号：")
        find = 0
        # 删除后列表长度会减少，循环的索引可能会超过新的长度，
        # 倒序循环防止索引错位
        for i in range(len(studentsList) - 1, -1, -1):
            if studentsList[i]["studentID"] == studentID:
                find = 1
                del studentsList[i]
                print("删除成功！")
                in1 = int(input("继续删除请输入1，否则返回主菜单："))
                if in1 == 1:
                    deleteStudent()
                else:
                    menuRoot()
        if find == 0:
            print("您要删除的学生不存在！")
            in1 = int(input("输入1继续进行删除，否则返回主菜单："))
            if in1 == 1:
                deleteStudent()
            else:
                menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        deleteStudent()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        deleteStudent()


# 输出单个学生的成绩
def showStudentScore(sel):
    try:
        studentID = input("请输入要查询的学生的学号：")
        find = 0
        for i in studentsList:
            if i["studentID"] == studentID:
                find = 1
                print(f"Python程序设计的成绩是：{i['pythonScore']}")
                print(f"数据库的成绩是：{i['databaseScore']}")
                print(f"物联网技术的成绩是：{i['IOTScore']}")
        if find == 0:
            print("您查找的学生不存在！")
        sel1 = eval(input("输入1继续进行查询，否则返回上一级！"))
        if sel1 == 1:
            showStudentScore(sel)
        else:
            match sel:
                case 2:
                    menuTech()
                case 3:
                    menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        showStudentScore(sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        showStudentScore(sel)


# 输出指定成绩的最高分和平均分
def showSubjectScore(sel):
    try:
        pythonScoreList = []
        databaseScoreList = []
        IOTScoreList = []
        pythonScoreSum = 0
        databaseScoreSum = 0
        IOTScoreSum = 0
        # 将所有人各科的成绩拿出来转换为整型放到一个列表里
        for i in studentsList:
            pythonScoreList.append(int(i["pythonScore"]))
            databaseScoreList.append(int(i["databaseScore"]))
            IOTScoreList.append(int(i["IOTScore"]))
        # 分别求和
        for i in pythonScoreList:
            pythonScoreSum = pythonScoreSum + i
        for i in databaseScoreList:
            databaseScoreSum = databaseScoreSum + i
        for i in IOTScoreList:
            IOTScoreSum = IOTScoreSum + i
        print("1。Python程序设计，2.数据库，3.物联网技术")
        print("输入0退出查询！")
        while True:
            flag = int(input("请输入要查询的科目："))
            match flag:
                case 0:
                    break
                case 1:
                    print(
                        f"Python程序设计的最高分是：{max(pythonScoreList)}分，平均分是：{round(pythonScoreSum / len(pythonScoreList), 2)}")
                case 2:
                    print(
                        f"数据库的最高分是：{max(databaseScoreList)}分，平均分是：{round(databaseScoreSum / len(databaseScoreList), 2)}")
                case 3:
                    print(
                        f"物联网技术的最高分是：{max(IOTScoreList)}分，平均分是：{round(IOTScoreSum / len(IOTScoreList), 2)}")
        sel1 = eval(input("输入1继续进行查询，否则返回上一级！"))
        if sel1 == 1:
            showSubjectScore(sel)
        else:
            match sel:
                case 2:
                    menuTech()
                case 3:
                    menuRoot()
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        showSubjectScore(sel)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        showSubjectScore(sel)


# 输出总分排名
def rankStudents():
    try:
        rankNum = 0
        print(f"学号------姓名---Python------数据库---物联网技术-总成绩--排名")
        newList = sorted(studentsList, key=lambda x: x["sumScore"], reverse=True)
        for student in newList:
            rankNum +=1
            print((f"{student['studentID']}\t {student['name']} \t "
                   f"{student['pythonScore']} \t\t{student['databaseScore']}\t\t "
                   f"{student['IOTScore']} \t{student['sumScore']}\t\t{rankNum}\n"))
    except Exception as e:
        print(f"发生异常: {str(e)}")
        rankStudents()


# 学生查看自己的个人信息
def queryStu():
    try:
        for student in studentsList:
            if student["studentID"] == user:
                print(f"学号------姓名----手机号-------邮箱-------Python--数据库---物联网技术-总成绩")
                print((f"{student['studentID']}\t {student['name']} \t{student['number']}\t "
                       f"{student['email']} \t{student['pythonScore']} \t\t{student['databaseScore']}\t\t "
                       f"{student['IOTScore']} \t{student['sumScore']}\n"))
    except Exception as e:
        print(f"发生异常: {str(e)}")
        queryStu()


# 学生查询本人成绩
def queryScore():
    try:
        for student in studentsList:
            if student["studentID"] == user:
                print(f"学号------姓名----Python--数据库---物联网技术-总成绩")
                print((f"{student['studentID']}\t {student['name']} \t "
                       f"{student['pythonScore']} \t\t{student['databaseScore']}\t\t "
                       f"{student['IOTScore']} \t{student['sumScore']}\n"))
                break
    except Exception as e:
        print(f"发生异常: {str(e)}")
        queryScore()


# 学生修改本人信息
def modifyStuPerson():
    try:
        for i in studentsList:
            if i["studentID"] == user:
                print("1。修改姓名，2.修改手机号，3.修改邮箱")
                print("输入0退出修改！")
                while True:
                    flag = int(input("请输入要修改的选项："))
                    match flag:
                        case 0:
                            break
                        case 1:
                            name = input("请输入学生的姓名：")
                            i["name"] = name
                        case 2:
                            number = input("请输入学生的手机号：")
                            i["number"] = number
                        case 3:
                            email = input("请输入学生的邮箱:")
                            i["email"] = email
        print("修改成功！")
    except ValueError as e1:
        print(f"输入无效，请输入一个有效的值。错误信息：{str(e1)}")
        modifyStuPerson()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        modifyStuPerson()


# 保存修改
def saveFileStu():
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"学号	姓名	手机号	          邮箱           Python     数据库     物联网技术  总成绩\n")
            for student in studentsList:
                file.write(f"{student['studentID']}\t {student['name']} \t{student['number']}\t "
                           f"{student['email']} \t{student['pythonScore']} \t{student['databaseScore']}\t "
                           f"{student['IOTScore']} \t{student['sumScore']}\n")
    except IOError:
        print("Error: 没有找到文件或读取文件失败!")
        saveFileStu()
    except Exception as e:
        print(f"发生异常: {str(e)}")
        saveFileStu()


# 密码保存
def saveFilePasswd(path, wlist):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(f"ID\t密码\n")
            for i in wlist:
                file.write(f"{i['ID']}\t {i['passwd']}\n")
    except IOError:
        print("Error: 没有找到文件或读取文件失败!")
        saveFilePasswd(path, wlist)
    except Exception as e:
        print(f"发生异常: {str(e)}")
        saveFilePasswd(path, wlist)


print("欢迎使用学生成绩管理系统")
readFile()
init()
