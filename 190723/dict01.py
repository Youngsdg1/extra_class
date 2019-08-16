# key - value 접근하기
d = {'a': 1, 'b': 2, 'c': [1, 2, 3]}

# 벨류를 꺼낼때는 언제나 대괄호!!! 인덱스 접근처럼이라고 생각하면 안헷갈림
d['a'] #1
# 은행에 금고 기능이 있는거라 생각. 이 금고에 내 지문이 등록돼있냐 마냐. 몇개가 들었는지 안물안궁.

for key in d: #d는 for를 돌리면 key가 나온다. 값은 몰라도 key는 아니까
    if key == 'a':
        result =d[key]
        # 지문을 다 보고 이게 내 지문이네! 하는 꼴임. 위 아래 같은거임

# key를 꺼내는 2가지 방법
for key in d:
    pass

for key in d.keys():
    pass

# value를 꺼내는 방법
for value in d.values():
    pass





#value 다 프린트하고싶으면
for value in d.values():
    print(value)

for key in d:
    print(d[key])

#key, value 같이 꺼내기:
for key, value in d.itmes():
    pass



# dict methods

# for 를 돌릴 때 raw, .keys(), .values(), .items()

# 왜 for 를 돌리지 않는가.