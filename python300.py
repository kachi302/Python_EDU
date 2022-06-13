# from os import sep


# print('Hello world')
# print("mary's cosmetics")
# print('신씨가 소리질렀다."도둑이야"')
# print("c:\windows")
# print("안녕하세요\n만나서 \t\t 반갑습니다.")
# print("오늘은","일요일")
# print("naver","kakao","samsung", sep="/")
# #print 줄바꿈, ; --> 한줄에 여러개의 명령을 작성, end="" 줄바꿈 없이 출력 할때
# print("first", end="");print("second")
# print(5/3)
# # 변수 사용하기
# samsung = 50000
# print(samsung * 10)

# current_total = 298000000000000
# current_unit = 50000
# per = 15.79
# print(" 시가 총액 :", current_total)
# print("현재가 ", current_unit)
# print("PER", per)
# #문자열 출력
# s = "hello"
# t = "python"
# print(s+'!', t)
# print(2 + 2 * 3)
# #type 함수
# a = 128
# print(type(a))
# a = "123"
# print(type(a))

# # 문자열을 정수로 변환
# num_str = "720"
# num_int = int(num_str)
# print(num_int)

# print(num_int+1,type(num_int))

# #정수를 문자로
# num_int = 170
# num_str = str(num_int)
# print(num_str)

# # 문자를 float
# num_str = "15.79"
# num_float = float(num_str)
# print(num_float)

# year = "2020"
# year_int = int(year)
# print(year_int, year_int+1, year_int+2)

# air_m_price = 48584
# period = 36
# tot_price = air_m_price * period
# print(tot_price)

#https://wikidocs.net/7021 21 항목

# from distutils.command.config import LANG_EXT


# letters = 'python'
# print(letters[0],letters[2], letters[0:3],letters[3:-1])

# license_plate = '24가 2110'
# print(license_plate[4:])
# print(license_plate[-4:])
# #문자열 자르기 (시작인덱스:끝인덱스:오프셋)
# string= '홀짝홀짝'
# print(string[::2])
# # 문자열 거꾸로 출력
# string = 'python'
# print(string[::-1])

# #문자열 치환
# string='010-9439-3984'
# nString = string.replace('-',' ')
# print(nString)
# print(string.replace('-',''))
# #문자열 다루기
# url = 'http://empal.com'
# new_url = url.split('.')
# print(new_url, new_url[-1])

# string = 'abcdefghijkabe'
# print(string.replace('a','A'),'  ',string)


# string = 'abab'
# n_string = string.replace('a','A')
# print(n_string)

# a ='3'
# b ='4'
# print(a + b)
# print(a * 3)

# print('-' * 80)

# a = 'python'
# b = 'java'
# print(a +' '+ b)
# print((a + ' '+ b + ' ')* 3)

# name1 = '김민수'
# age1 = 10
# name2 = '이철희'
# age2 = 13
# print('이름 : ' + name1 + ' 나이 ' +str(age1))
# # 포맷팀 함수 사용
# print('이름 %s 나이 : %d' % (name1, age1))
# print('이름 %s 나이 : %d' % (name2, age2))
# # format 함수 사용
# print(' format 함수 사용')
# print('이름: {} 나이 : {}'.format(name1, age1))
# print('이름: {} 나이: {}'.format(name2,age2))
# # f string 사용
# print('f string 사용')
# print(f'이름: {name1} 나이: {age1}')
# # comma 제거
# samsung_stock = '5,969,782,550'
# print(samsung_stock.replace(',',''))
# n_stock = int(samsung_stock.replace(',',''))
# print(int(n_stock),type(n_stock))

# # 문자 슬라이싱
# q_quote = '2020/03(E) (IFRS 연결)'
# print(q_quote[:7])
# print(q_quote[7:])

