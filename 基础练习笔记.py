import fileinput
import time

print("hello world ")
print("你好，世界")
print("你好，世界")
print("你好，世界")

"""
print("你好，世界")
print("你好，世界")
"""

# 整数
print(666)
# print(13.14)

rmb = 30
print("余额:",rmb)

# 买了冰淇淋，花了10元
rmb = rmb - 10
print("买了冰淇淋后，余额为:",rmb,"元")


# 在print语句中，直接输出类型信息
print(type("你好，生活"))
print(type(123))
print(type(3.14))

fen_ge_fu = "~~~~~~~~~~~~~~~~~~~~~"
print(fen_ge_fu)

# 用变量存储type()的结果
this_is_001 = type("你好")
this_is_002 = type("12345")
this_is_003 = type("3.141")
print(this_is_001)
print(this_is_002)
print(this_is_003)

# 查看变量中存储的数据类型
name = "你好，world"
this_is_004 = type(name)
print(this_is_004)

print(fen_ge_fu)

# 讲数字类型转换成字符串
num_str = str(12345)
print(type(num_str))
print(fen_ge_fu)
float_int = int(3.14)
print(type(float_int))

print(fen_ge_fu)

# 要将字符串转为数字或者浮点数，必须要求字符串里的内容是数字，汉子不行

num3 = int("1223")
print(type(num3),num3)


num2 = float("333")
print(type(num2),num2)

# 命名规则
# 一、 只能使用 中文、英文、数字、下划线
# 1_name = "张三"
_name = "张三"
name_1 = "李四"
# 二、 大小写敏感
Mask = "马斯克"
mask = "马萨卡"
print(Mask)
print(mask)
# 三、不可以使用关键字




a = 1
b = 0
while b <= 8:
    b += 1
    while a < b:
        print(f"{a}*{b}={a*b}\t" ,end='')
        a += 1
    if a == b:
        print(f"{a}*{b}={a*b}")
        a = 1

print(fen_ge_fu)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print('欢迎来到黑马儿童游乐场(园)，儿童免费，成人收费')
# 一个变量后面要用到
age = int(input('请输入你的年龄：'))

if age >= 18:
    # 如果年龄是18以上岁，输出一下内容
    print('您已成年，游玩需要补票10元。')
    print('祝你游玩愉快！')

