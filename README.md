# Sogang-Portal

# 프로젝트 개요

## 프로젝트명
Sogang Portal

## 프로젝트 주제
학교 내 분산되고 사용자 경험이 좋지 않은 서비스들(모바일 학생증, 모바일 세인트, 서강톡톡 등)을 통합하고 소외된 사람 없이 인맥 커넥션이 가능한 크로스 플랫폼 웹앱

## 프로젝트 설명
평소에 학교 앱들을 사용하며 늦은 응답시간과 불편하고 제한적인 기능으로 불편함을 느끼고 있었던 서강대학교 학생들에게 편리하고 확장적인 기능을 제공함으로써 좀 더 윤택한 학교생활을 보낼 수 있을 것이라고 생각된다.

# 프로젝트 구조

![](http://cscp2.sogang.ac.kr/CSE4186/CSE4186/UserData/Flow_chart.png)

# 개발 내용

![](http://cscp2.sogang.ac.kr/CSE4186/CSE4186/UserData/SSS_Functions.png)

# 발표 자료
## 제안발표
[SSS단 프로젝트 제안 발표](https://docs.google.com/presentation/d/18DYEJCWu4yFunC44IADAZYT3pTJGqKVjfHwRkBmoOKo/edit?usp=sharing)





## 1. 개요

- 주제: 풀어야할 문제
<img width="608" alt="Untitled" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/4c7b28b6-513c-44ee-ab64-6509ae4f6b03">

   위에서 확인할 수 있는 바와 같이 기존 서강대학교의 공식 어플리케이션들이 UI/UX가 불편하고, 속도가 느리며, 기능에 많은 하자가 있음에 따라 사용자들에게 부정적인 경험을 초래하고 있다. 심지어는 이 얼마 되지 않는 기능들이 여러 앱에 분산되어 있어, 더욱 불편함을 호소하는 사용자들이 많다. 때문에 위의 앱에서 제공되는 부족한 양의 기능 조차 다수의 학생들이 모바일 웹을 통해 사용한다.

   또한 모바일 웹 또한 속도가 느리고 웹에서 모바일 기능을 지원하지 않는 경우도 있어 이외의 기능들, 크게 시간표와 게시판 기능을 외부 프로그램에 의존하고 있는 실정이다. 외부 프로그램들은 아무래도 서강대학교의 실정과 맞지 않는 부분들이 있어,  이 역시 학생들에게 부정적인 경험을 안겨주지만 다른 대안이 존재하지 않기에 어쩔 수 없기 계속 사용하고 있는 상황이다.

   따라서 서강대학교의 여러 어플을 통합하고 외부 프로그램들의 기능 또한 추가하여 기능적으로도 개선되고, 속도, UI/UX 측면에서도 개선되어 학생들의 불편을 해소시킬 수 있는 어플을 개발하고자 하였다.

- 목표: 제안목표 (수정 시 변경 사유 포함)

1. 서강대학교에서 공식적으로 제공하는 어플리케이션의 기능들을 통합한다. 기능들은 다음과 같다.

   -모바일 학생증: QR코드를 통해 서강대학교 시스템 전반에서 사용할 수 있는 모바일 학생증 기능을 가져온다.

   -모바일 세인트: 서강대학교 세인트를 통해 학생의 정보를 불러와, 각 학생들에게 제공해주는 기능을 가져온다.

   -사이버 캠퍼스: 사이버 캠퍼스의 정보를 불러와 각 학생이 수강하고 있는 과목들의 정보 제공하는 기능을 가져온다. 기존에는 사이버 캠퍼스의 공지들을 앱 알림으로 보내는 시스템까지 개발하려 했으나, 사이버 캠퍼스 자체가 외부에서 개발한 프로그램이라 굉장히 복잡한 구조로 이루어져 있고 보안이 강력한 이슈로 인해, 미구현하는 것으로 결정하였다. 

   -서강톡톡: 현재 유용하게 사용되는 기능이 없어 배제되었다.

2. 현재 외부 프로그램을 통해 사용되는 부분을 어플리케이션의 기능으로 추가한다.

   -시간표: 위의 학생 정보를 통해 시간표를 자동으로 작성해주고, 추가로 사용자 개인 일정(아르바이트 등) 추가 가능하도록 개발한다.

   -게시판: 세인트 ID를 통해 자동으로 가입되는 커뮤니티 기능을 추가한다.

3. 위 각 기능 들에 더해, 접근하기 어려웠던 서강대학교 요람, 학교 공식 사이트를 통해 얻을 수 있던 정보로 학습된 AI Chat bot 기능을 통해 이 정보들을 쉽게 찾을 수 있도록 한다. 기존에는 추가 기능으로 서강대학교 내부 지도를 3D 안내도로 제작하려 하였으나, 대상자인 서강대학교 학생들이 대부분 서강대학교의 지리에 익숙하여 안내도의 수요가 적을 것으로 판단하여 이 기능은 배제하였다. 

4. 데이터베이스 정규화와 다른 최적화 알고리즘, 시스템 디자인들을 통해 안정성을 높이면서도 빠른 앱을 개발하여 기존 어플리케이션을 완전히 대체할 수 있도록 개발 목표를 설정한다.

- 프로젝트 성과


  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/7c7096b0-29e5-460b-8f6e-701108a2ef14">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/494f990e-fd8e-4dd4-b15c-02bff5c95378">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/13606fd5-7081-4674-bbc6-c868177966fc">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/0e24f6e5-1f28-4ae7-bda7-e9ee46b7ccee">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/dec3c7a7-51af-44b6-a48c-31c16cc1c706">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/f2ce3a73-1311-40d5-924a-059afbc59724">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/5c3d6ca0-f503-420e-bbfb-2ddea9b6c7d1">
  <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/ba315e02-6ba6-4eac-a6ec-f6e9567687b0">



   위의 목표들을 모두 이루기 위해서는 웹 앱으로 개발하는 것이 가장 효과적일 것이라 생각하여, 웹 앱의 형식으로 개발되었다. 위의 목표를 구현하기 위해 각각의 기능들에 대해 여러 방법들을 사용하여 독립적으로 개발하였으나, 각 기능이 유기적으로 동작할 수 있도록 개발하였다. 따라서 앱의 안정성이 향상되었고, 속도 면에서도 기존 공식 어플리케이션에서 2~3초의 로딩 시간이 필요한 부분들도 모두 사용자가 알아차리기 힘든 만큼 빠른 속도로 로딩되며, UI/UX 또한 여러 기능이 한 눈에 들어오도록 디자인 되었다. 

   웹 앱으로 개발된 것의 또다른 큰 장점으로, 결과물이 플랫폼에 제약받지 않고 여러 플랫폼에서 유연하게 작동한다는 점도 있었다.

## 2. 추진체계

- 팀구성: 팀원 구성 및 역할

  **강상원(20191559): 팀장**

  - 백엔드 담당
  - 크롤링, 얻은 정보 데이터베이스 저장
  - UI/UX 반응형 디자인
  - Sogang GPT 학습
  - 개발환경 통합 및 진행과정 총괄, Wiki 작성

  **임형진(20191639): 팀원**

  - 백엔드/프론트 엔드 보조
  - 데이터베이스 구현
  - 게시판 개발
  - UI/UX 디자인
  - 발표자료, 보고서 총괄

  **황성민(20191669): 팀원** 

  - 프론트 엔드 담당
  - 시간표 개발
  - 크롤링의 규격과 데이터베이스의 규격간의 전환 함수 개발
  - UI/UX 디자인

- 프로젝트 관리: 관리체계, 규약, 방법론 등

  - SSS단은 매주 목요일 저녁 5:00~8:00 학교 내 오프라인 정기 모임을 가지고, 그 이외에 비정기적인 모임을 상시로 가지기로 하였다. 5학기생 컴퓨터공학과 동기이기에 수업 등 일정의 조율의 용이함이 있었다. Notion mention 기능을 통한 상호 개발 과정 공유, 의견 전달 과정도 이루어졌다.
  - 피치 못할 사정으로 미리 정의한 회의 시간에 진행이 어려울 경우, 최소 20분 전 회의시간 변경에 대해 노티하고 재조정함을 원칙으로 하여 회의 날짜에 대한 혼선을 피하였다.
  - 개발 과정, 회의 내용 등 전반 모든 과정을 Notion에 체계적으로 기록하여 향후 회의록 작성, 보고서, 발표자료를 만드는 데 있어 활용되도록 하였다.

   프로젝트는 IEEE 표준에 따라 6단계로 진행하는 것으로 결정지었다. 6단계는 각각 Analysis(요구사항 분석), Design(프로그램 디자인), Development(개발), Testing(테스트), Implement(적용), Maintenance(유지보수)로 나뉘는데, 최대한 이 방향성을 따라가는 것으로 결정하였다.

   협업을 하는 것에 따라 개발 규정을 정하는 것이 중요하였다. 개발 규정은 구두 회의를 통해 결정하였고, 이후에 조금씩 수정하며 협업을 이어나갔다.

  - 각자에게 독립적인 기능을 개발하도록 개발 부분을 배정하여 개발간의 불필요한 의견 충돌이 일어나는 일을 피할 수 있도록 하였다. 공유되는 부분인 데이터베이스와 크롤링 정보 저장 부분을 독립적인 프로그램으로 구현하고 쉽게 사용할 수 있도록 메서드를 구현하여 협업의 효율을 높였다.

  - JSDoc을 사용하여 각 개발 모듈별 인자, 반환값 타입 힌트를 제공하고 협업 시 서로 모듈의 사용 용도를 파악하기 용이하게 하였다.

    ```python
    def get_saint_cookies(id, pw):
        """
        모바일 세인트 로그인 후 쿠키를 받아오는 함수
        @param id: 학번
        @param pw: 비밀번호
        @return: 세션 쿠키값
        """
        # 세션 만들어서 쿠키 값을 받아오기
        login_url = "https://msaint.sogang.ac.kr/loginproc.aspx"  # 모바일 세인트 로그인 주소
        header = {
            "User-Agent": "Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 \
                (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
        }
    		...
    ```

   다양한 언어/도구를 사용하여 개발이 진행되기에 각종 환경을 통일하는 것이 필요하였다. Django를 메인으로 사용하기에 개발 도구로 pycharm을 채택하였고, requirments.txt 문서를 통해 각자의 파이썬 인터프리터가 모두 같은 기능을 가질 수 있도록 하였다. 버전 관리는 github의 공유 리포지토리를 이용해서 진행하였다. 기타 프로젝트 관련 회의는 대면 회의로 진행하여 내용을  Notion을 통해 저장하였다.

   위 내용을 요약하여 작성하자면 다음과 같다.

   [프로젝트 개발환경]

  - [Backend] Django
  - [Database] SQlite
  - [Version Control] GitHub
  - [UI/UX] Figma
  - [Documentation] Notion
  - [File Transfer] Google Drive

- 개인별 기여사항: 역할에 따른 개발범위, 주요이슈


  강상원[백엔드]

  백엔드(크롤링):

  - 개발 범위: 모바일 세인트, 사이버 캠퍼스, 개설 교과목 크롤링 로직 구현

  - 주요이슈: Web Dynpro를 이용하여 동적으로 생성되는 교과목 정보 return 값에 대한 크롤링 구동

  - 문제해결: Web Dynpro를 이용하여 교과과정 정보를 동적으로 생성하고 반환하는 값에 대한 크롤링 구동 및 크롤링 대상 URL의 동적인 변경을 처리하는 로직을 구현. 최종적으로, 이러한 로직을 구현하여 웹 애플리케이션에서 교과과정 정보를 자동으로 업데이트

  - 성과명시: 대학교 과목 크롤링, 모바일 세인트 및 사이버 캠퍼스 크롤링 로직 구현. 각 웹 애플리케이션의 동작 방식을 이해하고, 데이터베이스와의 상호작용 방법을 측정. 크롤링된 데이터를 처리하고 저장하기 위한 데이터 구조와 알고리즘 설계

    속도 면에서 기존 어플리케이션 대비 2~3초 단축 (개설교과목 조회 한 28초 이상), 사용자 경험 개선

  GPT 학습, Fine Tuning:

  - 개발범위: Sogang GPT 개발

  - 주요이슈: pdf, 이미지 파일 등 여러 형식으로 되어 있는 학교 관련 자료, 정보들을 기존 OpenAI의 API에 적용하기에 한계 /  프롬포트 입력 길이 제한 또한 존재

  - 문제해결:  LlamaIndex를 이용하여 PDF 파일, 이미지 등의 학교 자료를 학습시켜 natural-language query로 학습시킨 결과 노드 인덱스 추출

  - 성과명시:  Generate한 Large Language Model을 이용해 ChatGPT Davinchi model을 fine-tuning

    각 사용자마다 접속할 때 서로 다른 채팅이 열려 독자성 확보 / 개인정보 침해 문제를 미연 방지

  UI/UX:

  - 개발 범위: 앱 전반
  - 주요 이슈: 반응형 UI/UX 디자인, 디자인 트렌드에 맞고 시인성도 챙기는 구조 지향
  - 문제해결: 다양한 기기에서 앱 사용 측면 고려, 모든 기기에서 앱을 사용할 수 있도록 반응형 디자인 적용, 화면의 크기와 해상도에 맞게 UI/UX가 자동으로 조정.Windows, Mac OS 및 각종 모바일 기기에서 점차 상용화되어가고 있는 Neumorphism 적용
  - 성과 명시:  기존의 플랫 디자인과 조각감 있는 디자인을 혼합해 비교적 세련되고 현대적인 느낌을 줌. 사용자에게 더욱 직관적이고 쉽게 접근할 수 있는 디자인 제공

  앱 기능 통합:

  - 개발 범위: 각 앱 대상 핵심 기능들 로직 파악, cookie 인자 값과 유효기간 분석 통한 사용자 인증
  - 주요 이슈: 모바일 학생증(QR code) 생성 로직 알아내기 및 구현
  - 성과 명시: 각 앱 apk 파일 디컴파일을 통해  request uri 분석, Dummy data 보내기 포함 여러 방식으로 로그인 폼 정보 전달 방식 추출

  임형진[데이터베이스]

  데이터베이스:

  - 개발범위: 데이터베이스 구현
  - 주요이슈: 다중 데이터베이스 트랜잭션 처리, 데이터베이스 objects manager 구동
  - 문제해결: Django ORM의 transaction.atomic()을 이용한 트랜잭션 처리, Django manager에서 objects manager 직접 상속받아 해결.
  - 성과명시: 안정적인 데이터베이스 구현으로 앱 전반적인 안정성 향상, 사용자 데이터 보호

  UI/UX:

  - 개발범위: UI/UX 디자인
  - 주요이슈: 반응형 웹 디자인
  - 문제해결: trailwind css를 이용하여 반응형 웹 디자인 후 Django template 사용하여 url 링크.
  - 성과명시: 사용자 친화적인 UI/UX 디자인으로 사용성 향상

  게시판:

  - 개발범위: 게시판 개발
  - 주요이슈: 데이터 유효성 검사 및 클라이언트에서 서버로 보내는 데이터 안정성 검사
  - 문제해결: Django Forms와 ModelForm을 이용한 데이터 유효성 검사, 데이터베이스 항목 추가하여 데이터 진위여부 확인. CSRF token 알고리즘 사용하여 데이터 안정성 검사.
  - 성과명시: 안정적인 게시판을 구현하였고, 게시판에 사용된 코드와 모델을 다른 UI 및 모델에도 사용

  사용자 프로필:

  - 개발범위: 사용자 프로필 개발
  - 주요이슈: 프로필 사진 업로드 및 저장
  - 문제해결: AWS EC2를 사용하여 업로드된 이미지를 저장하고, 해당 이미지 URL을 프로필과 연결
  - 성과명시: 안정적인 프로필 업로드 및 이미지 저장 기능을 구현하여 사용자 경험 향상

  황성민[프론트엔드]

  프론트엔드:

  - 개발범위: 백엔드와 데이터베이스에서 정보를 가져와 유저와 정보를 주고받는 프론트 엔드 개발
  - 주요이슈: 개발자끼리의 데이터베이스 충돌, 백엔드에서의 크롤링과 데이터베이스에서 요구하는 규격의 차이
  - 문제해결: 개발자 개개인의 데이터베이스 상태를 고려하여 데이터베이스에 추가 저장 혹은 제거를 하여 현재 커밋버전에 맞는 데이터베이스 상태를 공유, 백엔드 → 데이터베이스, 데이터베이스 → 백엔드로의 규격을 맞추는 함수를 만들고 추상화시켜 누구나 접근할 수 있도록 함
  - 성과명시: 일정시간에 한번씩 크롤링을 계속 하여 자동으로 유지보수가 되는 앱을 구현하여 시간이 지나도 오류가 생길 가능성이 확연히 줄어듦

  시간표:

  - 개발범위: 시간표 개발
  - 주요이슈: 데이터베이스에서의 규격을 html에 전달, 시간표의 불러오기 팝업 검색 등 기능 추가
  - 문제해결: 장고에서 데이터베이스의 규격을 html에 전달할 함수를 짜서 html에 제공, 자바스크립트를 이용하여 현재 유저의 강의의 개수에 따라 특정 위치에 시간표를 만들어 주고 팝업 또한 자바스크립트를 이용해 특정 버튼을 누르면 나오는 이벤트를 받아 팝업창을 visible하게 바꾸게 하였고 팝업창 이외의 것을 클릭하면 unvisible하게 변경하였고 검색 또한 자바스크립트를 통해 검색된 결과만을 보여주는 기능을 제작하였다.
  - 성과명시: 데이터베이스에 있는 정보를 유저가 보기 편하게 제공받을 수 있게 되었고 시간표에서 다양한 기능을 통해 유저의 편의를 증대함

  UI/UX:

  - 개발범위: UI/UX 디자인
  - 주요이슈: 반응형 웹 디자인, 시간표 블럭 크기
  - 문제해결: teleportHQ를 사용하여 html을 추출한후 자바스크립트로 조정, 자바스크립트를 통해 시간과 요일에 따른 크기 및 위치를 계산하여 css를 불러와 html에 추가
  - 성과명시: 시간표를 보다 효율적이게 계산하여 유저가 볼 수 있도록 제작함

## 3. 개발내용

- 개발범위

  1. 프론트엔드

     - 홈화면, 모바일 학생증, 시간표, 게시판, 설정, 기능(각종 학교 웹사이트의 기능 링크, Sogang GPT)에 대해 구현한다. Sogang GPT란 Chat GPT에 서강대학교의 정보를 학습시켜 정보 검색을 용이하게 해주는 기능을 의미한다.

  2. 백엔드

     - 크롤링을 위해 서강대학교 또는 사이버캠퍼스 서버와 통신을 할 때 마다 그에 맞는 서버 프로토콜 환경을 조성하여 서버에 request를 보내고 쿠키값을 얻어와 그 쿠키값으로 서버와 통신을 주고 받는다.
     - 유저에게서 데이터베이스에 있는 내용이 필요한 프론트엔드부분을 확인할 때 마다 데이터베이스에서 알맞게 정보를 가져와 html에 전달하여 유저가 볼 수 있도록 구현한다.
     - 유저가 생성되거나 로그인하거나 일정 시간 마다 유저에 가지고 있어야할 정보들을 크롤링해서 데이터베이스에 저장시키고 유저가 유저에 한해서만 사용될 정보를 추가할 정보를 저장(ex 시간표 추가)을 할때 마다 데이터베이스에 저장시킨다.
     - 서버가 시작되거나 일정 시간마다 개설교과목등 서버가 가지고 있어야할 정보들을 새로 크롤링해오고 데이터베이스에 저장시키고 유저 혹은 서버에서 추가적인 정보를 저장(ex 게시물 생성)을 할때 마다 데이터베이스에 저장시킨다.

  3. 데이터베이스
     
     <img width="637" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/1d158a2c-25dc-43e6-a387-c5a1f23faa45">

    

     Database diagram

     - 데이터베이스의 relation을 정립하고 relation들 끼리의 관계를 구상한 후, Django의 Model을 사용하여 구현한다.
     - 각 데이터베이스에 접근이 용이하도록 메서드를 작성한다.

- 시스템 또는 SW 구조
    
   <img width="585" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/87465015-7a7a-48fc-9bf3-a50aa2a4deef">

  

  프로젝트 구조도

  - 서버 측에서 서강대학교 웹사이트를 크롤링한 후 데이터베이스에 저장하고, 클라이언트의 요청이 있을 시에 서버에서 필요한 정보를 전송한다. 위 일련의 작업은 Django를 통해 구현되었으며, 데이터베이스는 SQLite를 통해 구현되었다. 즉 대부분의 백엔드 작업(크롤링, 어플리케이션 로직, 서버/클라이언트 간 통신)은 모두 Django를 통해 구현되어 있다.

   ![image](https://github.com/kevink1113/Sogang-Portal/assets/48401272/f4824838-c5fd-46f9-bf0c-7f309cdb642d)

  

  Figma 디자인 초안

  - UI/UX는 Figma로 시제작 후, TailwindCSS를 통해 css html 코드로 만들어, 반응형 웹으로 사용할 수 있게 하였다. 여기에 Django의 html 템플릿 코드 기능을 사용하여 앱의 각각의 기능들을 사용자 화면에 링크해주었다. 위에서 구현한 기능들을 AWS EC2를 통해 실제 서버에서 실행시킬 수 있도록 하였다.

  - Sogang GPT 개발 관련
   <img width="339" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/3b302300-fc15-4a54-aad4-365d558115a3">

  기존 OpenAI의 ChatGPT API는 유료 계정까지도 프롬포트 입력 길이, 횟수가 제한되어 있기에 요람 등 800페이지가 넘는 자료를 해당 API를 통해 한번에 학습시키는 것은 불능에 가까웠으며, 결과의 신뢰성 또한 보장하지 못하였다. 이에 LlamaIndex를 이용하여 PDF 파일, 이미지 등의 학교 자료를 학습시켜 natural-language query로 학습시킨 결과 노드 인덱스를 얻는다. 

  Generate한 Large Language Model을 이용해 ChatGPT Davinchi model을 fine-tuning하였다. 

  각 사용자마다 접속할 때 서로 다른 채팅이 열려 독자성 확보 / 개인정보 침해 문제를 미연에 방지하였다. 
  <img width="416" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/f94526a9-b4e3-458b-8da8-8ded991c9c20">

  

  학습을 통해 Generate한 Node Index 일부

- 개발내용: 주요구성요소, *설계고려사항, 특장점(프로젝트 독창성) 등 포함*


  [주요구성요소]

  상단바를 통해 현재 메뉴 또는 Sogang Link(앱 이름)을 확인할 수 있도록 하였고, 하단바는 반응형으로 설계하여 화면에 표시된 각각의 메뉴들을 클릭해 메뉴를 이동할 수 있도록 구현하였다. 

  1) 홈화면

  현재 로그인한 학생의 학사 정보와 공지, 과제 목록 그리고 당일의 시간표를 나타내 유저가 현재 필요한 정보와 최신 학사 정보를 효율적으로 얻을 수 있도록 한다.

  1-1) 모바일 학생증

  홈화면에서 학생정보를 클릭하면 학생증을 확인할 수 있도록 한다. 화면에 표시된 QR코드를 통해 도서관 출입이나 열람실 예약 등 기존의 학생증 QR코드와 동일한 일을 할 수 있도록 한다.

  2) 시간표

  현재 학기 또는 상단바에서 선택된 학기에 수강하거나 추가 또는 직접추가한 시간표를 불러와서 시간표 형식에 맞게 확인할 수 있도록 하였고 해당 학기의 개설교과목에 있는 시간표를 추가하거나 아니면 직접 강의를 만들어 추가 할 수 있도록 제작함. 또한 시간표를 클릭하여 수정 및 삭제가 가능하도록 하였고 강의정보를 확인하여 그 강의에 대한 자세한 정보와 성적을 확인할 수 있도록 한다.

  3) 게시판

  게시판의 분류를 header의 기능에 넣어 게시판의 분류에 따라 노출되는 게시물을 상이하게 구현함. 게시판에 처음 들어가면 nickname을 설정하고 그 nickname대로 자신과 다른 유저들에게 노출이 됨. 분류를 설정하고 게시글을 작성하면 분류에 맞게 게시글이 이동하고 게시글에는 사진 지도 동영상등을 첨부할 수 있다.

  4) 설정

  현재 이 앱에서 사용하는 프로필 사진과 nickname을 변경할 수 있다.

  5) 기능

  이외에 유용하게 사용할 수 있으나, 위의 메뉴 들에 대해 우선순위 적으로 부족한 기능들을 한눈에 확인할 수 있도록 하는 메뉴이다.

  5-1) 학식, 열람실 현황, 서강대학교 메인페이지, 학사일정, 웹메일

  각각을 확인할 수 있는 링크로 redirection하여 해당하는 항목에 대해 확인할 수 있도록 한다.

  6) Sogang GPT

  GPT를 서강대학교 안내 및 도우미로 사용할 수 있도록 학습시켜 서강대학교 전용의 gpt를 제작한다.

  [설계 고려 사항]

  1) 서강대학교 학생을 타겟으로 삼았기에, 집단의 특수성을 고려하여 어플리케이션의 기능을 배치하고 UI 역시 이를 충분히 고려하여 설계한다.

  2) 저장해야 하는 정보량이 충분히 크기 때문에, 이를 효율적으로 저장할 수 있도록 데이터베이스 설계시 중복이 발생하는 것을 최대한 피한다. 또한 각각의 기능들을 설계할 때 데이터베이스에서 전탐색 하는 것을 최소화하여 딜레이가 발생하는 것을 최대한 방지한다.

  3) 위의 기능들이 독립적으로 작동할 수 있도록 개발하여, 버그가 발생하더라도 다른 기능에 까지 영향을 주지 않도록 한다.

  4) Django에서 개발하는 것으로 기본적으로 여러 플랫폼에서 사용할 수 있으므로, UI/UX 또한 추가로 여러 플랫폼에 맞게 최적화되도록 설계하여 다양한 플랫폼에서 유연하게 사용할 수 있도록 설계한다.

  5) 어플리케이션의 데이터베이스가 민감한 정보를 다수 포함하기에, Django에서 제공하는 기본적인 보안에 더해 추가로 보안 관련 알고리즘을 사용하여 데이터 안정성을 높인다.

  [특장점]

  1) 기존의 서강대 공식 어플리케이션의 기능을 한 어플리케이션에서 모두 사용할 수 있다.

  2) 위에 더해 외부 프로그램들에서 사용하던 기능 또한 한 어플리케이션에서 사용할 수 있도록 하므로, 기능적인 측면에서 기존의 앱에 비해 월등한 장점을 가진다.

  3) 기존의 다른 외부 프로그램을 사용하기 위해선 각각의 프로그램에 새로 가입을 하고, 학생증 등을 이용하여 인증하는 방식을 거쳐야 하였지만, 서강링크를 사용하였을 때는 서강대학교 학생들이 모두 보유하고 있는 세인트의 아이디와 비밀번호를 통해 로그인할 수 있어, 별도의 가입이 필요없다.

  4) 위의 외부 프로그램들의 정보는 유저가 직접 기입해야 했지만, 서강링크는 유저의 정보를 이용한 크롤링을 통해 학생의 정보를 자동으로 받아와 제공해준다. 유저가 직접 기입할 수 있는 기능 역시 유지하여, 사용자 설정 시간표 등도 제작할 수 있도록 한다.

  5) 일반적으로 어플리케이션의 기능이 많아질 수록 속도는 저하되나 기존의 어플리케이션들에서 사용되는 알고리즘을 개선하고 불필요한 리소스 사용을 최소화시켜 속도를 향상시킨다.

