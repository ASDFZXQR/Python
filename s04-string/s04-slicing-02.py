# 문자열 슬라이싱(slicing)
# 특정한 범위를 지정해서 추출
# 추출을 하게되면 기존의 문자열의 변화는 없다.(원본의 변화는 없다)
# 추출된 문자열은 새로운 변수에 할당

# 변수 = 문자열[시작번호:종료번호:스텝]
# 시작위치 : 0부터시작
# 종료위치 : 종료번호 -1까지
# 스텝간격 : 건너뛰기

s = "영일이삼사오육칠팔구십"
print(s)

#%%

print(s[0:7:1]) # 영일이삼사오육
print(s[0:7:2]) # 영이사육
print(s[1:7:2]) # 일삼오