else:
    #如果不是，输出以下结果
    print('欢迎小朋友来玩，结束还送python C++ C语言 java web前端 HTML linux等等编程教学')
    print('祝你游玩和学习编程更加愉快')
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 算术运算
print("1+1=",1+1)
print("3-1=",3-1)
print("6*2=",6*2)
print("6/2=",6/2)
print("16//3=",16//3)  #取整数
print("9%2=",9%2)    # 取余数
print("3**4=",3**4)  # 指数

# 用变量接收它
name = """你好"""
name = """你
在
干啥
哦"""

"""你好"""
name2 = '你好'
name3 = "你好"
print(name,type(name))
print(name2)
print(name3)


# 字符串三种定义方式
# 在字符串内，包含单引号
name = " 你好、 ‘生活’ "
# 在字符串内，包含双引号
name2 = ' 你好、 ‘生活 '
# 使用转义字符\ ，解除引号的作用
name7 = "   \"你好，生活    \"    \" "

# 字符串拼接
print("你好" + "生活")
# 字符串字面量 和字符串变量的拼接
name11 = "马斯克"
address = "美国"
doing = "造火箭"
tell = "123456"
print("我是" + name11 + ",我在" + address + ",正在" + doing + "，我的电话是" + tell)
# 只能相同字符串类型的才能拼接，不同类型的不得行
name11 = '111'
address = '222'
doing = '333'
tell = '444'
print("我是" + name11 + ",我在" + address + ",正在" + doing + "，我的电话是" + tell)


# 字符串格式化,
who = "马斯克"
message = "在造火箭的是  %s " % who   # %s 占位 ,% 去补全变量，按顺序
print(message)

"""
 % 表示：我要占位
 s 表示： 将变量 变成字符串放入占位的地方
 %s  表示: 将内容转换成 字符串，放入占位位置
 %d  表示: 将内容转换成 整数，  放入占位位置
 %f  表示: 将内容转换成 浮点型，放入占位位置
"""


# 通过占位的形式，完成数字和字符串的拼接
class_room = 6
avg_grade = 95
message2 = " 英语学科，高三 %s班，考试的平均成绩是 %s " % (class_room,avg_grade)   # %s 占位 ,% 去补全变量，按顺序
print(message2)
# 练习(1)
name001 = "马斯克"
setup_year = 2023
time_huo = 11.28
message3 = "%s ，在 %d 年,早上 %f 分，发射火箭" % (name001,setup_year,time_huo)
print(message3)
print(fen_ge_fu)
# 练习(2)
# f"{占位}"
# f"{变量}{变量}" 的方式进行快速格式化
# 这种方式，① 不理会类型 ②不做精度控制，适合对精度没有要求的时候快速使用
name001 = "马斯克"
setup_year = 2023
time_huo = 11.28
# f: format
print(f"{name001},在{setup_year}年，早上{time_huo}分，发射火箭")




"""
字符串数字精度控制
 m 控制宽度，
 .n 控制小数点精度，要求是数字，会进行小数的四舍五入
 
例子：
%5d:表示将整数的宽度控制在5位，如数字11，被设置为5d，就会变成:  [空格][空格][空格] 11  ，用三个空格补足宽度。

%5.2f: 表示将宽度控制为5，将小数点精度设置为2小数点和小数部分也算入宽度计算。
如，对11.34567设置了%7.2f 后，结果是:[空格][空格]11.35。2个空格补足宽度，小数部分限制2位精度后，四舍五入为 .35
"""

# 表达式的格式化
# 表达式：一条具有 明确执行结果 的代 码语句
# 如 1+1、5*2,就是表达式，有具体的结果，结果是一个数字。   name=“张三”  age=11+11 也是的，具体结果传给变量
print("1+1的结果是：%d" % (1+1))
print(f"1+2的结果是：{1+2}")
print("字符串在Python中的类型是：%s" % type('字符串'))
# f"{表达式}"
# "%s 或者 %d 或者 %f   % (表达式、表达式、表达式)
"""
练习
stock_name ，公司名字
stock_price ，当前股价
stock_code ，股票代码
stock_price_daily_growth_factor ，股票每日增长系数，浮点类型，比如1,2 
growth_days ,增长天数
计算，经过growth_days 天的增长后，股票达到了多少钱
使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数。

示例： 公司：特斯拉 ，股票代码：123456 ，当前股价 66.77    ---使用f"{变量}"的方式输出
      每日的增长系数是：1.2 ，经过七天后的增长后，股票达到了：123.45   ---使用% 占位符的方式输出
"""

stock_name = "tesl"
stock_price = 66.77
stock_code = 123456
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price*stock_price_daily_growth_factor*growth_days
print(f"公司：{stock_name},股票代码：{stock_code},当前的股价：{stock_price}")
print("每日的增长系数是: %s ,经过了 %d 天增长后，股票到达了： %.2f " % (stock_price_daily_growth_factor,growth_days,finally_stock_price))



# input 语句
"""
print("请输入你的名字")
name = input()
print("欢迎 %s ，来到我的世界" % name)
# 或者
name = input("请输入你的名字")
print("欢迎 %s ，来到我的世界" % name)
"""
"""
# 输入数字类型
num = input("请告诉我，你的银行卡密码：")
num = int(num)
print("你的银行卡密码类型是： ",type(num))
"""
"""
# 练习：
user_name = input("请输入你的昵称")
user_type = input("请输入你的会员等级")
print(f"{user_name},你好，你的等级是{user_type}，欢迎来到我的世界")
"""

# 布尔类型

result = 10 > 5
print(f"10>5的结果是：{result},类型是：{type(result)}")

result = "xiaoming" == "xiaozhang"
print(f"字符串xiaoming是否和xiaozahng相同，结果是：{result},类型是：{type(result)}")

num1 = 10
num2 = 20
print(f"10 == 10 的结果是：{num1==num2}")
num1 = 10
num2 = 20
print(f"10 != 10 的结果是：{num1!=num2}")

name1 = "zhangsan"
name11 = "lisi"
print(f"zhangsan == lisi 结果是： {name1 == name11}")

num1 = 10
num2 = 5
print(f"10>5的结果是: {num1 > num2}")
num1 = 10
num2 = 5
print(f"10<5的结果是: {num1 < num2}")




# if 语句
""" 
age = input("请输入你的年龄")
age = int(age)
# age = int(input("请输入你的年龄"))
if age >= 18:
    print("你已经成年了")
# if age < 18:
else:
    print("未成年")
"""

# age = int(input("请输入你的年龄"))
# if 18 <= age < 60:
#     print("你已经成年了")
# elif age >= 60:
#     print("你老了")
# else:
#     print("未成年")


# 公司发礼物，条件 ①和② 同时满足
# ① 年龄18~~30之间
# ② 入职时间大于2年，或者等级大于3
# age = int(input("请输入你的年龄"))
# year = int(input("请输入你的入职时间"))
# level = int(input("请输入你的等级"))
# # 通过缩进嵌套
# if age >= 18:
#     print("成年人符合")
#     if age < 30:
#         print("年龄达标")
#         if year > 2:
#             print("入职时间达标，可以领取")
#         # else:
#         #     print("年龄达标，入职时间不足，不能领取")
#         elif level > 3:
#             print("等级达标，可以领取")
#         else:
#             print("等级和入职时间不够，不能领取")
#     else:
#         print("年纪超过30，不能领取")
# else:
#     print("未成年不能领取")




# # 猜数字
# # 构造一个随机数字
# import random
# num = random.randint(1 , 10)
# guess_num = int(input("请输入猜测数字"))
# # 通过if判断语句进行数字的猜测
# if guess_num == num:
#     print("第一次猜对了")
# else:
#     if guess_num > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#
#     guess_num = int(input("再次输入猜测数字"))
#
#     if guess_num == num:
#         print("第二次猜对了")
#     else:
#         if guess_num > num:
#             print("第二次猜大了")
#         else:
#             print("第二次猜小了")
#
#         guess_num = int(input("再次输入猜测数字"))
#
#         if guess_num == num:
#             print("第三次猜对了")
#         else:
#             print("三次机会用完了")



# 一、while循环
i = 0
while i < 10:
    print("小美，我喜欢你")
    i = i+1   # 终止条件

# 练习：求1-100的和
sum1 = 0
a = 1
while a <= 100:
    sum1 = sum1 + a
    a = a + 1
print(f"1累加到100的和是：{sum1}")





# # 二、猜数字
# import random
# num = random.randint(1,100)
#
# # 记录猜了多少次
# count = 0
# # 通过布尔类型变量，做循环是否继续标记
# biaoji = True
# while biaoji:
#     guess_num = int(input("请输入你猜的数字"))
#     count = count + 1
#     if guess_num == num:
#         print("猜中了")
#         print(f"一共猜了{count}次")
#         # 设置为false，就是终止循环
#         biaoji = False
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#
#





# while 循环嵌套,使用空格缩进
# 外层循环
i = 1
while i < 100:
    print(f"今天是第{i}天，准备表白...")
    i = i + 1

    # 内存循环
    j = 0
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j = j+1
    print("小美，我喜欢你")
print(f"坚持到{i}天，表白成功")



# # 换行
# print("Helloo")
# print("World")
# # 不换行
# print("Hello",end='')
# print("world",end='')

print("Hi\t\tWind")

print("Hello\tWorld")


# # 通过while循环，输出久久乘法表

# 外循环
# 控制行的循环 i <=9
# 控制每一行的输出结果，循环 ， j <= i
i = 1  # 控制行的循环
while i <= 9:
    # 内循环
    j = 1
    while j <= i:  # 控制每一行输出的循环
        print(f"{j}*{i}={j*i}\t",end='')  # \t 对齐，end 不换行
        j = j+1
    i = i+1     # 退出内循环，进行外循环
    print()  # 换行作用



# for 循环
# name = "sangfor"
# for x in name:
#     print(x)

# 统计有多少a字母
name = "sangfor is security corporation"
# 定义一个变量，统计有多少a
count = 0

# for 循环统计
# for 临时变量 in 统计的数据
for x in name:
    if x == "s":
        count = count +1
print(f"有{count}个s")

# range(5) 取得的数据是: [0,1,2,3,4]
# range(num1,num2)
# range(5,10) 取得是数据是： [5,6,7,8,9]
# range(num1,num2,step) 步长默认为1
# range(5,10,2) 取得的数据是： [5,7,9]
for x in range(10):
    print(x)
for x in range(5,10):
    print(x)
for x in range(5,20,3):
    print(x)

print(fen_ge_fu)

count = 0
for num in range(1,101):
    if num % 2 == 0 :
        count = count + 1
print("1-100之间，偶数个数为：",count)


# for 循环的作用域
# for x in range(6):
#     print(x)   # x只在for内部生效
# print(x)     # x只在for内部生效
# 如果要在for外部访问临时变量，需要在for之前定义变量
x = 0
for x in range(6):
    print(x)   # x只在for内部生效
print(x)     # x只在for内部生效



# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print()



# 循环中断，continue 与 break
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")
print("语句3")

print(fen_ge_fu)

for i in range(1,6):
    print("语句1")
    break
    print("语句2")
print("语句3")
print(fen_ge_fu)
for i in range(1,5):
    print("语句1")
    for j in range(1,3):
        print("语句2")
        continue
        print("语句3")
print("语句4")

print(fen_ge_fu)

for i in range(1,5):
    print("语句1")
    for j in range(1,3):
        print("语句2")
        break
        print("语句3")
print("语句4")


# 练习
money = 10086
for i in range(1,100):
    import random
    score = random.randint(1,10)

    if score < 5 :
        print(f"员工{i}的绩效分是{score},不满足发工资条件")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}满足条件，发1000工资")
    else:
        print(f"余额{money}，不足1000，下个月发")
        break


