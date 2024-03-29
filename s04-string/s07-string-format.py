# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자(character)
# %d : 정수(10진수, decimal)
# %f :실수(float)
# %o : 8진수(octal)
# %x : 16진수(hexa-decimal)

# 형식
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)

#%%

# 실수 포맷 : %f
eco =  2.2445
print("올해의 경제 성장률 예상치는 (%f)입니다." % eco) # 2.240000
print("올해의 경제 성장률 예상치는 (%d)입니다." % eco) # 2

#%%

# 소숫점 이하 3자리를 반올림해서
# 소숫점 이하 2자리로 제한

print("올해의 경제 성장률 예상치는 (%.2f)입니다." % eco) # 2.25

#%%

# 전체 자릿수 지정
# 정렬 : 기본은 오른쪽 정렬
# 정렬 : -1, 왼쪽 정렬
# 남은 자릿수는 공백 처리

pi = 3.14
print("원주율은 (%f)입니다." % pi)
print("원주율은 (%10f)입니다." % pi)
print("원주율은 (%10.2f)입니다." % pi)
print("원주율은 (%-10.2f)입니다." % pi)

#%%

n2 = 10
n4 = 1000
n5 = 10000

# 전체 자릿수 지정
# 정렬 : 기본 오른쪽 정렬
print("정수 자릿수 지정 (%6d)" % n2)
print("정수 자릿수 지정 (%6d)" % n4)
print("정수 자릿수 지정 (%6d)" % n5)

# 왼쪽 정렬(minus (-))
print("정수 자릿수 지정 (%-6d)" % n2)
print("정수 자릿수 지정 (%-6d)" % n2)
print("정수 자릿수 지정 (%-6d)" % n2)

#%%

# 문자열 정렬
# 한글은 2자리를 차지하지만 한 문자를 처리

s = "문자열 정렬"
print("     :12345678901234567890")
print("기본 (%s)" % s)
print("오른쪽 (%10s)" % s)
print("왼쪽 (%-10s)" % s)

#%%

s = "ABMab12"
print("       :12345678901234567890")
print("기본   (%s)" % s)
print("오른쪽 (%10s)" % s)
print("왼쪽   (%-10s)" % s)



























