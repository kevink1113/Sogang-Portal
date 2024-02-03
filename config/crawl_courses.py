import requests
from bs4 import BeautifulSoup
from time import sleep
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
# 경고 비활성화
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

years = {
    '30': 'WD27',
    '29': 'WD28',
    '28': 'WD29',
    '27': 'WD2A',
    '26': 'WD2B',
    '25': 'WD2C',
    '24': 'WD2D',
    '23': 'WD2E',
    '22': 'WD2F',
    '21': 'WD30',
    '20': 'WD31',
    '19': 'WD32',
    '18': 'WD33',
    '17': 'WD34',
    '16': 'WD35',
    '15': 'WD36',
    '14': 'WD37',
    '13': 'WD38',
    '12': 'WD39',
    '11': 'WD3A',
    '10': 'WD3B',
    '09': 'WD3C',
    '08': 'WD3D',
    '07': 'WD3E',
    '06': 'WD3F',
    '05': 'WD40',
    '04': 'WD41',
    '03': 'WD42',
    '02': 'WD43',
    '01': 'WD44',
    '00': 'WD45',
    '99': 'WD46'
}

semesters = {
    '1': 'WD4C',
    's': 'WD4D',
    '2': 'WD4E',
    'w': 'WD4F'
}

columns = [
    '학년도',
    '학기',
    '소속',
    '학과',
    '과목번호',
    '분반',
    '과목명',
    '강의계획서',
    '학점',
    '수업시간_강의실',
    '시간',
    '교수진',
    '수강생수',
    '영어강의',
    '중국어강의',
    '공학인증',
    '국제학생',
    'Honors과목',
    '홀짝구분',
    '승인과목',
    '시험일자',
    '수강대상',
    '권장학년',
    '수강신청_참조사항',
    '과목_설명',
    '비고'
]


def crawl_courses(year, semester):
    """
    개설교과목 정보 페이지에서 selenium 이용 크롤링 후 pandas DataFrame으로 반환
    @param year: 개설년도
    @param semester: 개설학기
    @return: 개설교과목 정보 DataFrame
    """
    print(f'{year} year, {semester} semester crawling start.')
    try:
        target_url = "http://sis109.sogang.ac.kr/sap/bc/webdynpro/sap/zcmw9016?sap-language=KO&sap-cssurl=http%3a%2f%2fsaint.sogang.ac.kr%3a80%2fcom.sap.portal.design.urdesigndata%2fthemes%2fportal%2fcustom_tradeshow_01%2fls%2fls_sf3.css%3fv%3d10.30.7.261448.1491647873000#%20%3Chttp://sis109.sogang.ac.kr/sap/bc/webdynpro/sap/zcmw9016?sap-language=KO&sap-cssurl=http://saint.sogang.ac.kr:80/com.sap.portal.design.urdesigndata/themes/portal/custom_tradeshow_01/ls/ls_sf3.css?v%3d10.30.7.261448.1491647873000#"
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("window-size=1400,1500")
        driver = webdriver.Chrome(options=options)
        driver.get(target_url)
        print('Entering Target Page...')
        driver.implicitly_wait(30)  # 30초 기다림 (페이지 로딩 시간)
        year_xpath = f'//*[@id="{years[year]}"]'
        semester_xpath = f'//*[@id="{semesters[semester]}"]'
        # 개설년도 Form 선택 후 클릭
        sleep(0.5)
        driver.find_element(By.XPATH, r'//*[@id="WD25"]').click()
        # 개설년도 클릭
        sleep(0.5)
        driver.find_element(By.XPATH, year_xpath).click()
        # 학기 Form 선택 후 클릭
        sleep(0.5)
        driver.find_element(By.XPATH, r'//*[@id="WD4A"]').click()
        # 학기 선택
        sleep(0.5)
        driver.find_element(By.XPATH, semester_xpath).click()
        # WD4C WD4D WD4E WD4F
        # 소속구분 Form 선택 후 클릭
        sleep(0.5)
        driver.find_element(By.XPATH, r'//*[@id="WD7E"]').click()
        # 학부 클릭
        sleep(0.5)
        driver.find_element(By.XPATH, r'//*[@id="WD80"]').click()
        # 검색 클릭
        sleep(1.5)
        driver.find_element(By.XPATH, r'//*[@id="WDBC"]').click()
        contentTable = '//*[@id="WDC0-contentTBody"]/tr[3]'
        print('Resource fetching...')
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, contentTable)))
        print('Resource fetching done')
        print('Saving data...')
        # 스크래핑
        html = driver.page_source
        # print("==html===")
        # print(html)
        # print("==html end===")
        result_df = lxmlToDataframe(html)
        result_df = preprocessor(result_df)
        print(f'{year} year, {semester} semester crawling done.')
        driver.close()
        return result_df
    except Exception as e:
        print(f'Error crawling {year} year, {semester} semester courses. Error: {e}')
        return None