# #문자열 공백제거
# data ='   dabee  '
# data1 = data.strip()
# print(data1)
# # 대문자
# ticker = 'btc_ticker'
# ticker1 = ticker.upper()
# print(ticker1)
# # 소문자
# print(ticker1.lower())
# # 첫문자를 대문자로 변경
# data = 'hello'
# data1 = data.capitalize()
# print(data1)
# #endswith  - 일치 해야 한다.
# file_name = '보고서.xlsx'
# print(file_name.endswith('xlsx'))
# print(file_name.endswith(('xlsx','xls')))

# #startswith 메서드 (시작 문자)
# file_name = '2020_보고서.xlsx'
# print(file_name.startswith('2020'))

# data = 'hello world'
# print(data.split(' '))
# data = 'btc_krw'
# data1 = data.split('_')
# print(data1)

# data ='2020-05-01'
# data1 = data.split('-')
# print(data1[1:])
# #오른쪽 공백 제거
# data = '030912  '
# print(len(data),len(data.rstrip()),data.rstrip())

# # 리스트 생성
# from audioop import avg


# movie_rank = ['닥터 스트레인지','스플릿','럭키']
# print(movie_rank)
# movie_rank.append('홍길동')
# print(movie_rank)
# movie_rank.insert(1,'슈퍼맨')
# print(movie_rank)
# movie_rank.remove('스플릿')
# print(movie_rank)
# del movie_rank[2]
# print(movie_rank)

# #list 합치기
# lang1 = ['C', 'C++', 'JAVA']
# lang2 = ['Python', 'Go', 'C#']

# lang3 = lang1 + lang2
# print(lang3)

# # 최대값, 최소값
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('max ', max(nums), 'min', min(nums))
# print('max %d  min %d' %(max(nums),min(nums)) )

# #list 합
# print(sum(nums))
# #list item 갯수
# print(len(nums))

# #list 평균
# print(sum(nums)/ len(nums))

# price = ['20220311', 100, 100, 100, 100, 100]
# print(price[1:])

# # 홀수만
# print(nums[::2])
# #짝수만
# print(nums[1::2])

# # 역방향
# print(nums[::-1])

# lang1=['samsung','lg','naver']
# print(lang1[::2])
# print(lang1[0], lang1[2])
# print(" ".join(lang1))
# print("/".join(lang1))
# print("\n".join(lang1))
# lang3='samsung/lg/naver'
# lang4 = lang3.split('/')
# print(lang4)
# 튜플  - () 로 정의
# my_varialbe = ()
# print(type(my_varialbe))
# movie_rank = ('닥터 스트레인지','스플릿','럭키')
# print(movie_rank)
# my_tuple = (1,) #하나의 데이타가 저장이 되는 경우는 (2,) 와 같이 쉼표를 입력한다.
# print(type(my_tuple))

# #t = (1, 2, 3)
# #t[0] ='a'   #튜플은 원소의 값을 수정 할수 없다.
# #t= 1, 2, 3, 4   #원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.
# #print(type(t))
# t = ('a', 'b', 'c')  # 튜플은 수정 할수가 없기에, 새로운 튜플을 선언해야 한다.
# t = ('A', 'b', 'c') # 기존에 설정한 튤플은 자동으로 삭제된다.
# print(t)
# #튜플을 리스트로 변환
# data = list(t)
# print(data)
# data[0]='aa'
# print(data)
# #튜플 언패킹
# a, b, c = t
# print(a, b,c)
# #튜플 range
# data = tuple(range(2,100,2))
# print(data)

# 파이썬 딕셔널리
# * 표현식
# a, b, *c = (0, 1, 2, 3, 4, 5)
# print(a, b, c)
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _= scores
# print(valid_score) 
# a, b, *valid_score = scores
# print(valid_score)
# #start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩
# a, *valid_score, b = scores
# print(valid_score)
# # 비어있는 딕셔널리
# temp = {}
# print(type(temp))

# ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1200}
# print(ice)
# # 추가
# ice['죠스바'] = 1200
# ice['월드콘'] = 1300
# print(ice)
# print('메로나 가격:', ice['메로나'])
# #수정
# ice['메로나']=1300
# print('메로나 가격:', ice['메로나'])
# #삭제
# del ice['메로나']
# print(ice)

