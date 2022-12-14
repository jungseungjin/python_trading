# 판다스(Pandas)라는 모듈은 1차원 데이터를 다루는 Series 타입과 2차원 데이터를 위한 DataFrame 타입을 제공합니다. 
# 특히 Series와 DataFrame 타입을 사용하면 데이터를 엑셀로 쉽게 저장할 수 있고 그래프도 그릴 수 있습니다. 
# 또한, 데이터 분석을 위한 다양한 메서드를 제공합니다.

# Series 생성
# 판다스 Series는 1차원 데이터를 저장하기에 효과적인 자료구조입니다. 
# 여기서 1차원 데이터라는 것은 엑셀 시트에 있는 한 행 또는 한 열에 있는 데이터를 생각하시면 됩니다.
#  예를 들어 비트코인의 최근 5일 종가와 같은 것들이 1차원 데이터입니다.

# Series는 클래스로 pandas 모듈 안에 포함되어 있습니다. 따라서 이를 사용하기 위해서는 먼저 import를 해야 합니다.

# from pandas import Series
# Series 객체는 리스트를 사용해서 만들 수 있습니다. 클래스 Series의 생성자로 리스트를 넘겨주면 Series 객체가 생성됩니다.

# data = [100, 200, 300, 400]
# s = Series(data)
# print(type(s))
# 라인 1: data라는 변수가 파이썬 리스트를 바인딩합니다.
# 라인 2: Series 객체가 생성됩니다. 생성된 Series 객체를 s라는 변수가 바인딩합니다.
# 라인 3: s라는 변수가 바인딩하는 객체의 타입을 출력합니다.


# 위 코드를 실행하면 0부터 시작하는 정수 인덱스와 함께 리스트의 데이터가 출력됩니다. 0부터 시작하는 정수 인덱스에 값이 맵핑되는 것을 보면 파이썬의 리스트와 비슷해 보입니다.

# 0    100
# 1    200
# 2    300
# 3    400
# dtype: int64


# Series 생성할 때 인덱스를 지정하기
# 이번에는 표 4-4의 리플 종가 데이터를 Series 객체로 표현해 보겠습니다. 저장해야 할 정보는 날짜와 해당일의 리플 종가입니다. 파이썬 리스트를 사용하면 리플의 종가 또는 날짜만 저장할 수 있습니다.

# 표 4-4 리플의 5일 종가

# 날짜	리플 종가
# 2018-08-01	512
# 2018-08-02	508
# 2018-08-03	514
# 2018-08-04	507
# 2018-08-05	500
# 앞에서 Series 객체를 생성했던 것처럼 종가 데이터만 사용해서 Series 객체를 생성하면 날짜를 표현할 수 없습니다. 날짜별로 종가를 저장하기 위해서는 Series 객체를 생성할 때 index 파라미터로 날짜를 넘겨주면 됩니다.

# # ch04/04_10.py
# 1: from pandas import Series 
# 2: date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
# 3: xrp_close = [512, 508, 512, 507, 500] 
# 4: s = Series(xrp_close, index=date) 
# 5: print(s)
# 라인 3: 각 날짜를 문자열로 표현하고 이를 리스트 객체로 만듭니다.
# 라인 4: 리플 종가를 리스트로 만듭니다.
# 라인 5: 리플 종가를 갖고 Series 객체를 생성하는데 이때 인덱스 값으로 날짜를 지정합니다.


# s라는 변수는 Series 객체를 바인딩합니다. 
# 출력된 값을 확인해보면 인덱스로 정숫값 대신에 문자열로 표현된 날짜가 사용된 것을 확인할 수 있습니다. 
# Series 객체를 생성할 때 index 파라미터를 따로 지정하지 않으면 데이터는 0부터 시작하는 정수 인덱스를 갖습니다. 
# 하지만 index 파라미터를 지정하면 딕셔너리의 key-value처럼 index-value라는 관계를 갖고 저장됩니다.

# 2018-08-01 512 
# 2018-08-02 508 
# 2018-08-03 512 
# 2018-08-04 507 
# 2018-08-05 500 
# dtype: int64
# Series 객체를 생성할 때 인덱스를 지정하면 표 4-5와 같이 기존의 정수 인덱스와 추가된 인덱스가 함께 사용됩니다. 정수 인덱스가 화면에 출력되지는 않지만, 내부적으로 자동 설정됩니다.

# 표 4-5 인덱스를 추가한 Series의 내부

# 인덱스1	인덱스2	값
# 0	'2018-08-01'	512
# 1	'2018-08-02'	508
# 2	'2018-08-03'	512
# 3	'2018-08-04'	507
# 4	'2018-08-05'	500
# 따라서 512라는 값을 출력할 때 다음과 같은 두 가지 표현이 모두 가능합니다.

# print(s[0])
# print(s['2018-08-01'])

# Series 인덱싱/슬라이싱
# Series 객체에 저장된 값은 인덱스를 사용해서 얻어올 수 있습니다. 
# 파이썬 딕셔너리에서 keys()와 values() 메서드를 통해 모든 key와 value를 얻을 수 있었던 것처럼 Series 객체에서는 index와 values 속성을 통해 모든 index와 value를 얻을 수 있습니다.

# # ch04/04_11.py
# 1: from pandas import Series 
# 2: 
# 3: date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
# 4: xrp_close = [512, 508, 512, 507, 500] 
# 5: s = Series(xrp_close, index=date) 
# 6: 
# 7: print(s.index) 
# 8: print(s.values)
# 코드를 실행하면 우리가 흔히 사용했던 리스트는 아니지만 index와 value가 출력됩니다.

