# for => 안전. 반드시 끝남 처음 => 끝 모두 순회하며 돌아요
# for 와 in은 반드시 합쳐서 가야됨
# for ? in ??: ? 내가 짓고 싶은 이름. ?? 돌릴 수 있는 것 : list,string,range,dict,tuple
for i in range(10):
    print(i+1)  # 1부터 10을 출력

    
         

total = 0
for n in [1, 2, 3, 4 ,5]:
    total = total + n

print(total)

# while => 내가 끝을 지정해야함. 자우도 높음
# whlie (T/F)
# 짝으로 Flag를 많이씀

# 파이썬 내맘대로 T/F 변환법칙
# F:0, '', [], {}, (), None 얘네를 제외한 모든건 다 T !!! 비어있는 !! 0 이 아닌 모든것!!
# while 뒤에 있는게 F가 될 때까지 무한히 돈다. break 한번 만나면 아예 끝나. 달리는 차의 키를 뽑는거임. 

# Falg = True

# while flag:
    

#     언젠가  flag = False 가 되는 순간을 우리가 조종할 수 있음!!


x =0
while x < 10:
    print('열번말하기')
    x = x + 1