def lxmlToDataframe(html):
    """
    크롤링한 데이터를 스크래핑하여 DataFrame으로 저장
    @param html: 크롤링한 html
    @return: 스크래핑한 데이터 DataFrame
    """
    from bs4 import BeautifulSoup
    import pandas as pd

    soup = BeautifulSoup(html, 'lxml')
    res = soup.find("tbody", id='WDC0-contentTBody')
    if not res:  # res가 None인 경우 처리
        print("No data found in the specified tbody id")
        return pd.DataFrame()  # 빈 DataFrame 반환

    trs = res.find_all('tr')

    # 모든 행을 순회하며 최대 열 개수 확인
    max_columns = 0
    for tr in trs:
        tds = tr.find_all('td')
        max_columns = max(max_columns, len(tds))

    # 데이터를 저장할 리스트 초기화
    crawled_data = [[] for _ in range(max_columns)]

    for tr in trs:
        tds = tr.find_all('td')
        for idx, td in enumerate(tds):
            # td 안에 span이 있는 경우와 없는 경우를 처리
            text = td.find('span').text if td.find('span') else ' '
            crawled_data[idx].append(text)

    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame({columns[i]: crawled_data[i] for i in range(len(columns)) if i < len(crawled_data)})

    # 과목 ID와 department 열 추가
    subject_ids = ['21-2-' + crawled_data[4][i] + '-' + crawled_data[5][i] for i in range(len(crawled_data[0]))]
    df['subject_id'] = subject_ids
    df['department'] = ''  # department 정보가 없으므로 빈 문자열 할당

    return df


firstDays = []
secondDays = []
firstStartTime = []
secondStartTime = []
firstEndTime = []
secondEndTime = []
firstTotalTime = []
secondTotalTime = []
classrooms = []

def split_day_time_classroom(x):
    """
    요일, 시간, 강의실을 분리하여 저장
    @param x: 요일, 시간, 강의실이 합쳐진 문자열
    @return: 요일, 시간, 강의실을 분리하여 저장
    """
    arr = x.split(" / ")
    if len(arr) == 0 or arr[0] == '' or arr[0] == '\xa0':
        firstDays.append('')
        secondDays.append('')
        firstStartTime.append('')
        secondStartTime.append('')
        firstEndTime.append('')
        secondEndTime.append('')
        firstTotalTime.append('')
        secondTotalTime.append('')
        classrooms.append('')
    else:
        if len(arr) == 2:
            arr1 = arr[0].split(' ')
            arr2 = arr[1].split(' ')
            firstDays.append(arr1[0])
            secondDays.append(arr2[0])

            if len(arr1) > 1:
                firstTotalTime.append(arr1[1])
                firstStartTime.append(arr1[1].split('~')[0])
                firstEndTime.append(arr1[1].split('~')[1])
            else:
                firstTotalTime.append('')
                firstStartTime.append('')
                firstEndTime.append('')

            if len(arr2) > 1:
                secondTotalTime.append(arr2[1])
                secondStartTime.append(arr2[1].split('~')[0])
                secondEndTime.append(arr2[1].split('~')[1])
            else:
                secondTotalTime.append('')
                secondStartTime.append('')
                secondEndTime.append('')

            if len(arr2) == 3 and arr2[2] != '':
                classrooms.append(arr2[2])
            else:
                classrooms.append('')

        else:
            arr = x.split(' ')
            firstDays.append(arr[0])
            secondDays.append(arr[0])

            if len(arr) > 1:
                firstTotalTime.append(arr[1])
                secondTotalTime.append(arr[1])
                firstStartTime.append(arr[1].split('~')[0])
                firstEndTime.append(arr[1].split('~')[1])
                secondStartTime.append(arr[1].split('~')[0])
                secondEndTime.append(arr[1].split('~')[1])
            else:
                firstTotalTime.append('')
                secondTotalTime.append('')
                firstStartTime.append('')
                firstEndTime.append('')
                secondStartTime.append('')
                secondEndTime.append('')

            if len(arr) == 3 and arr[2] != '':
                classrooms.append(arr[2])
            else:
                classrooms.append('')



def preprocessor(df):
    """
    일부 컬럼 추가 및 수정을 위한 데이터 전처리기
    1. 학점 Int로 변형
    2. 수업 요일, 시작시간, 종료시간, 강의실 분리
    3. 대면 여부 추가
    4. 강의 언어 추가
    @param df: 전처리할 데이터
    @return: 전처리된 데이터
    """

    # 1. 학점 Int로 변형
    df.loc[:, '학점'] = df.loc[:, '학점'].map(lambda x: int(float(x)) if x in ['1.0', '2.0', '3.0'] else 0)

    # 2. 수업 요일, 시작시간, 종료시간, 강의실 분리
    df['수업시간_강의실'].map(lambda x: split_day_time_classroom(x))

    # new version
    df['요일1'] = firstDays
    df['요일2'] = secondDays

    df['시간1'] = firstTotalTime
    df['시간2'] = secondTotalTime

    df['시작시간1'] = firstStartTime
    df['종료시간1'] = firstEndTime

    df['시작시간2'] = secondStartTime
    df['종료시간2'] = secondEndTime

    df['강의실'] = classrooms

    # 3. 대면 여부 추가
    df['대면여부'] = '미정'
    df.loc[df['비고'].map(lambda x: x.startswith('[비대면]')), '대면여부'] = '비대면'
    df.loc[df['비고'].map(lambda x: x.startswith('[대면]')), '대면여부'] = '대면'

    # 4. 강의 언어 추가
    df['강의언어'] = '한국어'
    df.loc[df['영어강의'] == 'O', '강의언어'] = '영어'
    df.loc[df['중국어강의'] == 'O', '강의언어'] = '중국어'

    # 5. 비고 에서 [대면], [비대면] 제거
    df.loc[:, '비고'] = df['비고'].map(lambda x: x.replace("[대면]", ""))
    df.loc[:, '비고'] = df['비고'].map(lambda x: x.replace("[비대면]", ""))
    df.loc[:, '비고'] = df['비고'].map(lambda x: x[1:] if len(x) > 0 and x[0] == ' ' else x)

    # 6. updatedAt 추가
    df['updated_at'] = time.strftime('%Y년 %m월 %d일 %H시 %M분', time.localtime(time.time()))
    return df