# 函数 len 统计长度
name = "helloworld"
length = len(name)
print(length)
# # 函数的定义
# def 函数名（传入参数）:
#     函数体
#     return 返回值
# 函数的调用：
# 函数名（参数）


# 定义函数
def say_hi():
    print("Hi,我是马斯克")
# 调用函数
say_hi()

# 练习
def add(x,y):
    result = x + y
    print(f"{x}+{y}的结果是：{result}")

add(22,199)
add(5,66)

def check_hs(num):
    print("欢迎来到大学，请出示你的健康码，测量体温")
    if num <= 37.5:
        print(f"你的温度是{num},请进")
    else:
        print(f"你的体温是{num}，隔离")

check_hs(39)
check_hs(36)
check_hs(36.8)

# 函数的返回值
def add_1 (a,b):
    result = a +b
    return result

r = add_1(6,66)
r2 = add_1(3,6)
print(r,r2)


def say_hello():
    print("你好呀")
result = say_hello()
print(f"无返回值，返回的内容是：{result}")
print(f"返回的内容类型是：{type(result)}")

# 函数嵌套
def fun_b():
    print("--2--")

def fun_a():
    print("--1--")
    fun_b()   # 嵌套函数b
    print("--3---")
# 调用函数a
fun_a()


# 局部变量、全局变量