# Index(['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'], dtype='object') 
# [512 508 512 507 500]
# 파이썬 리스트에서 정숫값을 사용해서 인덱싱하거나 딕셔너리에서 key 값을 사용해서 인덱싱하는 것처럼 Series 객체 역시 index 값을 사용해서 인덱싱할 수 있습니다. 
# Series 객체는 여기서 하나 더 나아가 여러 index 값을 사용하면 동시에 여러 값을 한 번에 인덱싱할 수 있습니다. 
# 예를 들어 '2018-08-02'일과 '2018-08-04'일의 리플 가격을 얻어오려면 다음과 같이 코딩하면 됩니다.

# # ch04/04_12.py
# # 코드 생략
# 9: print(s[['2018-08-02', '2018-08-04']])
# 출력값을 확인해 봅시다. Series 객체를 인덱싱할 때 두 개 이상의 값을 사용하는 경우 인덱싱의 결과 역시 Series 객체임을 알 수 있습니다.

# 2018-08-02    508
# 2018-08-04    507
# dtype: int64
# 이번에는 Series 객체에 대해 슬라이싱 해보도록 하겠습니다. 
# Series 객체 생성 시 index를 따로 설정한 경우 기본적으로 사용되는 정수 인덱스에 추가로 설정한 인덱스도 사용됐지요? 
# 먼저 인덱스로 지정한 날짜 정보를 사용하여 슬라이싱 해보겠습니다.

# # ch04/04_13.py
# 1: from pandas import Series 
# 2: 
# 3: date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
# 4: xrp_close = [512, 508, 512, 507, 500] 
# 5: s = Series(xrp_close, index=date) 
# 6: 
# 7: print(s['2018-08-01': '2018-08-03'])
# 위 코드의 실행 결과를 살펴봅시다. 리스트 슬라이싱에서는 '[시작:끝]' 일 때 끝 인덱싱 값은 포함하지 않았습니다. 
# Series 객체에서는 정숫값이 아닌 사용자가 지정한 인덱싱 값으로 인덱싱하는 경우 끝 인덱싱 값도 포함합니다. 
# 그래서 s['2018-08-01': '2018-08-03']와 같이 슬라이싱하면 '2018-08-03'의 데이터까지 슬라이싱됩니다.

# 2018-08-01    512
# 2018-08-02    508
# 2018-08-03    512
# dtype: int64
# 정수값을 사용해서 슬라이싱하면 리스트와 튜플에서 배웠던 슬라이싱과 동일하게 끝값을 포함하지 않습니다.

# # 코드 생략
# 7: print(s[0:2])
# 정수 인덱싱를 사용한 결과 '2018-08-01'과 '2018-08-02'의 데이터만 슬라이싱 됐음을 확인할 수 있습니다.

# 2018-08-01    512
# 2018-08-02    508
# dtype: int64
# Series 추가/삭제
# 이번에는 생성된 Series 객체에 값을 추가하고 삭제해 보겠습니다. 
# Series 객체에 값을 추가하는 것은 딕셔너리와 동일합니다. 
# Series 객체에서 값 삭제는 drop() 메서드를 사용합니다.

# # ch04/04_14.py
# 1: from pandas import Series 
# 2:  
# 3: date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
# 4: xrp_close = [512, 508, 512, 507, 500] 
# 5: s = Series(xrp_close, index=date) 
# 6: 
# 7: s['2018-08-06'] = 490 
# 8: print(s.drop('2018-08-01')) 
# 9: print(s)
# 라인 7: 딕셔너리와 동일하게 추가할 key에 값을 대입해서 Series에 데이터를 추가합니다.
# 라인 8: Series 클래스의 drop 메서드로 ‘2018-08-06’ 키와 값을 삭제합니다.
# 라인 9: s가 바인딩하는 객체를 화면에 출력합니다.

# Series 객체는 drop 메서드를 호출하면 원본 데이터는 그대로 유지되고 특정 항목이 삭제된 새로운 Series 객체가 리턴됩니다.

# 2018-08-02    508
# 2018-08-03    512
# 2018-08-04    507
# 2018-08-05    500
# 2018-08-06    490
# dtype: int64
# 2018-08-01    512
# 2018-08-02    508
# 2018-08-03    512
# 2018-08-04    507
# 2018-08-05    500
# 2018-08-06    490
# dtype: int64
# Series의 연산
# 리스트, 튜플, 딕셔너리는 저장된 값에 사칙연산을 직접 적용할 수 없었습니다. 다음과 같이 리스트에 네 개의 값이 저장되어 있을 때, 나누기 연산을 시도하면 에러가 발생합니다.

# my_list = [100, 200, 300, 400]
# print (my_list / 10)
# TypeError: unsupported operand type(s) for /: 'list' and 'int
# 파이썬의 기본 자료구조는 반복문을 사용해서 모든 값을 가져온 후에 나누기 연산을 적용하고, 그 결과를 새로운 리스트에 저장해야만 합니다. 그렇다면 Series는 사칙연산에 대해 어떻게 동작할까요?

# new_list = []
# for val in my_list: 
#     new_list.append(val/10)
# Series 객체는 저장된 모든 데이터에 사칙연산을 적용합니다. 다음 코드에서 Series(변수 s)에 저장된 모든 값에 나누기10 연산이 적용됩니다.

# # ch04/04_15.py
# 1: from pandas import Series 
# 2: s = Series([100, 200, 300, 400])
# 3: print(s /10)
# 0    10.0
# 1    20.0
# 2    30.0
# 3    40.0
# dtype: float64
# 반환값이 Series라는 사실이 중요합니다. 새로운 리스트를 만들고 반복문을 사용하는 것보다 쉽죠? 이것이 Pandas를 사용하는 이유입니다.