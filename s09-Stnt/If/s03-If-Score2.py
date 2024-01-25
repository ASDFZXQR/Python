# -*- coding: utf-8 -*-
# if문

# 결과 = 참 if 조건식 else 거짓
# 조건식이 참이면 '참'을 결과에 할당
# 조건식이 참이 아니면 '거짓'을 결과에 할당

#%%

# [문제]
# 점수(score)에 따라 등급을 분류하라
# A: 90점 이상
# B: 80점 이상
# C: 70점 이상
# D: 60점 이상
# E: 60점 미만
# 60점 이상 '합격'
# 60점 미만 '불합격'

"""
score = 77   # 점수
grade = 'A'  # 등급
msg = '합격' # 합격 or 불합격

if score >= 90:
    grade = 'A'
    msg = '합격'
elif score >= 80:
    grade = 'B'
    msg = '합격'
elif score >= 70:
    grade = 'C'
    msg = '합격'
elif score >= 60:
    grade = 'D'
else:
    grade ='E'
    msg = '불합격'
"""

score = 59
grade = 'E'
msg = '불합격'

#%%
# 처리:
    
if score >= 60:
    msg = '합격'
    grade = 'A' if score >= 90 else\
    'B' if score >= 80 else\
    'C' if score >= 70 else 'D'
    
else:
    msg = '불합격'
    
#%%
    
    
    
print(f"({score})점, 등급({grade}), 합격유무({msg})")