#局部变量
def test_a():
    num66 = 100   # 局部变量在函数体内部，在外访问则报错
    print(num66)

test_a()  # 100
# print(num66) #报错： num 找不到

# 全局变量
num22 = 200   # 定义在函数的外面

def test_aa():
    print(num22)

def test_bb():
    print(num22)  # 访问全局变量num22

test_aa()
test_bb()
print(num22)



# 在函数内修改全局变量
num22 = 55   # 定义在函数的外面
def test_aa():
    print(num22)
def test_bb():
    num22 = 66
    print(num22)  # 访问全局变量num22
test_aa()
test_bb()
print(num22)

# global 关键字
num22 = 333333
def test_aa():
    print(num22)
def test_bb():
    global num22   # global 声明全局变量
    num22 = 555555
    print(num22)  # 访问全局变量num22
test_aa()
test_bb()
print(num22)

print(fen_ge_fu)
# # 练习
# money = 1000000
# name = None
# name = input("请输入你的姓名")
# # 查询余额
# def query(show_header):
#     if show_header:
#         print("-----查询余额-----")
#     print(f"{name},你好，你的余额剩余：{money}元")
# # 存款
# def saving(num):
#     global money
#     money += num
#     print("-----存款-----")
#     print(f"{name},你好，存款：{money}元，成功")
#     # 调用query函数，查询余额
#     query(False)
# # 取款
# def get_money(num):
#     global money
#     money -= num
#     print("---取款---")
#     print(f"{name},你好，取款：{money}元，成功")
#     query(False)
#
# # 定义主菜单函数
# def main():
#     print("-----主菜单-----")
#     print(f"{name},你好，欢迎来到马斯克银行，请选择操作")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入你的选择：")
# # 设置循环，确保程序不退出
# while True:
#     keyword_input = main()
#     if keyword_input == "1":
#         query(True)
#         continue
#     elif keyword_input == "2":
#         num = int(input("你要存多少钱？请输入："))
#         saving(num)
#         continue
#     elif keyword_input == "3":
#         num = int(input("你要取多少钱？请输入："))
#         get_money(num)
#         continue
#     else:
#         print("程序退出")
#         break
print(fen_ge_fu)





