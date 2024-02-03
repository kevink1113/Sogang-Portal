import requests
from bs4 import BeautifulSoup
from requests import Response
# 경고 비활성화
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_saint_cookies(id, pw):
    """
    모바일 세인트 로그인 후 쿠키를 받아오는 함수
    @param id: 학번
    @param pw: 비밀번호
    @return: 세션 쿠키값
    """
    # 세션 만들어서 쿠키 값을 받아오자!
    login_url = "https://msaint.sogang.ac.kr/loginproc.aspx"  # 모바일 세인트 로그인 주소
    header = {
        "User-Agent": "Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 \
            (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
    }
    # request에 아이디 비번 암호 그대로 전달.. 서강대 보안 어데감?
    LOGIN_INFO = {
        'destURL': '/',
        'userid': id,
        'passwd': pw,
    }
    try:
        session = requests.session()  # 세션 생성
        response = session.post(login_url, headers=header, data=LOGIN_INFO, verify=False)
        cookies = session.cookies  # 쿠키 값 받아오기
        session.close()  # 세션 닫기
        if len(cookies) == 0:
            return None
        return cookies
    except:
        print("Failed to login")
        return None


def get_student_info(cookies):
    info_url = "https://msaint.sogang.ac.kr/studentInfo/s1.aspx"  # 학생정보 주소
    try:
        response: Response = requests.get(info_url, cookies=cookies, verify=False)
        if response.status_code == 200:
            # BeautifulSoup 객체 생성
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.select('tr')  # 모든 행(<tr> 태그) 선택

            info = {}
            for row in rows:
                th_text = row.select_one('th').text  # 행의 <th> 태그 텍스트
                td_text = row.select_one('td').text  # 행의 <td> 태그 텍스트
                info[th_text] = td_text

            for key, value in info.items():
                print(f"{key}: {value}")

            return info
    except:
        print("Connection refused by the server..")
        return None


def get_takes_info_by_semester(cookies, semester):
    """
    실제로 수강한 학기마다의 수강신청 정보를 받아오는 함수
    @param cookies: 세션 쿠키값
    @param semester: semesteridx 값
    @return:
    """
    semester_dict = {}
    semester_url = f"https://msaint.sogang.ac.kr/grade/g2.aspx?isposted=1&semesteridx={semester}"  # 수강신청 정보 주소
    try:    
        response: Response = requests.get(semester_url, cookies=cookies, verify=False)
        if response.status_code == 200:
            # BeautifulSoup 객체 생성
            soup = BeautifulSoup(response.text, 'html.parser')
            # 수강신청 조회리스트를 추출
            courses = soup.select('tr[id^=tr]')

            # 수강신청 조회리스트를 순회하며 각 과목의 정보를 출력
            for course in courses:
                course_dict = {}
                course_number = course.select_one('td:nth-child(1)').text
                course_class = course.select_one('td:nth-child(2)').text
                course_name = course.select_one('td:nth-child(3)').text
                course_tr_id = course['id'][2:]

                course_dict['course_number'] = course_number
                course_dict['course_class'] = course_class
                course_dict['course_name'] = course_name
                course_dict['tr_id'] = course_tr_id

                semester_dict[course_tr_id] = course_dict
            return semester_dict
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except:
        print("Connection refused by the server..")
        return None


def get_takes_info(cookies):
    """
    세션 쿠키값을 이용해 수강신청 정보를 받아오는 함수
    @param cookies: 세션 쿠키값
    @return: 수강신청 정보
    """
    takes_info = {}
    takes_url = "https://msaint.sogang.ac.kr/grade/g2.aspx"  # 수강신청 정보 주소
    try:
        response: Response = requests.get(takes_url, cookies=cookies, verify=False)
        if response.status_code == 200:
            # BeautifulSoup 객체 생성
            soup = BeautifulSoup(response.text, 'html.parser')
            semesters = soup.select('select[name=semesteridx] > option')

            # 수강신청 조회리스트를 순회하며 각 과목의 정보를 출력
            for index, semester in enumerate(semesters):
                if index == 0:  # 첫번째 옵션은 무선택을 의미하므로 제외
                    continue
                # print(f"<학기: {semester.text}, value: {semester['value']}>")
                # 'value' 값(semesteridx)은 2023년도 1학기이면: 2023010과 같이 표현됨
                semester_value = semester['value']
                takes_info[semester_value] = get_takes_info_by_semester(cookies, semester_value)

            return takes_info
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except:
        print("Connection refused by the server..")
        return None


def pretty_print_takes_info(takes_info):
    for semester, courses in takes_info.items():
        print(f"학기: {semester}")
        print("-" * 40)
        for tr_id, course in courses.items():
            print(f"과목 번호: {course['course_number']}, 분반: {course['course_class']}, "
                  f"교과목명: {course['course_name']}, tr_id: {tr_id}")
        print("=" * 40)