- 이슈 및 해결방안

  - 비밀번호 저장으로 인한 개인정보 보안 이슈

    사이버캠퍼스, 서강톡톡 등 크롤링: 로그인 유지 처리 방법 관련, 정통법에서는 로컬 파일에 저장하면 필수적으로 일방향 암호화 (해쉬)를 해야 하지만 데이터베이스와 같은 경우 양방향 암호화를 해도 무관하다고 명시됨. 따라서 데이터베이스에 암호를 저장할 때 양방향 암호화를 하면 가능. -> 실 비밀번호 받아오기에 제약. 로그인 유지는 쿠키 값 또는 세션 유지로 처리 가능.  

    SAINT 사이트에서 쿠키를 받아와서 하면 세션이 만료가 되지 않지만, 사이버 캠퍼스같은 경우에는 세션이 하루 안에 만료가 되어 유저가 하루마다 다시 접속을 해줘야하는 문제가 있다. 이를 해결하기 위해 비밀번호를 받는 등 여러가지 방법이 고려되었으나 멘토링 결과 정보통신법에 위반될 가능성이 있어 비밀번호를 받지 않는 방향으로 진행하였다. 

    따라서 비밀번호를 저장하지 않으면서 세션을 유지하기 위해서는 서버에 쿠키를 저장해두고 그 쿠키를 이용하여 세션이 만료될 때 마다 세션을 연장시켜주는 방식을 채택하여 진행하였다. 
    
    <img width="582" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/b8adc7f2-3fb4-4ac4-8e5a-a1f0ca0bb377">

    

  - 개설교과목 Crawling 작업

    개설교과목 정보에 대해서는 서강대학교가 SAP 웹 디렉프로 (Web Dynpro) 프레임워크를 사용하여 개발하였다. 이 프레임워크는 웹 브라우저에서 사용자 인터페이스를 제공하고, 백엔드 시스템과 통신하여 데이터를 처리하고 표시하는 기능을 제공한다. 서버가 각 검색에 독립적인 아이디 값을 할당하여 식별하고, 이에 대해 검색 요청 결과를 반환하기에 동적인 웹 페이지를 처리하는 데 유용한 Selenium 라이브러리를 사용할 수밖에 없었다. 

    <img width="200" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/b5c643a1-5a85-4f74-a3d5-6e8f08804245">
    Selenium
    <img width="200" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/4f582512-906e-45d7-8a81-7fc60b841246">
    Python Requests
    



    그러나 Selenium은 requests 라이브러리와 다르게 실제 가상 웹 브라우저를 띄워 실행하기 때문에 자동화 작업이 request보다는 느리고, 브라우저를 제어하기 위해 시스템 리소스를 고모한다는 단점이 있었다. 이에 DB의 핵심 축을 담당하는 Takes relation의 정보 입출력이 시간 소모적일 수 있다는 우려가 있었으나, 이는 모든 학생들이 공통의 개설교과목 풀을 사용하고, 교과목 정보가 매시간 업데이트가 일어나지 않는 정보이므로 사용자 로그인, 세션 이벤트와 async하게 처리할 수 있었다. Selenium을 통한 개설교과목 정보 크롤링은 1일에 한 번 업데이트를 하는 방향으로 하였고, Python의 BackgroundScheduler을 사용해 이러한 반복 작업 처리를 다뤘다. 

    이수, 시간표 등 DB 관련 정보들과 함께 업데이트 되도록 한다는 문제를 해결하기 위해 데이터베이스 트랜잭션을 이용한 처리 방식을 도입하였다. 크롤링 결과를 받아와 이를 기존 DB와 비교하여 업데이트를 진행하는 과정에서 이를 하나의 트랜잭션으로 처리하였으며, 이 과정에서 문제가 발생할 경우 트랜잭션 롤백을 통해 이전 상태로 되돌릴 수 있도록 하였다. 이를 통해 교과목 정보 업데이트 과정에서 DB의 일관성을 유지할 수 있었다.


    <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/d8c44141-b2c7-4688-823c-f4a4392413fc">
    
    자동화된 Selenium 크롤링 과정
    <img width="566" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/3476d9c6-468a-4d81-9966-1fe073d72163">

    동적 페이지 크롤링 코드 일부

  - 게시판 관련 이슈

    한 유저가 한 게시물에 여러 차례 접속하거나 한 게시물에 대해 여러 차례 추천할 경우에 그것이 조회수/추천수에 모두 반영되는 이슈가 발생하였다. 기존의 데이터베이스를 사용하여서는 각 추천/조회가 반영되어야 할 지를 확인할 수 없었기에, 데이터베이스의 수정이 필요하였다. Django model의 ManyToManyField를 활용하여 각각의 글에 어떤 사용자가 조회/추천하였는지를 저장하는 방식으로 문제를 일부 해결하였으나, 이렇게 할 시에 각각의 글을 불러올 때마다 필드를 전탐색해야하는 문제가 발생하여, 데이터베이스에 조회수, 추천수만 저장하는 column인 view_num, upvote_num을 추가하여 이를 해결하였다.

    게시판에 사진을 업로드하는 기능 구현에도 한차례 이슈가 발생했다. 초기 개발 부분에서는 미디어 파일을 모두 한 폴더(static 폴더)에 저장하는 방식으로 구현되었다. 그러나 게시판을 구현하는 과정에서 많은 양의 사진을 저장해야할 필요가 생겼는데, 이는 기존의 방식으로 구현하였을 때 오버헤드가 발생할 수 있는 부분이었다. 이 이슈를 해결하기 위해 서버가 디버깅될 때 각각의 미디어 파일 호출이 모두 static 폴더에 있는 파일을 호출하는 것처럼 만들어(실제로는 다른 폴더를 링크한다), 원래의 저장 방식을 바꾸지 않으면서도 미디어의 저장을 다른 폴더에 할 수 있도록 하였다. 이때 개발된 방법을 통해 프로필에 사진을 업로드 할 수 있는 기능 또한 추가되었다.