# 容器
# 定义一个列表 list
name_all = ['张三','李四','王麻子','张杰','林俊杰','王菲',123,111,'mask']
print(name_all)
print(type(name_all))
# 下标索引
print(name_all[0])
print(name_all[1])
print(name_all[2])

print(name_all[-1])
print(name_all[-2])
print(name_all[-3])

num_list = [[1,2,3],[5,6,7]]
print(num_list)
print(type(num_list))
print(num_list[1][2])  # 取7 ，嵌套

# 函数的常用操作方法
# 1、查询下标
mylist = ['张三','李四','王麻子']
index = mylist.index("张三")
# index2 = mylist.index("hello")
print(f"张三在列表中的下标索引值是：{index}")
# print(f"张三在列表中的下标索引值是：{index2}")

# 2、修改特定下标索引值
mylist[0] = "法外狂徒"
print(f"列表被修改元素后，结果为：{mylist}")

# 3、插入元素
mylist.insert(1,"罗翔")
print(f"列表插入元素后：{mylist}")

# 4、追加元素
mylist.append("法学")
print(f"追加元素后：{mylist}")
# 追加一批元素
mylist.extend(["zs","ls","wmz"])
print(mylist)

# 5、删除
del mylist[2]
print(f"删除元素后：{mylist}")
# 删除2
element = mylist.pop(1)
print(f"pop取出后元素后：{mylist},取出的元素是:{element}")
# 删除3
mylist.remove("王麻子")
print(mylist)

# 清空列表
mylist.clear()
print(mylist)

# 统计列表内某元素的个数
mylist = ['张三','李四','王麻子',"张三","法外狂徒","张三","法外狂徒","法外狂徒"]
count = mylist.count("法外狂徒")
print(count)

# 统计列表内，有多少个元素
count = len(mylist)
print(f"一共有{count}个元素")

