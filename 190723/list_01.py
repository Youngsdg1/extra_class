# 리스트 만드는 법
# [] , 
# 리스트 안에는 모든 것이 들어갈 수 있다.
# [모든것, 모든것, 모든것, all]
# int, bool, str, list, tuple, dict, set, range


[1, True, 'asdf', [2, False, 'asdf', [], (), range], (), {}, range(0)]

# 일반적인 list
# 1. 요소 모두의 자료형이 같습니다.
# 2. 요소 모두를 관통하는 단어를 찾습니다.
# 3. 그 단어의 복수형을 이름으로 짓습니다.


numbers_1 = [1, 2, 3]

numbers_2 = [10, 20, 30]

numbers_3 = [100, 200, 300]

number_lists = [numbers_1, numbers_2, numbers_3]

number_lists[2]  # numbers_3
numbers_3[1]  # 200

number_lists[2][1]  # 200