## 4. 성과

- 목표치: 기능, 성능(정량, 정성) 목표

### 기능 목표

- 모바일 학생증: QR코드를 통해 서강대학교 시스템 전반에서 사용할 수 있는 모바일 학생증 기능 개발
- 모바일 세인트: 서강대학교 세인트를 통해 학생의 정보를 불러와, 각 학생들에게 제공해주는 기능 개발
- 시간표: 위의 학생 정보를 통해 시간표를 자동으로 작성, 추가로 사용자 개인 일정(아르바이트 등) 추가 가능하도록 개발.
- 게시판: 세인트 ID를 통해 가입할 수 있는 커뮤니티 기능 추가.
- AI Chat bot 기능을 통한 학교 정보 검색 기능 추가

### 정량/정성 목표

1. 모바일 학생증, 모바일 세인트, 시간표, 게시판, AI Chat bot 기능들의 안정적인 구현으로 앱 전반적인 안정성 향상
   - [Backend] Django를 사용하여 대부분의 부분을 구현
   - [Database] SQLite를 통해 데이터베이스를 구현
   - [Frontend] CSS, HTML를 사용하여 UI/UX를 구현
   - 위의 개발 도구의 기본적인 보안 능력에 더해 csrf.token 알고리즘을 사용하여 외부의 공격에 대한 서버의 안정성 증가

