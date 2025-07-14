from slackclient import SlackClient
import time
from flask import json
from bs4 import BeautifulSoup
import requests
import itertools
from random import *
import gspread
import time
import os
from oauth2client.service_account import ServiceAccountCredentials
from gspread.urls import SPREADSHEETS_API_V4_BASE_URL
from gspread.utils import a1_to_rowcol
from datetime import date
from datetime import datetime
import re
import datetime as dt
from selenium import webdriver

login_basic_url2 = 'http://ftth.wlink.com.np/index.php/login/processLogin'
data = {
        'username': 'pratik.tamrakar',
        'password': 'Hyper2020$#@'
        }



scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


 

    


def insert_note(worksheet, label, note):
    """
    Insert note ito the google worksheet for a certain cell.

    Compatible with gspread.
    """
    spreadsheet_id = worksheet.spreadsheet.id
    worksheet_id = worksheet.id

    [row,col]=label


    url = f"{SPREADSHEETS_API_V4_BASE_URL}/{spreadsheet_id}:batchUpdate"
    payload = {
        "requests": [
            {
                "updateCells": {
                    "range": {
                        "sheetId": worksheet_id,
                        "startRowIndex": row-1,
                        "endRowIndex": row,
                        "startColumnIndex": col-1,
                        "endColumnIndex": col
                    },
                    "rows": [
                        {
                            "values": [
                                {
                                    "note": note
                                }
                            ]
                        }
                    ],
                    "fields": "note"
                }
            }
        ]
    }
    worksheet.spreadsheet.client.request("post", url, json=payload)

def writetoactualsheet(horizontal_value,actual_value,vertical_value,note):
    sheet = client.open("python test").worksheet('Sheet3')
    cell_list = sheet.range('A1:AM66')
    for cell in cell_list:
        if(cell.value==horizontal_value):
            coll=cell.col
        if(cell.value==vertical_value):
            roww=cell.row
    sheet.update_cell(roww,coll,actual_value)
    insert_note(sheet,[roww,coll],note)
    return(None,None,None,None)

def writetoactualsheetnetwork(horizontal_value1,actual_value1,vertical_value1,note1):
    sheet = client.open("python test").worksheet('Network')
    cell_list1 = sheet.range('A1:AM66')
    for cell in cell_list1:
        if(cell.value==horizontal_value1):
            coll1=cell.col
        if(cell.value==vertical_value1):
            roww1=cell.row
    sheet.update_cell(roww1,coll1,actual_value1)
    insert_note(sheet,[roww1,coll1],note1)
    return(None,None,None,None)

def getfromsheet(data):
    print(data)
    sheet = client.open("python test").worksheet('dump')
    return(str(sheet.get_all_records()))

def getinstalldatafromsheet():
    sheet=client.open("python test").worksheet('Sheet2')
    return (str(sheet.get_all_records()))


#
#
def clearsheet():
    sheet = client.open("python test").worksheet('dump')
    sheet.clear()
    return(None)
#
def writetosheet(count,value):
    sheet = client.open("python test").worksheet('dump')
    sheet.update_cell(count+1,1,value)
    return (None,None)


    # data=sheet.get_all_records()
    # row=sheet.row_values(3)
    # col=sheet.col_values(2)
    # cell=sheet.cell(2,2).value
    # sheet. insert_row(row,2)
    # sheet.delete_row(2)
    # sheet.update_cell(2, 2, "apple")
    # pprint(len(data))






# def ebill_data(channel_name):
#     url='http://ebill.wlink.com.np/client/index.php?module_id=2&mode=list_customer'
#     login_basic_url = 'http://ebill.wlink.com.np/login/login_check.php'
#     now=datetime.now()
#     dat=now.strftime("%Y-%m-%d")

#     #for everything else
#     st=datetime.strptime(dat,'%Y-%m-%d')

#     en=datetime.strptime(dat, '%Y-%m-%d')



