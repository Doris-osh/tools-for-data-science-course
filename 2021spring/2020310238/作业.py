'''
def fibe(n):
    s = [1,1]
    while not s[-1] > n:
        s.append(s[-1]+s[-2])
    s.pop()
    t = 1
    for i in s:
        t *= i
    s1 = [s,t]
    return s1
n = int(input('请输入正整数n：'))
print(str(n)+'以内的斐波那契数列为：',end = '')
print(fibe(n)[0],end = '')
print('\n这些斐波那契数的乘积为：'+str(fibe(n)[1]))
'''

def fibe(n):
    s = [1,1]
    t = 1
    for i in range(n-2):
        s.append(s[i]+s[i+1])
        t *= s[-1]
    s1 = [s,t]
    return s1
n = int(input('请输入正整数n：'))
print('前'+str(n)+'个斐波那契数为：',end = '')
print(fibe(n)[0],end = '')
print('\n这些斐波那契数的乘积为：'+str(fibe(n)[1]))