2. 데이터베이스 정규화와 다른 최적화 알고리즘, 시스템 디자인들을 통해 빠른 앱 속도 향상
   - [Backend] Django ORM을 사용하여 데이터베이스 정규화
   - 다중 데이터베이스 트랜잭션 처리, 데이터베이스 objects manager 구동 문제를 Django ORM의 transaction.atomic()을 이용해 해결
   - SQL 쿼리 최적화를 위해 Django ORM을 사용하여 쿼리를 최적화, 서버에서 크롤링 등의 데이터 처리하는 시스템 디자인 사용.

3. 사용자 친화적인 UI/UX 디자인으로 사용성 향상
   - [UI/UX] Figma를 이용하여 UI/UX 디자인을 구현
   - 반응형 웹 디자인을 구현하기 위해 trailwind CSS를 사용

4. 안정적인 게시판과 프로필 업로드 및 이미지 저장 기능을 구현하여 사용자 경험 향상
   - [Backend] Django Forms와 ModelForm을 이용하여 게시판 데이터 유효성 검사를 구현
   - [Backend] AWS EC2를 사용하여 프로필 이미지 업로드와 저장을 구현
   - [Frontend] CSS, HTML을 사용하여 프로필 페이지 및 이미지 업로드 기능을 구현

5. 안정적인 데이터베이스 구현으로 앱 전반적인 안정성 향상, 사용자 데이터 보호
   - [Backend] Django ORM을 사용하여 앱 안전성 향상시키고 개인 데이터를 쿠키로 저장하는 것으로 구현.