#     #datetime formatting for installation per day
#     start=datetime.strptime(dat,'%Y-%m-%d')
#     startdate=start.strftime('%d %b %y')
#     end=datetime.strptime(dat, '%Y-%m-%d')
#     enddate=end.strftime('%d %b %y')

#     #updating clock



#     #date formatting for nettv data
#     strt=datetime.strptime(dat, '%Y-%m-%d')
#     strt_date=start.strftime('%m/%d/%Y')
#     ed=datetime.strptime(dat, '%Y-%m-%d')
#     ed_date=start.strftime('%m/%d/%Y')

# #for esupport pending tickets
#     year=start.strftime("%Y")
#     month=start.strftime("%m")

#     st=datetime.strptime(dat,'%Y-%m-%d')
#     en=datetime.strptime(dat, '%Y-%m-%d')
#     end_date=en.strftime('%Y-%m-%d')
#     start_date=st.strftime('%Y-%m-%d')
#     print(start_date)
#     print(end_date)


#     data = {  #ebill request
#         'username': 'kerina.shrestha',
#         'password': 'keri@2038',
#         'request_uri':"http://ebill.wlink.com.np/mainscreen/login_details.php",
#         'Submit':"Submit"
#         }

#     data2={ #installation per day
#         'user_name': "",
#         'plan_category': "",
#         'exceedFilter': "<=",
#         'exceed_days': "",
#         'includeDisable':"Y",
#         'owner': "WORLDLINK+IV",
#         'atype': "",
#         'supportzone_id':"50",
#         'marketed_by':"",
#         'service': "",
#         'cfrom':startdate,
#         'cto':enddate,
#         'rfrom':"",
#         'rto':"",
#         'exfrom':"",
#         'exto':"",
#         'reportType':"user",
#         'button':"+++++List+Users+++++"
#         }

#     data3={  #ebill refundable
#         'search_text':"",
#         'branch':"50",
#         'operator': "",
#         'flag_receive_refund':"REFUNDED",
#         'payment_type': "",
#         'date_from': dat,
#         'date_to': dat,
#         'submit': "Submit"
#         }
#     with requests.Session() as s:
#         #ebill log in
#         noww=dt.datetime.now()
#         time_update=str(noww.hour) + ":" + str(noww.minute)
#         print (time_update)
#         response = s.post(login_basic_url , data)
#         print('ebill logged in')
#         time.sleep(1)

    



#     #total number of installs today
#         clearsheet()
#         try:
#             response2=s.post("http://ebill.wlink.com.np/listusers/index.php",data=data2)
#             soup=BeautifulSoup(response2.content,'html.parser')
#             a=soup.find('table' ,id='list-table')
#             install = (a.find_all('tr'))
#             b=(a.find_all('td'))
#             print ("Todays installation : "+str(len(install)-1))
#             total_install=(len(install)-1)
#             i=20
#             j=1
#             for b[i] in b:
#                 writetosheet(j,b[i+18].text)
#                 i=i+21
#                 j=j+1
#                 if (i>(len(b))-2):
#                     break
#             writetoactualsheet(start_date,total_install,'total installation',getinstalldatafromsheet())
#             installmsg="-Installation data filled\n"
#         except:
            
#             writetoactualsheet(start_date,"0",'total installation',getinstalldatafromsheet())
#             installmsg="-Installation data filled\n"



#     #credit note details
#         clearsheet()
#         response3 = s.get("http://ebill.wlink.com.np/credit_note/index.php?by_username=&username=&credit_note_number=&branch=50&optfiscal=17-JUL-19:15-JUL-20&date_from={}&date_to={}&go= Go ".format(start_date,end_date))
#         soup2=BeautifulSoup(response3.content,'html.parser')
#         credit_note=soup2.find('table', id='einvoice_report')
#         try:
#             aa=credit_note.find_all('tr')
#             i=1
#             for i in range(1,len(aa)-1):
#                 print(aa[i].text)
#                 writetosheet(i,aa[i].text)
#                 i=i+1
#             writetoactualsheet(start_date,len(aa)-3,'number of credit note',getfromsheet('data'))
#         except:
#             print('no credit note')
#             writetoactualsheet(start_date,'0','number of credit note','no credit note')
#         creditmsg="-Credit note data filled\n"


