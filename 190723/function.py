# return value

# 세상에 있는 함수의 갯수 4가지는 이 조합으로 이루어져있다
# 인자가 있는거랑 없는거
# 리턴이 있는거랑 없는거

def yes_in_yes_out(x):  # immutable
    return x

yiyo = yes_in_yes_out(100)
yiyo  # 100


def yes_in_no_out(x):
    result = x * 2

yino = yes_in_no_out(100)
yino  # None

def no_in_yes_out():  # immutable
    return ';)'

niyo = no_in_yes_out()
nuyo  # ;)

def no_in_no_out():
    1 + 1

nino = no_in_no_out()
nino  # None