- 프로젝트 산출물

  - 로그인 및 메인 페이지, 모바일 학생증


    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2015.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%202.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2016.png)

    - 기존 Saint 아이디를 사용해 손쉽게 로그인, 각종 기능 하단 네비게이션 바에서 손쉽게 접근
    - 학교 최신 공지사항 손쉽게 확인, 모바일 학생증 사용, 해야 할 일 확인
      - 독립적인 앱으로 있던 모바일 학생증 기능 통합, 학생증 QR 생성 알고리즘 파악

  - 시간표


    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%203.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2017.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2018.png)

    실제 이수 과목 반영, 개설교과목 주기적 갱신으로 최신화 / 과목별 성적, 정보 통합 확인

    사용자 정의 일정 추가, 삭제로 일정 통합 관리

  - 게시판


    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2019.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2020.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%204.png)

    인증된 학우들과의 커뮤니케이션, 맛집 게시판 등 정보 공유 활성화 / 첨부 내용, 양식의 다변화

  - 기능들


    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2021.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2022.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2023.png)

    열람실 좌석 / 학식 / 학사일정 / 웹메일 등의 기능 종합

  - Sogang GPT


    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%201.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2024.png)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2025.png)

    개설교과목, 학교 시설, 규정, **기타 정보**에 대한 이해

    궁극적인 학교 생활 도우미가 되는 것을 목표로 삼았다. 

