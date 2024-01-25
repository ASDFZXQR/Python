# 조건문 : If

# [문제]
# 가진 돈을 가지고 음료수를 구매하는데
# 돈에 따라서 가장 비싼 음료를 구매한다.
# 커피: 5000
# 탄산: 3000
# 생수: 1000
#%%
"""
money = int(input("가진 돈이 얼마인가?"))
coffee = 5000
drink = 3000
water = 1000

if money >= 5000:
    print("커피")
elif money >= 3000:
    print("탄산")
elif money >= 1000:
    print("생수")
"""
#%%

money = int(input("가진 돈이 얼마인가?"))
print(type(money), money)

print(f"당신이 가진 돈은 ({money})원 입니다.")

# 값이 큰 순서로 조건을 처리해야 한다.

if money >= 5000:
    print("당신이 가진 돈으로(커피)를 살수 있습니다.")
elif money >= 3000:
    print("당신이 가진 돈으로(탄산)음료를 살수 있습니다.")
elif money >= 1000:
    print("당신이 가진 돈으로(생수)를 살수 있습니다.")
else:
    print("그냥 정수기 물을 드세요.")