# #딕셔널리 생성
# inventory = {'메로나': [200,20],
#            '비비빅': [300, 10],
#            '죠스바': [400, 10]}
# print(inventory)
# # 딕셔널리 인덱싱
# print(inventory['메로나'][0],'원',inventory['메로나'][1],'개' )
# inventory['월드콘']=[200, 10]
# print(inventory)
# # 딕셔널리 키 인덱싱
# ice_name = list(ice.keys())
# print(ice_name)

# user = input('입력')
# print(user * 2)

# user = int(input('임의의 수'))
# if user % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')
        
# if user + 20 > 255:
#     print(255)
# else:
#     print(user + 20)    
# n_num = user - 20
# if n_num < 0:
#     print(0)
# elif n_num > 255:
#     print(255)
# else:
#     print(n_num)

# # 입력 시간 판단
# iTime = input("현재 시간은 ")
# if iTime[-2:] == '00':
#     print('정각')
# else:
#     print('정각이 아님')    
# # 117    
# fruit = ['사과', '포도', '홍시']
# i_f = input('좋아 하는 과일은? ')
# if i_f in fruit:
#     print('ok')
# else:
#     print('false')                 
#warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# i_warr = input('투자 종목')
# if i_warr in warn_investment_list:
#     print('투자경고 종목 입니다.')
# else:
#     print('투자 경보 종목이 아닙니다.')    
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# # i_season = input('좋아 하는 계절은 ?')
# # dict 의 key 값
# # if i_season in fruit:
# #     print('정답입니다.')
# # else:
# #     print('오답입니다.')  
# # dict 의 value 값
# i_fruit = input('좋아 하는 과일은 ?')
# if i_fruit in fruit.values():
#     print('정답입니다.')
# else:
#     print('오답입니다.')      
# 대소문자
# i_aphabet = input('알파벳 ?')
# if i_aphabet.islower():
#     print(i_aphabet.upper())
# else:
#     print(i_aphabet.lower())    
# i_score = int(input(' 점수는 ?'))
# if 81 <= i_score <= 100:
#     print('A')
# elif 61 <= i_score <= 80:
#     print('B')
# elif 41 <= i_score <= 60:
#     print('C')
# elif 21 <= i_score <= 40:
#     print('D')
# elif 0 <= i_score <= 20: 
#     print('E')    
# else:
#     print(' Error , 점수 입력 오류')               

# 환율 = {'달러':1167,
#         '엔':1.96,
#         '유로':1268,
#         '위안':171}
# usr = input('입력')
# num, currency = usr.split()
# print(float(num) * 환율[currency], '원')    

# num = input(' 3개의 숫자 입력')
# num1, num2, num3 = num.split()
# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)      
# tel = {'011':'SK',
#        '016':'KT',
#        '019':'LG',
#        '010':'알수 없음'}
# i_phone = input('폰번호')
# num1, num2, num3 = i_phone.split('-')
# print(num1, tel[num1])

# 우편번호 = input('우편번호 :')
# 우편번호 = 우편번호[:3]
# if 우편번호 in ['010', '011', '012']:
#     print('강묵부')
# elif 우편번호 in ['014','015', '016']:
#     print('도봉구')
# else:
#     print('노원구')      

# jumin = input('주민번호')
# jumin = jumin.split('-')[1]
# print(jumin)
# if jumin[0] == '1' or jumin[0] == '3':
#     print('Man')
# else:
#     print('Woman')  
# jumin = input('주민번호')
# b_jumin = jumin.split('-')[1]
# print(b_jumin)
# if 0 <= int(b_jumin[1:3]) <= 8:
#     print('서울입니다.')
# else:
#     print('서울이 아닙니다.')    
# 129
# num = input('주민번호:')
# cal1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# cal2 = 11 - (cal1 % 11)
# cal3 = str(cal2)
# if num[-1] == cal3[-1]:
#     print("유효한 주민번호")
# else:
#     print('유효하지 않은 번호')            