# while循环遍历列表
def lis_while_func():
    my_list = ['张三', '李四', "法外狂徒"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表元素：{element}")
        index += 1
lis_while_func()

print(fen_ge_fu)

# for循环遍历
def list_for_func():
    my_list = ['张三', '李四', "法外狂徒","张三","李四"]
    for element in my_list:
        print(f"列表的元素有:{element}")
list_for_func()

# 练习 ：统计一个列表中的偶数
def list_even_num_func():
    count = 0
    list_even = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in list_even:
        if num % 2 == 0:
            count += 1
    print(f"偶数有{count}个")
list_even_num_func()


# 元组
t1 = (1,"张三",True,mask)
t2 = ()
t3 =tuple()
t4 = ("张三")    #不写逗号，就是str类型
t5 = ("张三",)
print(type(t1),t1)
print(type(t2),t2)
print(type(t3),t3)
print(type(t4),t4)
print(type(t5),t5)

# 嵌套
t6 = ((1,2,3),(4,5,6))
print(type(t6),t6)
num = t6[1][2]
print(f"前天中取出的元素是：{num}")

# index 查找方法
t7 = ("张三","李四","法外狂徒","法外狂徒","法外狂徒","法外狂徒","法外狂徒")
index = t7.index("法外狂徒")
print(f"在t7中查找的元素是：{index}")
# 统计某元素个数
num = t7.count("法外狂徒")
print(f"法外狂徒在t7中的个数：{num}")
# 元素数量
len_t7 = len(t7)
print(f"t7元素中，一共有{len_t7}个元素")
# 元素遍历 while
index = 0
while index < len(t7):
    print(f"元组的元素有：{t7[index]}")
    index += 1
# 元素遍历 for
for element in t7:
    print(f"for元组的元素有：{element}")
# 不可修改
# t7[1] = "马斯克"
# 但可以修改嵌套内的list里的内容
t8 = (1,2,3,["张三","法外狂徒"])
print(t8)
t8[3][0] = "zs"
t8[3][1] = "fwkt"
print(t8)



# 字符串
my_str = "mynameismask"
value = my_str[2]
value2 = my_str[-6]
print(value,value2)
# 修改
new_str = my_str.replace("mask","xiuyuan")
print(f"将字符串{my_str}进行替换后得到{new_str}")
# 分割
my_list = "hello i am mask"
new_str = my_list.split(" ")  # 按照空格切分
print(f"将{my_list}切分后的字符串{new_str}")
# strip 方法
my_list = "  my name is mask   "
new_list = my_list.strip(" ")  # 去除前后空格
print(f"将{my_list}进行strip 后：{new_list}")
# strip 方法2
my_list = "12my name is mask121211"
new_list = my_list.strip("12")  # 去除1、2
print(f"将{my_list}进行strip 后：{new_list}")

# 序列和切片
my_list = [0,1,2,3,4,5,6,]
result1 = my_list[1:3]  # 起始为1，到3结束，默认步长为1
print(f"结果1为：{result1}")

my_list = [0,1,2,3,4,5,6,]
result2 = my_list[:]  # 起始和结束不写，表示从头到尾
print(f"结果2为：{result2}")

my_str = "1234567"
result3 = my_str[::2]  # 步长为2
print(f"结果3为：{result3}")

# 集合
my_set = {"张三","李四","法外狂徒","法学","罗翔","法外狂徒","法外狂徒","法外狂徒","法外狂徒"}  # 集合去重，排列无序
my_set_empty = set()   # 空集合
print(f"my_set的内容：{my_set},类型是:{type(my_set)}")
print(f"my_set_empty空集合的内容：{my_set_empty},类型是:{type(my_set_empty)}")
# 添加新元素
my_set.add("马斯克")
print(my_set)
# 移除元素
my_set.remove("法外狂徒")
print(my_set)
# 随机取出一个元素
element = my_set.pop()
print(f"取出的元素是：{element},现在的元素有{my_set}")
# 清空
my_set.clear()
print(my_set)
# 取出两个集合中的差集，集合1中有的，集合2没有的
set1 = {1,2,3}
set2 = {1,2,5}
set3 = set1.difference(set2)
set4 = set2.difference(set1)
print(set1)
print(set2)
print(set3)
print(set4)
print(fen_ge_fu)
# 消除差集
set1 = {1,2,3}
set2 = {1,2,5}
set1.difference_update(set2)  # 在集合1内，删除和集合2 相同的元素，结果：集合1修改，集合2不变
set2.difference_update(set1)
print(set1)
print(set2)
# 合并
set1 = {1,2,3}
set2 = {1,2,5}
set3 = set1.union(set2)
print(f"2集合合并结果：{set3}")
# 统计元素数量
set1 = {1,2,3,4,5,1,2,3}
num = len(set1)
print(num)
# for循环
set1 = {1,2,3,4,5,1,2,3}
for element in set1:
    print(element)














# 字典
# 键值对
# 字典字面量  {key:value,key:value,.....,key:value}
# 字典变量    my_dict = {key:value,key:value,.....,key:value}
# 空字典   my_dict = {}    或者    my_dict = dict()
my_dict1 = {"张三":66,"法外狂徒":70,"李四":88}
my_dict2 = {}
my_dict3 = dict()
print(f"字典1{my_dict1},类型:{type(my_dict1)}")
print(f"字典2{my_dict2},类型:{type(my_dict2)}")
print(f"字典3{my_dict3},类型:{type(my_dict3)}")
# 字典数据获取
stu_score = {"张三":66,"法外狂徒":70,"李四":88}
print(stu_score["张三"])
print(stu_score["李四"])
print(stu_score["法外狂徒"])
# 嵌套字典
stu_score_dict0 = {
    "张三":{}, "李四":{}, "法外狂徒":{}
}
# 在补全
stu_score_dict = {
    "张三": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    },
    "李四": {
        "语文": 71,
        "数学": 97,
        "英语": 21,
    },
    "法外狂徒": {
        "语文": 108,
        "数学": 121,
        "英语": 116,
    }
}
print(f"学生的考试信息: {stu_score_dict}")
# 从嵌套的字典里获取数据
# 查看张三的英语信息
score_zs = stu_score_dict["张三"]["英语"]
print(f"张三的英语分数：{score_zs}")
# 新增
stu_score2 = {"张三":66,"法外狂徒":70,"李四":88}
stu_score2["马斯克"] = 99
print(stu_score2)
# 删除
stu_score3 = {"张三":66,"法外狂徒":70,"李四":88}
value = stu_score3.pop("张三")
print(value)
print(stu_score3)
# 清空
stu_score4 = {"张三":66,"法外狂徒":70,"李四":88}
value = stu_score4.clear()
print(stu_score4)
# 获取全部key
stu_score5 = {"张三":66,"法外狂徒":70,"李四":88}
keys = stu_score5.keys()
print(f"字典的全部keys是：{keys}")

