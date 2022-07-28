import os
import ast
import json
import demjson

filename = 'students.txt'


def show_menu():
    print('=====================================')
    print('==========欢迎进入学生管理系统===========')
    print('0、退出')
    print('1、添加')
    print('2、删除')
    print('3、修改')
    print('4、排序')
    print('5、统计')
    print('6、显示所有信息')


def total():
    print('-----正在【统计】学生信息-----')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        if students:
            print('学生总数为: {0}'.format(len(students)))
        else:
            print('没有学生信息')
    else:
        print('文件不存在！！！')


def sort():
    print('-----正在【排序】学生信息-----')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        students_new = []
        for item in students:
            students_new.append(eval(item))
        if students_new:
            sort_mode = input('请输入生序排列->1，降序排列->2\n')
            # 输入不合法
            if sort_mode not in ['1', '2']:
                print('输入不合法')
                sort()
            reverse_tof = False
            if sort_mode == '2':
                reverse_tof = True
            # 排序操作
            students_new.sort(key=lambda x: x['id'], reverse=reverse_tof)
            # 显示排序结果
            for item in students_new:
                print(item)
        else:
            print('没有学生信息')
    else:
        print('文件不存在！！！')


def main():
    while True:
        show_menu()
        choice = int(input('请输入您的选择: '))
        if choice not in range(0, 7):
            print('没有这个选项，请重新选择！')
            continue

        if choice == 0:
            choice = input('您确定退出吗？y/n: ')
            if choice == 'y' or choice.lower() == 'y':
                break
            else:
                continue
        elif choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            modify()
        elif choice == 4:
            sort()
        elif choice == 5:
            total()
        elif choice == 6:
            show()


def add():
    print('-----正在【添加】学生信息-----')
    students = []
    while True:
        id = input('请输入id: ')
        if not id:
            break
        name = input('请输入name: ')
        if not name:
            print('输入的数据不能为空')
            continue
        try:
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入的数据有误')
            break
        students.append({'id': id, 'name': name, 'python': python, 'java': java})
        # students.append('\n')
        # 询问继续添加
        answer = input('是否继续添加信息？y/n\n')
        if answer == 'y':
            continue
        else:
            break
    # 保存学生数据
    save(students)


def save(students):
    # 判断是否存在文件
    # if not os.path.exists(filename):
    #     open(filename, 'a+')
    try:
        with open(filename, 'a+', encoding='utf-8') as flie:
            for item in students:
                flie.write(str(item) + '\n')
    except:
        raise IOError('保存数据出错！！！')


def delete():
    print('-----正在【删除】学生信息-----')
    while True:
        del_id = input('请输入要删除学生的id：\n')
        if del_id:
            # 获取原有的数据
            student_old = []
            del_flag = False
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
            if student_old != []:
                with open(filename, 'w+', encoding='utf-8') as wfile:
                    for item in student_old:
                        stu_dict = dict(eval(item))
                        if stu_dict['id'] != del_id:
                            wfile.write(str(stu_dict) + '\n')
                        else:
                            del_flag = True
                            print('成功删除id为{0}的学生'.format(del_id))
                if not del_flag:
                    print('没有找到id为{0}的学生'.format(del_id))
            else:
                print('没有学生数据！！')
                break
        answer = input('需要继续删除吗？y/n\n')
        if answer == 'y':
            continue
        else:
            break


def modify():
    print('-----正在【修改】学生信息-----')
    while True:
        # 判断有无文件
        if not os.path.exists(filename):
            print('学生信息文件不存在，无法进行修改操作')
            return
        # 存在文件则读取数据，判断有无学生数据
        student_old = None
        with open(filename, 'r', encoding='utf-8') as rf:
            student_old = rf.readlines()
        if student_old == []:
            print('没有学生数据，无法修改')
            break
        # 读取要修改的学生id
        id_modify = input('请输入要修改的学生id：\n')
        if not id_modify.isnumeric():
            print('请输入数字')
            continue
        # 判断id是否存在
        flag = False
        with open(filename, 'w+', encoding='utf-8') as wf:
            for item in student_old:
                item_dict = ast.literal_eval(item)
                if item_dict['id'] == id_modify:
                    # 存在，进行修改操作
                    print('存在ID为{0}的学生，可以进行性修改操作'.format(id_modify))
                    flag = True
                    name = input('请输入name：\n')
                    python = input('请输入python：\n')
                    java = input('请输入java：\n')
                    wf.write(str({'id': id_modify, 'name': name, 'python': python, 'java': java}) + '\n')
                else:
                    wf.write(str(item_dict) + '\n')
        if not flag:
            print('不存在ID为{0}的学生'.format(id_modify))
            break
        # 是否要继续修改


def show():
    print('-----正在【显示】学生信息-----')
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        if students:
            for item in students:
                print(item)
        else:
            print('没有学生信息！！！')
    else:
        print('文件不存在！！！')


if __name__ == '__main__':
    main()
    # d = {"id": 23, "name": "adam"}
    # dict_d = json.dumps(d)
    # print(dict_d)
    # print(type(dict_d))
