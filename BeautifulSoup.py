import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html,"html5lib")
tags = soup.select("#_per")
tag = tags[0]
print(tag.text)

# ID가 없는 태그의 경우에는 HTML 문서에서 태그의 상대적인 위치를 나열함으로써 데이터를 파싱하는 다중 셀렉터를 사용해야 합니다. 
# 다중 셀렉터가 기억나지 않으신 분은 4.1.5절을 복습하고 오세요. 
# 그림 4-21에서 HTML 코드를 보면 외국인 소진율은 <table> 안에 <tbody> 안에 <tr> 안에 <td> 안에 <em> 태그 안에 들어 있습니다.
#  이를 CSS 다중 셀렉터로 작성하면 아래와 같습니다.
# tags = soup.select("table tbody tr td em")

#다중 셀렉터를 보다 구체화해 원하는 값만 선택해봅시다. 
# 그림 4-21의 HTML 코드를 자세히 살펴보면, table 태그에는 lwidth 클래스 속성이, tr 태그에는 strong 클래스 속성이 부여되어 있습니다. 
# 이러한 사항들을 CSS 셀렉터에 반영해 봅시다. 클래스 속성은 마침표와 클래스 이름을 적어주면 됐었죠? 8번 라인 코드를 아래와 같이 수정해서 실행해보세요.

# tags = soup.select(".lwidth tbody .strong td em")


#크롬 브라우저를 사용하면 다중 셀렉터를 쉽게 만들 수 있습니다. 
# 그림 4-22와 같이 외국인 소진율에 대응되는 <em> 태그에 마우스 오른쪽 버튼을 클릭한 후 Copy → Copy selector 메뉴를 선택합니다.

tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")
# 코드를 실행해보면 nth-of-type을 사용하라는 에러 메시지가 출력됩니다. 
# 이는 BeautifulSoup 모듈이 CSS 셀렉터를 100% 지원하지 않아 nth-child를 인식하지 못하기 때문에 발생하는 에러입니다. 
# BeautifulSoup은 특정 위치의 자식 태그를 선택할 때 nth-of-type()을 사용해야 합니다. 파라미터로 몇 번째 자식 태그인지 선택할 것인지에 대한 인덱스를 전달하면 됩니다. 


# 라인의 코드를 아래 같이 수정하면 외국인 소진율 48.96만 화면에 출력됩니다.
#  “tab_con1 > nth-of- type(2)”는 tab_con1 ID를 갖는 태그 안에 두 번째 div를 선택하라는 뜻입니다.
tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em")

for tag in tags:
    print(tag.text)