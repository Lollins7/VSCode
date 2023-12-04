# 二十四点
import os
from time import sleep
from time import perf_counter


global Goal, MaxAllowRetryNum, Count
Goal, MaxAllowRetryNum, Count = 24, 3, 0

# 输出程序相关信息


def ptintInfo():
    print('''" 经典 24 点 "'''.center(72, "="))
    print(" 请用户输入四个正整数值 ".center(64, "-"))
    print(" 单个数值提供三试错机会。若机会用完,程序倒计时5秒退出 ".center(50, "-"))
    print(" 将输出所有的24点方案,并对方案进行计数 ".center(58, "-"))
    print(" 若无方案,程序退出,输出0 ".center(65, "-"))


def printSatistics(times):
    print("一共有{}种方案".format(Count))
    print("共耗时{:.3f}ms".format(times*1000))

# 得到四个用户输入值


def getNumbers():
    a = getOneNumber("一")
    b = getOneNumber("二")
    c = getOneNumber("三")
    d = getOneNumber("四")
    print("输入的数值为:"+a+','+b+','+c+','+d)
    return a+' '+b+' '+c+' '+d

 # 得到单个用户输入值
 # 单个提供三次试错机会，（不包括第一次输入）
 # 试错机会用完后，程序倒计时五秒强制退出


def getOneNumber(temp):
    global MaxAllowRetryNum
    for tryies in range(MaxAllowRetryNum+1):
        num = input("请输入第{}个值:".format(temp))
        try:
            num = int(eval(num))
            if num > 0:
                break
            else:
                print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        except:
            print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        if tryies == MaxAllowRetryNum:
            for i in range(5):
                print("\r所有次数已用完，程序将在{}秒后退出".format(5-i))
                sleep(1)
            print("\n")
            os._exit(0)
    return str(num)

# 穷举所有的数值列表
# 共4！=24种


def getNumList(numbers):
    items = numbers.split()
# 四重循环遍历穷举所有的数值组合
    #data_list = []
    # for i in range(4):
    #     for j in range(4):
    #         if i!=j:
    #             for p in range(4):
    #                 if p!=i and p!=j:
    #                     for q in range(4):
    #                         if q!=i and q!=j and q!=p:
    #                             data_list.append(items[i]+' '+items[j]+' '+items[p]+' '+items[q])
    data_list = [(items[i]+' '+items[j]+' '+items[p]+' '+items[q]) for i in range(4) for j in range(4)
                 for p in range(4) for q in range(4) if (i != j) & (i != p) & (i != q) & (j != p) & (j != q) & (p != q)]
# 使用set方法排除冗余的数字组合
# 当输入的数字中存在重复数字，则4！=24种排序方案会存在重复，必须排除
    return set(data_list)

# 穷举所有的操作符列表
# 共4x4x4=64种


def getOplist(ops):
    # op_list_orgin=ops
    # op_list=[]
    # 三重循环遍历穷举
    # for i in range(4):
    #     for j in range(4):
    #         for p in range(4):
    #             item=str(op_list_orgin[i])+' '+str(op_list_orgin[j])+' '+str(op_list_orgin[p])
    #             op_list.append(item)
    op_list = [ops[i]+' '+ops[j]+' '+ops[p]
               for i in range(4) for j in range(4) for p in range(4)]
    return op_list

# 计算24点


def Cal(num_list, opt_list):
    for numlist in num_list:
        nums = numlist.split()
        for oplist in opt_list:
            ops = oplist.split()
            Cal24(nums, ops)


# 对单种运算符顺序和单种数字顺序进行组合运算
def Cal24(nums, op):
    global Goal, Count

# 第一种情况 ((num0 op0 num1)op1 num2)op2 num3
    try:
        if round(eval("(("+nums[0]+op[0]+nums[1]+")"+op[1]+nums[2]+")"+op[2]+nums[3]), 0) == Goal:
            Count += 1
            print("(({}{}{}){}{}){}{}={}".format(
                nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], Goal))
    except:
        pass

# 第二种情况 (num0 op0 num1) op1 (num2 op2 num3)
    try:
        if round(eval("("+nums[0]+op[0]+nums[1]+")"+op[1]+"("+nums[2]+op[2]+nums[3]+")"), 0) == Goal:
            Count += 1
            print("({}{}{}){}({}{}{})={}".format(
                nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], Goal))
    except:
        pass

# 第三种情况 ( num0 op0 ( num1 op1 num2 )) op2 num3
    try:
        if round(eval("("+nums[0]+op[0]+"("+nums[1]+op[1]+nums[2]+"))"+op[2]+nums[3]), 0) == Goal:
            Count += 1
            print("({}{}({}{}{})){}{}={}".format(
                nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], Goal))
    except:
        pass

# 第四种情况 num0 op0 (( num1 op1 num2 ) op2 num3 )
    try:
        if round(eval(nums[0]+op[0]+"(("+nums[1]+op[1]+nums[2]+")"+op[2]+nums[3]+")"), 0) == Goal:
            Count += 1
            print("{}{}(({}{}{}){}{})={}".format(
                nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], Goal))
    except:
        pass

# 第五种情况 num0 op0 ( num1 op1 ( num2 op2 num3 ))
    try:
        if round(eval(nums[0]+op[0]+"("+nums[1]+op[1]+"("+nums[2]+op[2]+nums[3]+"))"), 0) == Goal:
            Count += 1
            print("{}{}({}{}({}{}{}))={}".format(
                nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], Goal))
    except:
        pass


if __name__ == '__main__':
    ptintInfo()
    numbers = getNumbers()
    start = perf_counter()
    num_list = getNumList(numbers)
    opt_list = getOplist('+-*/')
    Cal(num_list, opt_list)
    printSatistics(perf_counter()-start)