- 멘토 평가의견: 필수(* 근거자료 별지 첨부: email, 평가의견서 등)

  ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2026.png)

## 5. 검증

- 검증결과: (성능, 품질 검증) 시험방법, 시험결과치

### 성능, 품질 검증

성능은 개설교과목 및 학사 관련 정보 조회(GPT) 속도 측정 등을 통해 정량적인 측정이 가능하다. 또한 정성적 측면에서 접근성, 가독성, 다양성, 신뢰성, 신속성을 측정하여 프로젝트의 품질에 대한 개략적인 검증을 할 수 있다. 자세한 내용은 후술한 바와 같다. 

- 개설교과목 조회 속도

  측정 환경:  80Mbps 무선랜 환경으로 통일, 총 5회 측정 평균값 도출

  - 기존 개설교과목 정보 조회:  페이지 로딩 평균 **1.37초**, `2023학년도 1학기`: `대학 구분` 필터 적용 검색 소요 시간 평균 **27.42초**로 **도합 28.79**초 소요.
  - Sogang Link: 페이지 로드 시간 평균 **0.53초**, `2023학년도 1학기`: `대학 구분` 필터 적용 검색 시간 **미소요**로 **도합 0.53초** 소요.

  ⇒ 평균 사용자가 과목 정보를 얻는데 필요한 시간 **28.26초** 단축, 기존 사이트는 재검색 시마다 조회 시간 발생으로 실 단축 시간은 더 클 것으로 분석된다. 

  또한 기존 사이트가 일정 확률로 검색 실패 / 세션 만료 오류가 나는 문제도 해결하였다. 

