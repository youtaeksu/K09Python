print("=", "enumerate()", "="*20)
data = ['Naver', 'Kakao', 'Google']
for i, v in enumerate(data):
    print(i, v)
    
print("="*5, "eval()", "="*20)
print(eval('1+2'))
print(eval("'hi' + 'a'"))

print("="*5, "sorted()", "="*20)
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
print(sorted(numbers))

import sys
print("="*5, "이터레이터 함수1", "="*20)
list = [1,2,3,4]
it = iter(list)
while True:
    try:
        print('it=', next(it))
    except StopIteration:
        print("예외발생")
        break
print()