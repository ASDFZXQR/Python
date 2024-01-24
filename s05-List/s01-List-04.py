# 리스트(list)
# 여러 형태의 자료들의 연속된 모임
# 변경가능(mutable)

#%%

# 성적처리 : 이름, 국어, 영어, 수학
sl = ['우등생', [80, 90, 100], 0, 0.0]

#%%

# 총점
# sl[-2] = sl[1][0] + sl[1][1] + sl[1][2]
sc = sl[1] # 국어, 영어, 수학
sl[-2] = sc[0] + sc[1] + sc[2]
print("총합:", sum(sc))


# 평균
sl[-1] = sl[-2] / 3.0

print('전체:', sl)
print('점수:', sc)