#     #invoice details
#         try:
#             response4=s.get("http://ebill.wlink.com.np/einvoice/index.php?by_username=&username=&invoice_number=&subscriber_name=&tpin_no=&branch=&optfiscal=17-JUL-20:15-JUL-21&date_from={}&date_to={}&collection_mode=offline&optcashchq=&go= Go ".format(dat,dat))
#             soup3=BeautifulSoup(response4.content,'html.parser')
#             aaa=soup3.find('table', id='einvoice_report')
#             bbb=aaa.find_all('td')
#             print("Amount received(front desk and mobile app) : "+bbb[len(bbb)-2].text)
#             response5=s.get("http://ebill.wlink.com.np/einvoice/index.php?by_username=&username=&invoice_number=&subscriber_name=&tpin_no=&branch=&optfiscal=17-JUL-20:15-JUL-21&date_from={}&date_to={}&collection_mode=online&optcashchq=&go= Go ".format(dat,dat))
#             soup4=BeautifulSoup(response5.content,'html.parser')
#             aaa1=soup4.find('table', id='einvoice_report')
#             bbb1=aaa1.find_all('td')
#             print("Amount received(online) : "+bbb1[len(bbb1)-2].text)
#             total=float(bbb[len(bbb)-2].text)+float(bbb1[len(bbb1)-2].text)
#             print("Total : "+ str(total))
#             writetoactualsheet(start_date,bbb[len(bbb)-2].text,'Revenue(Front desk and Moblie Apps)',None)
#             writetoactualsheet(start_date,bbb1[len(bbb1)-2].text,'Revenue(online)',None)
#             writetoactualsheet(start_date,str(total),'Total revenue',None)
            
#         except:
#              print('no invoice note')
#         invoicemsg="-Invoice details filled\n"


#     #refund details
#         clearsheet()
#         time.sleep(2)
#         refund=s.post('http://ebill.wlink.com.np/refundabledeposit/index.php?module_id=83&mode=list&action=list',data=data3)
#         soup6=BeautifulSoup(refund.content,'html.parser')
#         i=0
#         for i in range(0,len(soup6.find_all('tr',bgcolor="#E9967A"))):
#             refund1=soup6.find_all('tr',bgcolor="#E9967A")[i]
#             #print(refund1.find_all('td')[1].text+"   "+refund1.find_all('td')[2].text+"   "+refund1.find_all('td')[3].text+"   "+refund1.find_all('td')[4].text+"   "+refund1.find_all('td')[6].text+"   "+refund1.find_all('td')[8].text+"   "+refund1.find_all('td')[9].text)
#             reff=refund1.find_all('td')[1].text+"   "+refund1.find_all('td')[2].text+"   "+refund1.find_all('td')[3].text+"   "+refund1.find_all('td')[4].text+"   "+refund1.find_all('td')[6].text+"   "+refund1.find_all('td')[8].text+"   "+refund1.find_all('td')[9].text
#             print(reff)
#             writetosheet(i+1,reff)
#             i=i+1
#         print('refund : '+str(i))
#         writetoactualsheet((start_date),i,'Number of refunds',getfromsheet(" "))
#         refundmsg="-Refund data filled\n"


#     #nettv users mapping
#         clearsheet()
#         time.sleep(2)
#         nettv=s.get('http://ebill.wlink.com.np/nettv/index.php?user_search=&mac_search=&operator=&branch_name=BANSBARI&from_date={}&to_date={}'.format(strt_date,ed_date))
#         soup7=BeautifulSoup(nettv.content,'html.parser')
#         i=0
#         for i in range(0,len(soup7.find_all('tr',class_='macrow'))):
#             net=soup7.find_all('tr',class_='macrow')[i]
#             abc=(net.find_all('td')[2].text+"  "+net.find_all('td')[3].text+"  "+net.find_all('td')[5].text+"  "+net.find_all('td')[6].text)
#             writetosheet(i+1,abc)
#             i=i+1
#         print('nettv : '+str(i))
#         writetoactualsheet(start_date,i,"nettv user mapping",getfromsheet('dump'))
#         nettvmsg="-Nettv data filled\n"
        
