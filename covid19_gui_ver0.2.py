#####################################
# @covid-19 confirmed person
# @2020.8.30
# @ver 0.2
# @devaspirant0510
#####################################
# 업데이트 내용
# -디자인 변경
# -폰트추가
# -레이아웃 설정
# -시도별 확진자 (라디오버튼 -> 콤보박스)
# -시도별 확진자 세부적인 데이터
# -검사현황 누적확진자 추가
#####################################
from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
from datetime import datetime
#####################################
# 웹크롤링
url='http://ncov.mohw.go.kr/' #사이트 주소
html=urllib.request.urlopen(url).read() #주소 읽기
soup=BeautifulSoup(html,'html.parser') # html부분만 가져오기
#일일 확진자 정보 
today=soup.find_all('span',{'class':'data'}) 
cov_today=[]
for to in today:
    cov_today.append(to.get_text())
local_cov=cov_today[0]#국내확진자
global_cov=cov_today[1]#해외확진자

#누적 확진자 정보
cov_accumulate=soup.find_all('span',{'class':'num'})
cov_accumulate_now=soup.find_all('span',{'class':'before'})

cov_accumulate_li=[]#누적
for i in cov_accumulate:
    cov_accumulate_li.append(i.get_text())
cov_accumulate=cov_accumulate_li[:4]

cov_accumulate_now_li=[]#전일대비
for i in cov_accumulate_now:
    cov_accumulate_now_li.append(i.get_text())
cov_accumulate_now=cov_accumulate_now_li[:4]
#검사현황
cov_check=soup.find_all('span',{"class","num"})

check_data_li=[]
for i in cov_check:
    check_data_li.append(i.get_text())
check_data_li=check_data_li[4:7]

#시도별 확진자
citystar=soup.find_all('span',{"class":'name'})#지역이름
citynujuk=soup.find_all('button',{"type":'button'})#지역별 누적 확진자
cov_data=soup.find_all("span",{"class","num"})#지역별 확진자 데이터
cov_junill=soup.find_all("span",{"class","sub_num red"})#시도별 전일대비 확진자
citynujuk=citynujuk[3:]#필요한 부분만  슬라이싱
citylist=[]
for i in citystar:
    citylist.append(i.get_text())#리스트에 지역별 확진자 정보를 저장

dataset=[]
for i in cov_data:
    dataset.append(i.get_text())


junilldataset=[]
for i in cov_junill:
    junilldataset.append(i.get_text())

junilldataset=junilldataset[1:]#전일대비 확진자 데이터
deaddataset=dataset[33::5]#사망자 데이터
quarantine_release_dataset=dataset[32::5]# 격리해제 데이터
nujukdataset=dataset[7:25]#누적확진자 데이터
isolationdataset=dataset[31::5]#격리 데이터
####################################
# GUI 

# 화면설정
root=Tk()
root.geometry("500x450")#화면크기
root.title("covid-19")#제목
titlefont=font.Font(family="Segoe UI", size=30,weight='bold')#제목폰트
font=font.Font(family="나눔 고딕", size=10,weight='bold')#기본폰트
root.resizable(False,False)#화면 크기 고정

# 제목 프레임
# 오늘 시간 불러옴
now=datetime.now()
today=f"{now.year}.{now.month}.{now.day}"
# Head 프레임
head=Frame(root,width=500,height=100,bg='#fffff0',borderwidth=3,relief=GROOVE)
head.place(x=0,y=0,width=500,height=100)
# 제목
titlelabel=Label(head,text='Covid-19',bg='#fffff0',font=titlefont)
titlelabel.place(x=0,y=0,width=350,height=120)
# 날짜
datelabel=Label(head,text=today,bg='#fffff0',font=font)
datelabel.place(x=300,y=50,width=200,height=50)


# 프레임 1==============================================================================================
frame1=Frame(root,bg='#fffff0',borderwidth=3,relief=GROOVE)
frame1.place(x=0,y=100,width=250,height=150)