# import requests
# btc = requests.get('https://api.bithumb.com/public/ticker/').json()['data']

# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])
# if (시가 + 변동폭) > 최고가:
#     print('상승장', 시가, 최고가, 변동폭)
# else:
#     print('하락장', 시가, 최고가, 변동폭)    
#  반복문
# fruit =['사과','귤', '바나나']
# for p_fruit in fruit:
#     print(p_fruit)
#     print('#####')
# for v in ['S', 'B', 'D']:
#     print(v.lower())
# v_list = [100, 200, 300]
# for vt_list in v_list:
#     print(int(vt_list * 1.1))
# v_list = ['김밥+라면','라면+밥','튀김라면']
# for v_list1 in v_list:
#     print('오늘의 메뉴 :', v_list1, len(v_list1), v_list1[0])

# num = [1, 2, 3]
# for num1 in num:
#     print(num1, ' * 3 ',' = ', num1*3)    
#리스트 = ["가", "나", "다", "라"]
# i = 리스트[1::]
# for n in i:  
#     print(n)
# i = 리스트[::2]  #[시작:끝:증감폭]
# for n in i:  
#     print(n)
# for n in 리스트[::-1]:
#     print(n)
# n_list = [20, -30, 40, -50]
# for n_n in n_list:
#     if n_n <0:
#         print(n_n)
# nList = [3, 100, 23, 44]
# for n in nList:
#     if n % 3 == 0:
#         print(n)       
# nList = [13, 21, 12, 14, 30, 18]
# for n in nList:
#     if n % 3 == 0 and n < 20:
#         print(n)
# nList = ["I", "study", "python", "language", "!"]
# for n in nList:
#     if len(n) > 3:
#         print(n)
# nList = ["A", "b", "c", "D"]
# for n in nList:
#     if n.isupper():
#         print('대문자 :',n)
#     else:
#         print('소문자', n)
# nList = ['dog', 'cat', 'parrot']
# for n in nList:
#     uFirst = n[0].upper()
#     nChar = uFirst + n[1::]
#     print(nChar)
#     print(n[0].upper() + n[1::])
# nList = ['hello.py', 'ex01.py', 'intro.hwp']
# for n in nList:
#     nchar = n.split('.')
#     print(nchar[0])
# nList =  ['intra.h', 'intra.c', 'define.h', 'run.py']
# for n in nList:
#     nc = n.split('.')
#     if nc[1] =='h' or nc[1] == 'c':
#         print(n)
# for n in range(2002, 2050, 4):
#     print(n)
# for n3 in range(0, 30, 3):
#     print(n3)        
# for n in range(0,100, 1):
#     print(99-n)
# nl=[]
# for n in range(1, 9, 1):
#     nl.append(n*3)
#     if n % 2 != 0:
#         print(n * 3)
# print(nl[3])    
# num = 3
# for n in range(1, 10, 2):
#     print ( n , '*', num ,' = ', n * num )
# from ast import Num
# sum = 0
# for n in range(1, 11, 1):
#     sum += n
# print(sum)    

# sum1 = 0
# for n in range(1, 10, 2):
#     sum1 += n
# print(sum1)    

# result = 1
# for i in range(1, 11):
#     result *= i
# print(result)    
from tkinter import N


price_list = [32100, 32150, 32000, 32500]
# for n in range(4):
#     print(price_list[n])
for n in range(1,len(price_list)):    
    #print(100+n*10, price_list[n])
    print(price_list[n-1], price_list[n])
    
my_list = ["가", "나", "다", "라", "마"]    
# for n in range(2,len(my_list)):
#     print(my_list[n-2], my_list[n-1], my_list[n])

for n in range(1,len(my_list)-1):
    print(my_list[len(my_list)-1-n], my_list[len(my_list)-n-2])    