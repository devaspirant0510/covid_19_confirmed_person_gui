from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
#####################################
# 웹크롤링
url='http://ncov.mohw.go.kr/' #사이트 주소
html=urllib.request.urlopen(url).read() #주소 읽기
soup=BeautifulSoup(html,'html.parser') # html부분만 가져오기
today=soup.find_all('span',{'class':'data'}) #오늘 확진자 정보 
cov_today=[]
for to in today:
    cov_today.append(to.get_text())
local_cov=cov_today[0]#국내확진자
global_cov=cov_today[1]#해외확진자

#시도별 확진자
citystar=soup.find_all('span',{"class":'name'})#지역이름
citynujuk=soup.find_all('button',{"type":'button'})#지역별 누적 확진자
citynujuk=citynujuk[3:]#필요한 부분만  슬라이싱
citylist=[]
for i in citynujuk:
    citylist.append(i.get_text())#리스트에 지역별 확진자 정보를 저장
    


####################################
# GUI 
root=Tk()
root.geometry("500x700")#화면크기
root.title("covid-19")
root.resizable(False,False)#화면 크기 조절 불가

label=Label(text="covid-19")
label.pack()

#일일 확진자 정보
today_cov_label=Label(text=f"국내 확진 :{local_cov} 명\n해외유입 :{global_cov} 명")
today_cov_label.pack()


citystar=Label(root,text="시도별확진자 현황")
citystar.pack()


city_var=IntVar()#라디오버튼에 대한 값

def press_btn():#라디오 버튼을 눌렀을때 value값과 맞게 citylist의 값을 보여줌
    city.config(text=citylist[city_var.get()-1])
local1 = Radiobutton(text='서울', value=1, variable=city_var,command=press_btn)
local1.select()
local1.pack()
local2 = Radiobutton(text='부산', value=2, variable=city_var,command=press_btn)
local2.pack()
local3 = Radiobutton(text='대구', value=3, variable=city_var,command=press_btn)
local3.pack()
local4 = Radiobutton(text='인천', value=4, variable=city_var,command=press_btn)
local4.pack()
local5 = Radiobutton(text='광주', value=5, variable=city_var,command=press_btn)
local5.pack()
local6 = Radiobutton(text='대전', value=6, variable=city_var,command=press_btn)
local6.pack()
local7 = Radiobutton(text='울산', value=7, variable=city_var,command=press_btn)
local7.pack()
local8 = Radiobutton(text='세종', value=8, variable=city_var,command=press_btn)
local8.pack()
local9 = Radiobutton(text='경기', value=9, variable=city_var,command=press_btn)
local9.pack()
local10 = Radiobutton(text='강원', value=10, variable=city_var,command=press_btn)
local10.pack()
local11 = Radiobutton(text='충북', value=11, variable=city_var,command=press_btn)
local11.pack()
local12 = Radiobutton(text='충남', value=12, variable=city_var,command=press_btn)
local12.pack()
local13 = Radiobutton(text='전북', value=13, variable=city_var,command=press_btn)
local13.pack()
local14 = Radiobutton(text='전남', value=14, variable=city_var,command=press_btn)
local14.pack()
local15 = Radiobutton(text='경북', value=15, variable=city_var,command=press_btn)
local15.pack()
local16 = Radiobutton(text='경남', value=16, variable=city_var,command=press_btn)
local16.pack()
local17 = Radiobutton(text='제주', value=17, variable=city_var,command=press_btn)
local17.pack()
local18 = Radiobutton(text='검역', value=18, variable=city_var,command=press_btn)
local18.pack()

citylabel=Label(root, text="지역별확진자",bg='yellow')
citylabel.pack()
city=Label(root, text="",bg='yellow',fg='red',width=20)
city.pack()



root.mainloop()

