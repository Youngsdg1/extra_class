# T/F가 되는 상황
# 비어있는 것들  or None

r = print('asdf')
print(r) = None

give_me = {'a':1, 'b': 2},.get('c') #None

if unknown_list == None #없어라는 값임

# 빈 리스트를 묻고싶으면
unknown_list == []

# 자동으로 F가 결정되는 경우
bool , if, while  # 0, 0.0, '', [], {}, (), None 얘네가 저 안에 들어가게 되면 전부 False 처리가 됨

# 자동으로 T가 되는 경우
if, while bool # 저것들 제외한 나머지 전부

# 특정 리스트가 값이 있다면 a 하고, 비었다면 b 하겠다
if some_list:  # type(some_list) == list 라면 뭐라도 있으면 내려가고, 비어있으면 False로 지나감
    a()
else:
    b() 

# 반대로 쓰고 싶으면
if not some_list:  
    a()
else:
    b() 