#         #network data
#         print(start_date)
#         driver=webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
#         driver.get("http://ftth.wlink.com.np/index.php/login")
#         username=driver.find_element_by_name("username")
#         username.send_keys("pratik.tamrakar")
#         password=driver.find_element_by_name("password")
#         password.send_keys("Hyper2020$#@")
#         login=driver.find_element_by_name("submit")
#         login.click()
#         time.sleep(1)
#         driver.get("http://ftth.wlink.com.np/index.php/home/splitterPortStatus")
#         time.sleep(60)
#         #basundhara
#         data_bsdr=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[59]/dt")
#         free_bsdr=(data_bsdr.text)[7:11]
#         olt_bsdr=(data_bsdr.text)[0:4]
#         total_bsdr=(data_bsdr.text)[12:16]
#         if(olt_bsdr=="BSDR"):
#             writetoactualsheetnetwork(start_date,total_bsdr,"BSDR total","")
#             writetoactualsheetnetwork(start_date,free_bsdr,"BSDR free","")
#         #budhanilkantha
#         data_bnkt=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[37]/dt")
#         free_bnkt=(data_bnkt.text)[7:11]
#         olt_bnkt=(data_bnkt.text)[0:4]
#         total_bnkt=(data_bnkt.text)[12:16]
#         if(olt_bnkt=="BNKT"):
#             writetoactualsheetnetwork(start_date,total_bnkt,"BNKT total","")
#             writetoactualsheetnetwork(start_date,free_bnkt,"BNKT free","")

#         #dhapasi
#         data_dhap=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[109]/dt")
#         free_dhap=(data_dhap.text)[7:11]
#         olt_dhap=(data_dhap.text)[0:4]
#         total_dhap=(data_dhap.text)[12:16]
#         if(olt_dhap=="DHAP"):
#             writetoactualsheetnetwork(start_date,total_dhap,"DHAP total","")
#             writetoactualsheetnetwork(start_date,free_dhap,"DHAP free","")
#         #mandikhatar
#         data_mdkr=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[218]/dt")
#         free_mdkr=(data_mdkr.text)[7:11]
#         olt_mdkr=(data_mdkr.text)[0:4]
#         total_mdkr=(data_mdkr.text)[12:16]
#         if(olt_mdkr=="MDKR"):
#             writetoactualsheetnetwork(start_date,total_mdkr,"MDKR total","")
#             writetoactualsheetnetwork(start_date,free_mdkr,"MDKR free","")
#         #golfutar
#         data_gftr=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[142]/dt")
#         free_gftr=(data_gftr.text)[7:11]
#         olt_gftr=(data_gftr.text)[0:4]
#         total_gftr=(data_gftr.text)[12:16]
#         if(olt_gftr=="GFTR"):
#             writetoactualsheetnetwork(start_date,total_gftr,"GFTR total","")
#             writetoactualsheetnetwork(start_date,free_gftr,"GFTR free","")
#         #tokha
#         data_tkha=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/dl[321]/dt")
#         free_tkha=(data_tkha.text)[7:11]
#         olt_tkha=(data_tkha.text)[0:4]
#         total_tkha=(data_tkha.text)[12:16]
#         if(olt_tkha=="TKHA"):
#             writetoactualsheetnetwork(start_date,total_tkha,"TKHA total","")
#             writetoactualsheetnetwork(start_date,free_tkha,"TKHA free","")

#         print(olt_bsdr+":"+total_bsdr+":"+free_bsdr
#             +"\n"+olt_bnkt+":"+ total_bnkt+":"+free_bnkt
#             +"\n"+olt_mdkr+":"+total_mdkr+":"+free_mdkr
#             +"\n"+  olt_gftr+":"+total_gftr+":"+free_gftr
#             +"\n"+olt_dhap+":"+total_dhap+":"+free_dhap
#             +"\n"+olt_tkha+":"+ total_tkha+":"+free_tkha)
#         network_msg="-Network sheet filled\n"
#         driver.close()

