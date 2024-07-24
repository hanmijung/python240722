# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=humordata&no=2021640&s_no=15504120&kind=total&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 디코딩 
        page = data.decode('utf-8', 'ignore')
        #스프 객체 
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', 
                attrs={'class':'subject'})
        
          #v<td class="subject"><a href="/board/view.php?table=sisa&amp;no=1239744&amp;s_no=15504064&amp;
        #kind=total&amp;page=2" target="_top">노태우가 머리숱 많은 전두환이면</a><span class="list_memo_count_span"> [3]</span>   </td>

        # <span class="subject_fixed" data-role="list-title-text" title="아이폰12프로 128블루 (택포 39만)">
        # 	아이폰12프로 128블루 (택포 39만
        # </span>
        for item in list:
                #에러처리 구문"
                try:
                        #title = item.text.strip()
                        title = item.find("a").text.strip()
                        #print(title)
                        
                        if (re.search('한국', title)):
                                print(title.strip())
                        
                except:
                        pass
             
