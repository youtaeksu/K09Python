'''
for문
    형식]
        for 반복변수 in 목록형:
            실행문;
    range()함수
        : 반복문에서 주로 사용하는 함수로 범위를 지정하거나 증가치를 지정한다.
        형식]
            range(10) : 0~9까지
            range(2,10) : 2~9까지
            range(2,10,2) : 2~9까지 2씩 증가
        구간이 설정되면 항상 마지막숫자의 미만까지 지정된다.
'''
# 0~4까지 반복한다.
from math import remainder


for i in range(5):
    print("i=", i, end=" ")
print()

# 리스트의 크기만큼 반복. 확장for문과 같은 형태로 사용.
list1 = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list1:
    sum += i
print("1부터 10까지의 합 = ", sum)

# 파이썬에서는 문자열을 즉시 인덱싱 할 수 있으므로 길이만큼 반복할 수 있다.
str1 = "파이썬이좋아요"
for ch in str1:
    #print()뒤에 end를 사용하면 줄바꿈없이 출력할 수 있다.
    print(ch, end=" ")
print()

# 2개의 중첩된 for문으로 구구단 출력하기
for dan in range(2,10): #2~9까지 반복
    for su in  range(1,10): #1~9까지 반복
        #printf()와 같이 서식을 지정하여 출력할 수 있다.
        print("%2d * %2d = %2d" % (dan, su, su*dan), end=' ')
    print()
print()

'''
for문도 else구문을 사용할 수 있다.
단, for문이 정상적으로 종료되었을때에만 실행된다.
'''
for i in range(3):
    print(i, end=" ")
else:
    # for문이 3번 실행된 후 else구문이 실행된다.
    print("for문 종료됨")

for i in range(3):
    print(i, end=" ")
    # 1번 실행 후 break를 만나게 되므로 for문을 탈출한다.
    break
else:
    # 따라서 이 경우 else구문이 실행되지 않는다.
    print("braek를 통해 for문이 완료되지 않았으므로 출력되지 않음.")
    
'''
시나리오] 연월일을 입력해서 요일 구하는 프로그램을 작성하시오.
#윤년추가규칙 : 지구의 공전주기가 365.2422 이므로 이를 보정하기 위한 수식이다.
-4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다.
-4로 나누어 떨어지지만 100으로도 나누어 떨어지는 해는 평년으로 한다.
-단, 400으로 나누어 떨어지는 해는 윤년으로 한다.(예: 2000년, 2400년)
'''

# 년, 월, 일을 숫자형으로 입력받는다.
year = int(input("년도를 입력하시오:"))
month = int(input("월을 입력하시오:"))
day = int(input("일을 입력하시오:"))

# 누적날짜수 : 서기 1년1월1일부터 입력한 날짜까지의 모든 일수를 더할것임.
total_days = 0
# 월별 날짜수를 리스트로 정의한다. (1월->31일, 7월8월->31일 등)
year_month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 서기 1년부터 입력할 년도까지의 누적 날짜수를 더한다.
# 만약 2022년을 입력했다면 2021년까지만 반복하여 누적한다.
for d in range(1,year):
    # 400으로 나눠서 떨어지면 윤년이므로 366일 된다.
    if d % 400 == 0:
        total_days = total_days + 366
    # 100으로 나눠지면 평년
    elif d % 100 == 0:
        total_days = total_days + 365
    # 4로 나눠지면 윤년
    elif d % 4 == 0:
        total_days = total_days + 366
    # 그 외는 모두 평년으로 계산한다.
    else:
        total_days = total_days + 365
        
# 입력년도의 각 달의 날짜수를 누적해서 더한다.
# 만약 6(월)을 입력했다면 5(월)까지 반복하여 누적한다.
for m in range(1, month):
    # 월별 날짜수를 정의한 리스트를 이용한다.
    total_days = total_days + year_month_days[m]

'''
입력월이 3이상이고 , 입력년도가 윤년이라면 1을 더해야 한다.
월별 날짜수는 2월이 28일로 고정되어 있으므로 별도의 처리가 없다면 무조건
평년으로 계산되기 때문이다.
'''
if month >= 3:
    if year % 400 == 0:
        total_days = total_days + 1
    elif year % 100 == 0:
        total_days = total_days + 0
    elif year % 4 == 0:
        total_days = total_days + 1
    else:
        total_days = total_days + 0
     
# 총 누적된 일수에 우리가 입력한 일수를 더해준다.   
total_days += day
print()
print("total_days :", total_days)
# 일주일은 7일이고 요일은 일요일부터 시작이므로 나머지가 0이라면 일요일로 판단할 수 있다.
remainder = total_days % 7
if remainder == 0:
    print("일요일입니다.")
if remainder == 1:
    print("월요일입니다.")
if remainder == 2:
    print("화요일입니다.")
if remainder == 3:
    print("수요일입니다.")
if remainder == 4:
    print("목요일입니다.")
if remainder == 5:
    print("금요일입니다.")
if remainder == 6:
    print("토요일입니다.")