#     #WRITE TIME TO SHEET
#         writetoactualsheet(start_date,time_update,"updated time",None)
#         timemsg="-Time updated\n"
#         print(time_update)
    
#     #ebill log out
#         time.sleep(2)
#         ebill_logout=s.get('http://ebill.wlink.com.np/login/log_out.php')
#         print('ebill logged out')
#     return(installmsg+creditmsg+invoicemsg+refundmsg+nettvmsg+timemsg+network_msg)    



def jokes():
    browser=requests.get("https://bestlifeonline.com/funny-short-jokes/")
    soup=BeautifulSoup(browser.content,'html.parser')
    jokes=(soup.find('ol', class_='ol1'))
    jokes_list=jokes.find_all('li')
    random_number=randint(1, 25)
    return(jokes_list[random_number].text)

def nextword(target, source):
    for i,w in enumerate(source):
        if w==target:
            return (source[i+1])

def previousword(target, source):
    for i,w in enumerate(source):
        if w==target:
            return (source[i-1])



def coronacases(country):

    if country=='world':
        browser=requests.get("https://www.worldometers.info/coronavirus")
    else:
        browser=requests.get("https://www.worldometers.info/coronavirus/country/{0}".format(country))
    soup=BeautifulSoup(browser.content,'html.parser')
    abc=(soup.find('div',class_='content-inner'))
    cases=("Coronavirus cases : "+abc.find_all('span')[0].text+"\n")
    deaths=("Deaths : "+abc.find_all('span')[1].text+"\n")
    recovery=("Recovered : "+abc.find_all('span')[2].text)
    allcases="```"+cases+deaths+recovery+"```"
    return(allcases)            

def userstatus(username):  #userstatus function for slack
    r=requests.get("https://api-int-beta.wlink.com.np/single_request/{0}".format(username))
    r2=requests.get("https://api-int-beta.wlink.com.np/common/checkUserNetwork/{0}?callback=jQuery22007343626478585873_1591514865046&_=1591514865048".format(username))
    c=r2.content.decode('utf-8')
    d=c.replace("jQuery22007343626478585873_1591514865046(","")
    e=d.replace(")","")
    s=json.loads(e)
    

    ##print(days.text)
    a=r.text
    b=r.json()

    ##print ("the support zone is : ")
    status= b ['customer_details_arr']['ACCOUNT_INFO'] ['STATUS']

      #json value extraction
    days_remaining=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['DAYS_LEFT']

    Grace=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['GRACE_STATUS']
    support_zone=r.json()['customer_details_arr'] ['EXTRA_INFO'] ['SUPPORT_ZONE']
    sts=(status+" "*19)[:12]#for setting the space limit for better allignment
    dys=(days_remaining+" "*19)[:16]
    grc=(Grace+" "*19)[:8]
    if (s['message']['status']==None ):
        alldata="Status : "+sts+"\nDays remaining : "+dys+"\nGrace : "+grc+"\nSupport Area : "+support_zone+"\n\n"
            
    else:
        reftt="TT : "+s['message']['reference']
        print (reftt)
        title=s['message']['referenceTitle']
        print(title)
        rfo=s['message']['publish_desc']
        print(rfo)
        if(s['message']['publish_desc']==None):
            alldata=reftt+"\n"+"Title : "+title+"\nRFO : unknown\n"+"Status : "+sts+"\nDays remaining : "+dys+"\nGrace : "+grc+"\nSupport Area : "+support_zone+"\n\n"
        else:    
            alldata=reftt+"\n"+"Title : "+title+"\n"+rfo+"\n"+"Status : "+sts+"\nDays remaining : "+dys+"\nGrace : "+grc+"\nSupport Area : "+support_zone+"\n\n"
    return(alldata)         


        