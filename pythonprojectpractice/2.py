# open the file
mine = open('我的發票.txt').read().split()
win = open('中獎號碼.txt').read().split()
money = [200, 1000, 4000, 10000, 40000, 200000]
sum = 0

for i, num in enumerate(mine):
    for j in win:
        for k in range(8, 2, -1):
            if num[-k:] == j[-k:]:
                sum = sum + money[k-3]
                print('No.', i+1, 'of receipt', num, 'is win!!')
                print('中', money[k-3], '元')
                break

print('You get', sum, 'dollars!!')


