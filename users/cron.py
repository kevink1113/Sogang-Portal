from apscheduler.schedulers.background import BackgroundScheduler
from config.crawl_courses import crawl_courses
from config.crawl_notice import crawl_notice
from pybo.models import *
from datetime import datetime,time

daytoint = {'월':1, '화':2, '수':3, '목':4, '금':5, '토':6, '일':7}

def get_current_courses():
  #반복되는 함수 course를 받아와서 데이터베이스에 저장해줌
  crawls = None
  crawls = crawl_courses('23','1')
  print(crawls)
  if crawls is not None :
    for i in range(len(crawls)) :
        course = Course.get_course_by_id(crawls['과목번호'][i]+'-'+crawls['분반'][i],231)
        #print(crawls['subject_id'][i])
        if course is None :
          course = Course()
        course.advisor = crawls['교수진'][i]
        course.classroom = crawls['강의실'][i]
        course.course_id = crawls['과목번호'][i]+'-'+crawls['분반'][i]
        #print(crawls['요일1'][i])
        if len(crawls['요일1'][i]) == 0 or len(crawls['요일1'][i])>5:
           day = 88
        else :
           day = daytoint[crawls['요일1'][i].split(',')[0]]
           if len(crawls['요일1'][i].split(','))>1:
              day = day*10 + daytoint[crawls['요일1'][i].split(',')[1]]
        course.day = day
        if len(crawls['종료시간1'][i]) == 0 :
          course.end_time = datetime.strptime('09:00', '%H:%M').time()
          course.start_time = datetime.strptime('09:00', '%H:%M').time()
        else :
          course.end_time = datetime.strptime(crawls['종료시간1'][i], '%H:%M').time()
          course.start_time = datetime.strptime(crawls['시작시간1'][i], '%H:%M').time()
        course.name = crawls['과목명'][i]
        course.semester = 231
        course.save()
  # crawls = crawl_courses('19','1')
  print(crawls)
  if crawls is not None :
    for i in range(len(crawls)) :
        course = Course.get_course_by_id(crawls['과목번호'][i]+'-'+crawls['분반'][i],191)
        #print(crawls['subject_id'][i])
        if course is None :
          course = Course()
        course.advisor = crawls['교수진'][i]
        course.classroom = crawls['강의실'][i]
        course.course_id = crawls['과목번호'][i]+'-'+crawls['분반'][i]
        #print(crawls['요일1'][i])
        if len(crawls['요일1'][i]) == 0 or len(crawls['요일1'][i])>5:
           day = 88
        else :
           day = daytoint[crawls['요일1'][i].split(',')[0]]
           if len(crawls['요일1'][i].split(','))>1:
              day = day*10 + daytoint[crawls['요일1'][i].split(',')[1]]
        course.day = day
        if len(crawls['종료시간1'][i]) == 0 :
          course.end_time = datetime.strptime('09:00', '%H:%M').time()
          course.start_time = datetime.strptime('09:00', '%H:%M').time()
        else :
          course.end_time = datetime.strptime(crawls['종료시간1'][i], '%H:%M').time()
          course.start_time = datetime.strptime(crawls['시작시간1'][i], '%H:%M').time()
        course.name = crawls['과목명'][i]
        course.semester = 191
        course.save()
  crawls = crawl_notice('1')
  print(crawls)
  if crawls is not None :
      for i in crawls:
        if Notice.objects.filter(mod=0,title=i['Title'],writer=i['Writer'],date=datetime.strptime(i['Date'], "%Y.%m.%d")) :
            continue
        notice=Notice()
        #print(i['Number'])
        if i['Number'] == 'TOP':
           i['Number'] = '132'
        notice.num = (int)(i['Number'])
        notice.title = i['Title']


        notice.url = i['Link']
        notice.writer = i['Writer']
        notice.view = (int)(i['Views'].replace(",",""))
        notice.date = datetime.strptime(i['Date'], "%Y.%m.%d")
        notice.file = i['Link']
        notice.mod = 0
        notice.save()


def run():
    get_current_courses()
    sched = BackgroundScheduler()
    sched.add_job(get_current_courses,'interval', seconds=300000, id='test')
    sched.start()
    pass