# 练习
info_dict = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 3
    }, "林俊杰": {
        "部门": "科技部",
        "工资": 6000,
        "级别": 1
    }, "刘德华": {
        "部门": "科技部",
        "工资": 7000,
        "级别": 2
    },
}
print(f"升职加薪前：{info_dict}")
# for 循环遍历字典
for name in info_dict:
    if info_dict[name]["级别"] == 1:
        # 获取员工信息
        employee_info_dict = info_dict[name]
        # 修改员工信息
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        # 更新信息
        info_dict[name] = employee_info_dict

print(f"升职加薪后：{info_dict}")



# 多个变量，接受多个返回值
def test_return():
    return 1,'hello',True

x,y,z = test_return()
print(x)
print(y)
print(z)

# 函数作为参数传递
def test_func(computer):
    result = computer(55,11)
    print(result)

def computer(x,y):
    return  x + y

test_func(computer)

# 函数作为参数传递
# lambda 匿名函数
def test_function(computer2):
    result = computer2(3,33)
    print(result)

test_function(lambda x, y:x + y)






# 文件读取
# 打开文件,文档不管用什么读取方法，都只会读取一次
# f = open("C:/Users/23189/Documents/001_note/ke_mu_1.txt","r",encoding="utf-8")
# print(type(f))

# read 读取
# print(f"读取10字节：{f.read(10)}")
# print(f"读取全部是：{f.read()}")
print("----------------------------------------------------")

# readLines 读取
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型是:{type(lines)}")
# print(f"lines对象的内容是:{lines}")

# readLine
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的数据是：{line1}")
# print(f"第二行的数据是：{line2}")
# print(f"第三行的数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行的数据是：{line}")

# 文件的关闭
# time.sleep(50000)    # 暂时运行500秒
# f.close()    # 关闭文件

# 对文件操作完成之后自动关闭
# with open("C:/Users/23189/Documents/001_note/ke_mu_1.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(f"每一行的数据：{line}")
#
# time.sleep(50000)

# f = open("C:/Users/23189/Documents/001_note/ke_mu_1.txt","r",encoding="utf-8")
# content = f.read()
# count = content.count("超速")
# print(f"超速在文件中出现了:{count}次")
# for line in f:
#     line = line.strip()  # 去除开头和结尾的空格及换行符
#     words = line.split(" ")
#     print(words)
#
# f.close()

# f = open("D:/001.txt","w",encoding="utf-8")
# f.write("hello , world ！！！")
# f.flush()  # 将内存中的内容写到硬盘中
# time.sleep(5000)
# f.close()  # 内置了flush
# f = open("D:/001.txt","a",encoding="utf-8")  # 追加
# f.write("\n好好学习，天天向上")
# f.close()