# 프레임 1 제목
today_cov_label=Label(frame1,text="일일 확진자",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
today_cov_label.place(x=11,y=2,width=230,height=23)

# 국내 확진자 정보
local_cov_label=Label(frame1,text=local_cov,relief=RIDGE,font=font)
local_cov_label.place(x=10,y=25,width=110,height=45)
local_cov_label_text=Label(frame1,text="국내 확진자",width=50,height=30,relief=RIDGE)
local_cov_label_text.place(x=10,y=70,width=110,height=20)

# 해외 유입 정보
global_cov_label=Label(frame1,text=global_cov,relief=RIDGE,font=font)
global_cov_label.place(x=130,y=25,width=110,height=45)
local_cov_label_text=Label(frame1,text="해외 유입",width=50,height=30,relief=RIDGE)
local_cov_label_text.place(x=130,y=70,width=110,height=20)
#========================================================================================================


# 프레임 2===============================================================================================
frame2=Frame(root,bg='#fffff0',borderwidth=3,relief=GROOVE)
frame2.place(x=0,y=200,width=250,height=250)

# 프레임 2 제목
confirmation_by_region=Label(frame2 ,text="검사현황",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
confirmation_by_region.place(x=5,y=2,width=235,height=23)

# 누적검사수 데이터 
fr2_label1_title=Label(frame2,text='누적검사수',relief=RIDGE,font=font)
fr2_label1_title.place(x=5,y=25,width=235,height=30)
fr2_label1_data=Label(frame2,text=check_data_li[0],relief=RIDGE,font=font)
fr2_label1_data.place(x=5,y=55,width=235,height=30)

# 누적검사완료수 데이터
fr2_label2_title=Label(frame2,text='누적검사완료수',relief=RIDGE,font=font)
fr2_label2_title.place(x=5,y=85,width=235,height=30)
fr2_label2_data=Label(frame2,text=check_data_li[1],relief=RIDGE,font=font)
fr2_label2_data.place(x=5,y=115,width=235,height=30)

# 누적확진률 데이터
fr2_label3_title=Label(frame2,text='누적확진률',relief=RIDGE,font=font)
fr2_label3_title.place(x=5,y=145,width=235,height=30)
fr2_label3_data=Label(frame2,text=check_data_li[2],relief=RIDGE,font=font)
fr2_label3_data.place(x=5,y=175,width=235,height=30)
#========================================================================================================



# 프레임 3================================================================================================
frame3=Frame(root,bg='#fffff0',borderwidth=3,relief=GROOVE)
frame3.place(x=250,y=100,width=250,height=130)

# 프레임 3 제목
accumulate_cov_label=Label(frame3,text="누적 확진자",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
accumulate_cov_label.place(x=5,y=2,width=235,height=23)

# 확진자 정보
fr3_labell_title=Label(frame3,text='확진자',font=font)
fr3_labell_title.place(x=5,y=30,width=55,height=20)
fr3_label1_main=Label(frame3,text=f"{cov_accumulate[0][4:]}\n{cov_accumulate_now[0][6:11]}")
fr3_label1_main.place(x=5,y=50,width=55,height=60)

# 완치 정보
fr3_label2_title=Label(frame3,text='완치',font=font)
fr3_label2_title.place(x=65,y=30,width=55,height=20)
fr3_label2_main=Label(frame3,text=f"{cov_accumulate[1]}\n{cov_accumulate_now[1]}")
fr3_label2_main.place(x=65,y=50,width=55,height=60)

# 격리중 정보
fr3_label3_title=Label(frame3,text='격리중',font=font)
fr3_label3_title.place(x=125,y=30,width=55,height=20)
fr3_label3_main=Label(frame3,text=f"{cov_accumulate[2]}\n{cov_accumulate_now[2]}")
fr3_label3_main.place(x=125,y=50,width=55,height=60)

# 사망 정보
fr3_label4_title=Label(frame3,text='사망',font=font)
fr3_label4_title.place(x=185,y=30,width=55,height=20)
fr3_label4_main=Label(frame3,text=f"{cov_accumulate[3]}\n{cov_accumulate_now[3]}")
fr3_label4_main.place(x=185,y=50,width=55,height=60)

#================================================================================================


# 프레임 3================================================================================================
frame4=Frame(root,bg='#fffff0',borderwidth=3,relief=GROOVE)
frame4.place(x=250,y=230,width=250,height=240)

# 프레임 3 제목
confirmation_by_region=Label(frame4 ,text="지역별 확진자",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
confirmation_by_region.place(x=5,y=2,width=235,height=23)

# 콤보박스 항복선택시 처리되는 이벤트
def on_select(event=None):
    # 선택한 지역에 맞게 데이터 출력
    if cov_by_region_combobox.get()=="서울":
        label3_text.config(text=nujukdataset[0])
        label4_text.config(text=junilldataset[0])
        label5_text.config(text=isolationdataset[0])
        label6_text.config(text=quarantine_release_dataset[0])
        label7_text.config(text=deaddataset[0])  
    elif cov_by_region_combobox.get()=="부산":
        label3_text.config(text=nujukdataset[1])
        label4_text.config(text=junilldataset[1]) 
        label5_text.config(text=isolationdataset[1]) 
        label6_text.config(text=quarantine_release_dataset[1])   
        label7_text.config(text=deaddataset[1])      
    elif cov_by_region_combobox.get()=="대구":
        label3_text.config(text=nujukdataset[2])
        label4_text.config(text=junilldataset[2])   
        label5_text.config(text=isolationdataset[2])         
        label6_text.config(text=quarantine_release_dataset[2])
        label7_text.config(text=deaddataset[2])      
    elif cov_by_region_combobox.get()=="인천":
        label3_text.config(text=nujukdataset[3])
        label4_text.config(text=junilldataset[3])   
        label5_text.config(text=isolationdataset[3])         
        label6_text.config(text=quarantine_release_dataset[3])
        label7_text.config(text=deaddataset[3])      
    elif cov_by_region_combobox.get()=="광주":
        label3_text.config(text=nujukdataset[4])
        label4_text.config(text=junilldataset[4])   
        label5_text.config(text=isolationdataset[4])         
        label6_text.config(text=quarantine_release_dataset[4])
        label7_text.config(text=deaddataset[4])      
    elif cov_by_region_combobox.get()=="대전":
        label3_text.config(text=nujukdataset[5]) 
        label4_text.config(text=junilldataset[5])   
        label5_text.config(text=isolationdataset[5])        
        label6_text.config(text=quarantine_release_dataset[5])
        label7_text.config(text=deaddataset[5])      
    elif cov_by_region_combobox.get()=="울산":
        label3_text.config(text=nujukdataset[6]) 
        label4_text.config(text=junilldataset[6])   
        label5_text.config(text=isolationdataset[6])        
        label6_text.config(text=quarantine_release_dataset[6])
        label7_text.config(text=deaddataset[6])      
    elif cov_by_region_combobox.get()=="세종":
        label3_text.config(text=nujukdataset[7]) 
        label4_text.config(text=junilldataset[7])   
        label5_text.config(text=isolationdataset[7])        
        label6_text.config(text=quarantine_release_dataset[7])
        label7_text.config(text=deaddataset[7])      
    elif cov_by_region_combobox.get()=="경기":
        label3_text.config(text=nujukdataset[8]) 
        label4_text.config(text=junilldataset[8])   
        label5_text.config(text=isolationdataset[8])        
        label6_text.config(text=quarantine_release_dataset[8])
        label7_text.config(text=deaddataset[8])      
    elif cov_by_region_combobox.get()=="강원":
        label3_text.config(text=nujukdataset[9]) 
        label4_text.config(text=junilldataset[9])   
        label5_text.config(text=isolationdataset[9])        
        label6_text.config(text=quarantine_release_dataset[9])
        label7_text.config(text=deaddataset[9])      
    elif cov_by_region_combobox.get()=="충북":
        label3_text.config(text=nujukdataset[10])
        label4_text.config(text=junilldataset[10])  
        label5_text.config(text=isolationdataset[10])         
        label6_text.config(text=quarantine_release_dataset[10]) 
        label7_text.config(text=deaddataset[10])      
    elif cov_by_region_combobox.get()=="충남":
        label2.config(text=nujukdataset[11])     
        label4_text.config(text=junilldataset[11])  
        label5_text.config(text=isolationdataset[11])     
        label6_text.config(text=quarantine_release_dataset[11])
        label7_text.config(text=deaddataset[11])      
    elif cov_by_region_combobox.get()=="전북":
        label2.config(text=nujukdataset[12])     
        label4_text.config(text=junilldataset[12])  
        label5_text.config(text=isolationdataset[12])     
        label6_text.config(text=quarantine_release_dataset[12])
        label7_text.config(text=deaddataset[12])      
    elif cov_by_region_combobox.get()=="경남":
        label3_text.config(text=nujukdataset[13])
        label4_text.config(text=junilldataset[13])  
        label5_text.config(text=isolationdataset[13])         
        label6_text.config(text=quarantine_release_dataset[13]) 
        label7_text.config(text=deaddataset[13])      
    elif cov_by_region_combobox.get()=="제주":
        label3_text.config(text=nujukdataset[14])
        label4_text.config(text=junilldataset[14])  
        label5_text.config(text=isolationdataset[14])         
        label6_text.config(text=quarantine_release_dataset[14]) 
        label7_text.config(text=deaddataset[14])      
    elif cov_by_region_combobox.get()=="검역":
        label3_text.config(text=nujukdataset[15])
        label4_text.config(text=junilldataset[15])  
        label5_text.config(text=isolationdataset[15])         
        label6_text.config(text=quarantine_release_dataset[15]) 
        label7_text.config(text=deaddataset[15])      

# 콤보박스               
cov_by_region_combobox=ttk.Combobox(frame4,height=12,values=citylist,state='readonly',font=font) #일기전용
cov_by_region_combobox.set("지역을 선택하세요")#초기 메시지
cov_by_region_combobox.place(x=110,y=30,width=130,height=25)
cov_by_region_combobox.bind('<<ComboboxSelected>>', on_select)#항목선택만해도 함수 실행되는 옵션

# 지역 레이블
label2=Label(frame4,text="지역",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label2.place(x=5,y=30,width=100,height=25)

# 누적확진환자 레이블
label3=Label(frame4,text="누적확진환자",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label3.place(x=5,y=60,width=100,height=25)
# 누적확진환자 데이터
label3_text=Label(frame4,text='',font=font)
label3_text.place(x=110,y=60,width=130,height=25)

# 전일대비 증감 레이블
label4=Label(frame4,text="전일대비 증감",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label4.place(x=5,y=90,width=100,height=25)
# 전일대비 증감 데이터
label4_text=Label(frame4,text='',font=font)
label4_text.place(x=110,y=90,width=130,height=25)

# 격리중 레이블
label5=Label(frame4,text="격리중",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label5.place(x=5,y=120,width=100,height=25)
# 격리중 데이터
label5_text=Label(frame4,text='',font=font)
label5_text.place(x=110,y=120,width=130,height=25)

# 누적격리해제 레이블
label6=Label(frame4,text="누적격리해제",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label6.place(x=5,y=150,width=100,height=25)
# 누적격리해제 데이터
label6_text=Label(frame4,text='',font=font)
label6_text.place(x=110,y=150,width=130,height=25)

# 사망자 레이블
label7=Label(frame4,text="사망자",font=font,bg="#E5D85C",borderwidth=2,relief=GROOVE)
label7.place(x=5,y=180,width=100,height=25)
# 사망자 데이터
label7_text=Label(frame4,text='',font=font)
label7_text.place(x=110,y=180,width=130,height=25)


root.mainloop()
