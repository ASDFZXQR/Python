# print() 함수
# "{0}{1}" format(value, value)

hello = "Hello"
world = "World"

print("{0}, {1}!!!". format(hello, world))
print("{1}, {0}!!!". format(world, hello))

print(hello, ', ', world, '!!!', sep='')
print(hello + ', ' + world + '!!!')
print(f"{hello}, {world}!!!")

#%%

helloworld = hello + ', ' + world + '!!!'
print(helloworld)

#%%

hw = hello       # 'hello
hw = hw + ', '   # 'hello, '
hw = hw + world  # 'hello, world'
hw = hw + '!!!'  # 'hello, world!!!'
print(hw)

#%%

# 복합대입연산자 : +=
# 오른쪽에 있는 표현식을 자기 자신과 더한 후
# 다시 자기 자신에게 할당
# a += b
# a = a + b

hw2 = hello   # 'hello
hw2 += ', '   # 'hello, '
hw2 += world  # 'hello, world'
hw2 += '!!!'  # 'hello, world!!!'
print(hw2)







