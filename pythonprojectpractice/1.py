# open(filename): Open file and return a corresponding file object.
mine = open('我的發票.txt').read().split()
goal = open('中獎號碼.txt').read().split()
money = open('$$.txt').read().split()
sum = 0
many = 0
for i, num in enumerate(mine):

    if num in goal:
        many = many + 1
        sum = sum + money[i]
        print('number', i+1, '張發票兌種號碼', num, '!')


print('total', many, '張')
print('total', sum, '元')


print(mine)
print(goal)


