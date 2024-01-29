# -*- coding: utf-8 -*-

# 파일 입출력
# open()
# close()
# read(), readline(), readlines()
# write

#%%

# 파일전체 읽기
# 'r' : 파일 내용을 읽기 모드로 오픈
# 파일객체.read() : 파일에 있는 모든 데이터를 읽어서 리턴
score_file = open("score.txt", "r", encoding="utf8")
read_data = score_file.read()
print(read_data)
score_file.close()

#%%

# 파일 라인 단위로 읽기
# 파일객체.readline()
score_file = open("score.txt", "r", encoding="utf8")
data1 = score_file.read()
print(data1, end="")
data2 = score_file.read()
print(data2, end="")
score_file.close()

#%%

score_file = open("score.txt", "r", encoding="uft8")

while True:
    line = score_file.readline()
    if not line:
        print("not line:", line) # line is empty
        break
    print(line, end="")

score_file.close()