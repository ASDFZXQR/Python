"""
[문제] 국어 ,영어 ,수학 점수의 값을 담을 수 있는
변수 3개를 만들고 총합을 담을 수 있는 변수를 만들어
3과목의 점수를 넣어서 출력하라.
"""

#%%

kor = 90
eng = 30
math = 20
tot = kor + eng + math

print("국어", kor)
print("영어", eng)
print("수학", math)
print("-" * 30)
print("합계", tot)

#%%

# 평균
# 나눗셈 연산자: 슬래시(/)

evg = tot / 3

print("평균", evg)
print("평균", tot / 3) # 실수 나눗셈
print("평균", tot // 3) # 정수 나눗셈