- 모바일 학생증 실사용 검증: 열람실, 도서관 사용
   <img width="383" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/6ecf6bc0-d2ba-4366-a46e-456d2f0df409">

  ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2027.png)

- 다양한 기기 viewport에 맞는 접근성, 가독성 상향

  - 태블릿에서 본 사이버캠퍼스 앱 화면 예시)
![image](https://github.com/kevink1113/Sogang-Portal/assets/48401272/efcc182b-a67e-4a56-8cde-e0223ee6840d)

    ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2028.png)

  - 데스크탑 웹 페이지와의 일관성 문제, PC와 일부 미지원 기기들의 앱 부재 해결

  - 데이터의 분산, 정보 접근성 개선

  - 정보 공유 다양성 증진, 신뢰성 확보

    - 에브리타임: 단순 사진 업로드만 가능, 계정 거래로 인한 외부인 유입 가능성.

      ⇒ 유튜브 영상, 파일, 지도 등 다양한 형식의 정보 공유 가능, 익명 간 구분: 닉네임 사용

      ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2029.png)

      ![Untitled](SSS%E1%84%83%E1%85%A1%E1%86%AB%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%85%E1%85%AD%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5%20772ff566afbd4db1a8c02ed775c2ba54/Untitled%2030.png)

      ⇒ Saint 계정 연동을 통해 정확한 구성원의 검증 가능, 별도의 회원가입이나 개인정보 요구 절차 불필요: 초기 접근성 향상

