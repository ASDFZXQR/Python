# -*- coding: utf-8 -*-

# [문제]
# for, range를 사용하여 다음의 합을 구하라.
# 1부터 10까지 연속된 숫자를 생성하여
# 홀수의 합과 짝수의 합을 각각 구하라.

#%%

s = 1
e = 11

odd = 0
even = 0

for n in range(s, e):
    if (n % 2) == 1:
        odd += n
    else:
        even += n
            
print("홀수의 합:", odd)
print("짝수의 합:", even)

#%%

# 홀수
odd = 0

for n in range(1, 10, 2):
    odd += n
    
print("홀수의 합:", odd)

#%%

# 짝수
even = 0

for n in range(2, 11, 2):
    even += n
    
print("짝수의 합:", even)