# [문제3]
# 한 달 급여가 400만원이다.
# 분기별 보너스는 월급여의 30%가 지급된다.
# 세금은 월급여의 3%이다.
# 보너스에 대한 세금은 없다.
# 월 세후 수령액은 얼마인가?
# 연 총세금은 얼마인가?
# 세 후 연수령액은 얼마인가?

#%%

salary = 4000000
print("급여 :", salary)

bonus = salary * 0.3
print("보너스 :", bonus)

tax = salary * 0.03
print("세금 :", tax)

pay = salary - tax
print("월 수령액 :", pay)

total_tax = tax * 12
print("연 세금 :", total_tax)

total = salary * 12
total += bonus * 4
print("총 연봉 :", total)

year_salary = pay * 12
year_salary += bonus * 4
print("연 수령액 :", year_salary)




















