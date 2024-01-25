# -*- coding: utf-8 -*-

# for

# [문제] 2단부터 9단까지 구구단을 만들어라
# for, range를 이용하라.

#%%


for n in range(2, 10):
    for m in range(1, 10):
        print(n * m, end=' ')
        print('')
        
#%%

for x in range(2, 10):
    for y in range(1, 10):
        print("%2d" % (x * y), end=' ')
        print()
        
#%%

for x in range(2, 10):
    for y in range(1, 10):
        print(f"{x*y:>2}", end=' ')
        print()
        
#%%

for x in range(2, 10):
    print(f"[{x}단]")
    for y in range(1,10):
        print(f"[{x}]*[{y}]=[{x*y:>2}]")
        print()
        