- Sogang GPT 답변의 신뢰성, 신속성

  - 기존 ChatGPT와의 학교 관련 질문 차이: 아래 예시와 같이 ChatGPT는 “서강대학교의 FA 규정”이라 명시하여도 엉뚱한 대답을 내놓는 것을 볼 수 있다.

   <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/61b89a16-ca45-4d06-9f2a-23cb895fd212">

   <img width="387" alt="image" src="https://github.com/kevink1113/Sogang-Portal/assets/48401272/be1edad5-59b8-4fc7-87f3-b4cbb0b125b4">


  - 답변 평균 속도 측정, GPT-4와의 비교 (2023.6.17, ChatGPT May 24 Version 기준)
    5가지 동일 질문 하, 답변 소요 평균 시간을 측정하였을 때 ChatGPT는 평균 10.83초, Sogang GPT는 3.81초가 소요되었다.

## 6. 향후개선방안

- 미해결이슈, 보완사항, 향후계획 등 기술

### 미해결이슈

- 검색 기능의 정교화
  - 검색 기능을 보다 정교하게 만들어서 사용자가 원하는 정보를 더 빠르고 정확하게 찾을 수 있도록 개선할 필요가 있다.
- Sogang GPT의 정확도 개선 및 학습 정교화
  - 현재 Sogang GPT는 95%정도의 정확도를 나타내고 있는데 이 정확도를 더 개선하여야 한다
  - GPT 학습 데이터를 추가하거나 모델을 개선하여 더 많은 기능을 하는 GPT를 개발해야할 필요가 있다.

### 보완사항

- 시간표 팝업 부분 UI개선
- 검색 기능의 정교화 등 서버 처리 속도 개선
- 닉네임 설정 부분 UI개선
- Sogang GPT의 정확도 개선 및 학습 정교화

### 향후계획

1. 사용자의 버그 제보를 통한 수정
   - 서강대학교 사이트 업데이트 등 환경 변화 시 크롤링 방법 변경
   - 사용자 들의 요구사항에 따른 소프트웨어 업데이트
   - 코멘트 추가, 시스템 모듈 구조 개선, 코드 최적화 등의 시스템 개선
   - 과목 알림 기능 추가 구현
2. GPT Model 학습 정교화 (실시간 공지, 해야 할 일 학습, 기타 기능과 연계)
3. 서강톡톡을 이용하여 특정 학생간의 강의 수강에 대한 6단계 분리 이론 검증
4. 앱에서 시간표를 추가하면 수강신청 담아놓기 기간에 자동으로 담아놓기
5. 사이버캠퍼스 온라인 강의 수강 기능 추가
6. 3D map 구현
7. 학사일정 UI에 추가
8. 시설물 예약 기능 추가
9. 앱에서 알림 기능 추가
