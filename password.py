import random
str_pass_low = 'qwertyuiopasdfghjklzxcvbnm'
srt_pass_up = str_pass_low.upper()
str_pass_other = '`~!@#$%^&*()_+=-1234567890{}][;:"\|<>.,?/'
str_end = str_pass_low + srt_pass_up + str_pass_other
list = str_end
print(list)
i = int(input('ВВедите длину пароля '))
password = ''
for j in range(0,i):
    # random.shuffle(list)
    o = random.choice(list)
    password = password + o
print(password)
input()