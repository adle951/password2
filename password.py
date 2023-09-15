password = '123'
times = 3
while True:
    answer = input('請輸入密碼：')
    if password == answer:
        print('密碼正確。')
        break
    else:
        times = times - 1
        print('密碼錯誤，還有', times, '次機會。')

    if times <= 0:
        print('登陸失敗')
        break