# # 练习
# fr = open("D:/bill.txt","r",encoding="utf-8")
# fw = open("D:/bill.txt.bak","w",encoding="utf-8")
# for line in fr:
#     line = line.strip()  # 清楚换行
#     if line.strip("，")[1] == "高速":
#         continue
#     fw.write(line)
#     fw.write("\n")
#
# fr.close()
# fw.close()



# 异常捕获 (1)
# f = open("D:/aaa.txt","r",encoding="utf-8")   # 文件不存在
# try:
#     f = open("D:/aaa.txt", "r", encoding="utf-8")
# except:
#     print("出现异常了，文件不存在，我现在将open的r改成w，去打开")
#     f = open("D:/aaa.txt", "w", encoding="utf-8")

# 异常捕获 (2)
# try:
#     print(name99999)
# except (NameError) as e:
#     print("出现异常了")

# 异常捕获 (2)
# try:
#     1 / 0
# except (NameError) as e:
#     print("出现异常了")

# 异常捕获 (2)
# try:
#     1 / 0
# except (NameError,ZeroDivisionError) as e:
#     print("出现异常了")

# 异常捕获 (2)
try:
    1 / 0
except Exception as e:   # Exception 顶级的异常，能够捕获所有的异常
    print("出现异常了")

# 异常捕获 (2)
try:
    f = open("D:/aaa.txt","r",encoding="utf-8")
except Exception as e:
    print("出现异常了,r改成w")
    f = open("D:/aaa.txt", "w", encoding="utf-8")
else:
    print("没有异常")
finally:                      # 不管有没有异常都会执行
    f.close()

print("-------------------------------------")

# 模块导入1
# import time   # ctrl + 鼠标左键，进入time函数
# print("你好")
# time.sleep(5)
# print("我也好")

# 模块导入2
# from time import sleep
# print("你好")
# sleep(5)
# print("我也好呀")

# 模块导入3
# from time import *
# print("你好")
# sleep(5)
# print("我好")

# 模块导入4
# import time as ttt  # as，取别名
# print("你好")
# ttt.sleep(5)
# print("我也好")

# 模块导入5
# from time import sleep as sl
# print("你好")
# sl(5)
# print("我也好呀")



# 导入自定义模块
# import my_mod1
# my_mod1.test(6, 66)

# from my_mod1 import test
# test(3,6)


import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()




# json
import json
data = [{"name":"张三","age":11},{"name":"李四","age":15},{"name":"罗翔","age":23}]
# 将字典转换为json
json_str = json.dumps(data,ensure_ascii=False)   # 不适用ASCII码转换：ensure_ascii=False
print(type(json_str))
print(json_str)
# 将json字符串 转换成  Python数据类型
s = '[{"name":"张二","age":11},{"name":"李五","age":15},{"name":"罗小翔","age":23}]'
l = json.loads(s)
print(type(l))
print(l)







# pyecharts 入门
from pyecharts.charts import Line
from pyecharts import options as opts
line_001 = Line()
line_001.add_xaxis(["中国","美国","英国"])
line_001.add_yaxis("GDP",[30,20,10])
line_001.set_global_opts(
    title_opts=opts.TitleOpts(title="GDP展示")

)

line_001.render()  # 将代码生成为图像



# from pyecharts.charts import Bar
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()






# 类，对象

# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
# 创建一个对象
stu_1 = Student()

# 对象属性赋值
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)






# 定义一个带有成员方法的类
class Student01:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，多多关照")

    def say_hi2(self,msg):
        print(f"大家好，我是{self.name}，{msg}")

stu01 = Student01()
stu01.name = "周杰伦"
stu01.say_hi2("哎呦，不错哦")

stu02 = Student01()
stu02.name = "林俊杰"
stu02.say_hi()


# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# 构建闹钟对象，并让其工作
clock1 = Clock()
clock1.id = "001"
clock1.price = 19.99
print(f"闹钟的ID:{clock1.id},价格：{clock1.price}")
clock1.ring()



# 连接数据库
from pymysql import Connection

conn = Connection(
    host="wyhhxx.cn",
    port=3306,
    user="root",
    password="123456"
)
print(conn.get_server_info())

conn.close()
























