#ANJEE version(0.1)
#A self learning artificial intelligence bot

from slackclient import SlackClient
import time
from flask import json
from bs4 import BeautifulSoup
import requests
import itertools
from function import coronacases
from function import userstatus
from function import nextword
from function import jokes
from function import previousword
import websocket
from selenium.webdriver.support.select import Select
from selenium import webdriver
import os
import re
from random import *




slack_token = 'xoxb-1161223414533-1167206867861-PkgzQsccSxNNXqG9DXvYtal9'  #token for anjee

sc =  SlackClient(slack_token)
login_basic_url = 'http://ftth.wlink.com.np/index.php/login/processLogin'
data = {
        'username': 'pratik.tamrakar',
        'password': 'Hyper2020$#@'
        }       

def oltid_values(oltname):
    names=['AMGR','BALJ','BDGN','BDHA','BHTR','BKNI','BKPT',
           'BKTP','BLKT','BLMB','BLTR','BMGL','BNGR','BNKT',
           'BNSH','BODE','BSDR','BSPT','BTBN','CHAU','CHBL',
           'CHPT','CKPT','CMSG','CPGN','DBGT','DHAP','DHTI',
           'DHUN','DMBR','DWKT','FCPK','FPNG','FTNG','GDHR',
           'GDWR','GFTR','GTHR','GWRK','HTBN','IMDL','JAWL',
           'JAWLTD','JAWLTEST02','JGTE02','JRPT','JRPT02','JRPT03',
           'KLSH','KLTR','KMCB','KOTS','KPAN','KPAN02','KPAN03','KRTP',
           'KSBU','KSNT','KSNT02','LUBU','LZMP','LZMP02','MDKR','MLPN',
           'MNMJ','MTDV','NBNS','NGKT','NIKP','NIKP02','NKHU','NLCK','NPLZ',
           'NRPT','OBNS','PLBR','PNGA','PPSI','PSDK','PSDK02','RBVN',
           'RJNA','RNBN','RNBR','SANO','SBNG','SCTR','SDJL','SDPR','SDPR02',
           'SLGR','SMGL','SMKU','SNGR','SNPA','SRTR','STCK','STPL','SUMT',
           'SWMB','SYNR','TDHA','TEKU','THCL','THCO','THLI','THMI','TKHA',
           'TNKT','TPTL']
           
           
    values=["199","5","41","77","265","252","87","19",
            "187","264","54","207","46","172","234","57","310",
            "358","223","290","74","45","49","340","279","118",
            "22","21","24","53","243","319","216","235","136",
            "192","34","78","7","111","10","58","3","151","226",
            "6","177","327","43","2","190","44","16","158","349",
            "23","60","152","277","284","62","372","38","143","237",
            "61","32","153","245","375","40","222","286","115","52",
            "88","79","4","36","288","342","117","336","295","334",
            "146","11","229","84","359","56","51","18","269","39",
            "114","231","95","134","8","347","262","42","50","292",
            "221","35","251","154","293"]
    
    i=0
    for names[i] in names:#for values in sequence
        if oltname==names[i]:
            return(values[i])
        else:
            i=i+1

# def onm_pending(stdate,endate,channel):
#     head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
#     data_fortroubleonm={"search_text":"","status":"notsolved","assigned_to":"5","userGroup":"667","created_by":"","from_date":stdate,"to_date":endate,"category":"","accepted_by":"","watched_tickets":"","filter_submit":"1","custom":""}
#     #data_forexpansion={"search_text":"","status":"notsolved","assigned_to":"5","userGroup":"668","created_by":"","from_date":start,"to_date":end,"category":"","accepted_by":"","watched_tickets":"","filter_submit":"1","custom":""}
#     #data_enterprisefiber={"search_text":"","status":"notsolved","assigned_to":"5","userGroup":"812","created_by":"","from_date":start,"to_date":end,"category":"","accepted_by":"","watched_tickets":"","filter_submit":"1","custom":""}
#     #data_enterprisesupport={"search_text":"","status":"notsolved","assigned_to":"5","userGroup":"853","created_by":"","from_date":start,"to_date":end,"category":"","accepted_by":"","watched_tickets":"","filter_submit":"1","custom":""}
#     with requests.Session() as s:
#         s.get("https://tt.wlink.com.np/login")    
#         s.post("https://tt.wlink.com.np/login/verify",data={"username":"pratik.tamrakar","password":"Hyper2020$#@"},headers=head)
#         response=s.post("https://tt.wlink.com.np/dashboard/get_dashboard_data_table",data=data_fortroubleonm)
#         soup=BeautifulSoup(response.content,'html.parser')
#         aa=soup.find("table",class_="table2")
#         i=2
#         j=0
#         postToSlack(channel=channel,message="`"+"Urgent and important pending troubleshoots of bansbari from "+stdate+" to "+endate+" : "+"`")
#         for i in range(i,len(aa.find_all('td')),9):
#             trouble_data=aa.find_all('td')[i].text[31:120]
#             msg=trouble_data.split(" ")
#             if "outage" in str(msg).lower():
#                 try:
#                     message1="```"+previousword("-",msg)+" "+"Outage : "+nextword("at",msg)+"```"
#                     postToSlack(channel=channel,message=message1)
#                 except:
#                     message1="```"+trouble_data+"```"
#                     postToSlack(channel=channel,message=message1)

#             elif "no" in str(msg).lower():
#                 message1="```"+trouble_data+"```"
#                 postToSlack(channel=channel,message=message1)
#             elif "bad" in str(msg).lower():
#                 message1="```"+trouble_data+"```"
#                 postToSlack(channel=channel,message=message1)
#             elif "pole" in str(msg).lower():
#                 message1="```"+trouble_data+"```"
#                 postToSlack(channel=channel,message=message1)        
#             j=j+1
#         message2="```"+"All troubleshoots :  : "+str(j)+"```"
#         postToSlack(channel=channel,message=message2)
        
#         #tt logout
#         s.get("https://tt.wlink.com.np/logout")
#     return(None,None,None)          

def esupportdata(username):
    with requests.Session() as s:
        esupport=s.post("https://esupport.wlink.com.np/new_tickets/login.php",data={"username":"pratik.tamrakar","password":"Hyper2020$#@","redirecturi":""})
        print('esupport logged in')
        pwr=s.post("http://esupport.wlink.com.np/new_tickets/trouble_ticket_new/index.php/ajax/fttxConnectionInfo",data={"machine_name":username})
        c=pwr.content.decode('utf-8')
        d=c.replace("jQuery22007343626478585873_1591514865046(","")
        e=d.replace(")","")
        print(e)
        power_username=json.loads(e)
        tx_power="Tx power : "+str(power_username["rxpower"])
        oltrx_power="OLT Rx power : "+str(power_username["oltRxPower"])
        last_down="Last down cause : "+str(power_username["lastdowncause"])
        ont_ip="ONT IP : "+str(power_username["ontip"])
        ont_id="ONT id : "+str(power_username["ont_id"])
        ont_serial="ONT serial : "+str(power_username["serial"])
        if(power_username["oltvendor"]=="Huawei"):
            if (power_username["state"]=="1"):
                status="Status : online"
            else:
                status="Status : offline"
        if(power_username["oltvendor"]=="Nokia"):
            if (power_username["state"]==True):
                status="Status : online"
            else:
                status="Status : offline"
        gpon="GPON : "+str(power_username["gpon"])
        pon_port="PON port : "+str(power_username["ponport"])            
        splitter_id="splitter id : "+str(power_username["splitter_id"])
        splitter_port="splitter port : "+str(power_username["splitter_port"])
        admin_state="ONT admin state : "+str(power_username["ontAdminState"])
        olt="OLT : "+str(power_username["oltname"])
        olt_vendor="OLT vendor : "+str(power_username["oltvendor"])
        logout=s.get('http://esupport.wlink.com.np/new_tickets/logout.php')
        print('esupport logged out')
        return (tx_power+"\n"+oltrx_power+"\n"+last_down+"\n"+ont_ip+
            "\n"+ont_id+"\n"+ont_serial+"\n"+status+"\n"+gpon+"\n"+pon_port+"\n"+splitter_id+
            "\n"+splitter_port+"\n"+admin_state+"\n"+olt+"\n"+olt_vendor)

def oltRxPower(x,channel):
    def usersassigned(y):#function for 1 distributions only
    #splitter detail page in soup
        index_page= s.get('http://ftth.wlink.com.np/index.php/splitters/splitterDetail/{0}'.format(y))     
        soup = BeautifulSoup(index_page.content, 'html.parser')

        esupport=s.post("https://esupport.wlink.com.np/new_tickets/login.php",data={"username":"pratik.tamrakar","password":"Hyper2020$#@","redirecturi":""})
        print('esupport logged in')
        
    
    #for finding and displaying the usernames 
        users=soup.find('div',class_='container')
        i=16
        for td in users.table.find_all('td'):      
            usernames=users.table.find_all('td')[i].text
            if (usernames!=""):
                pwr=s.post("http://esupport.wlink.com.np/new_tickets/trouble_ticket_new/index.php/ajax/fttxConnectionInfo",data={"machine_name":usernames})
                c=pwr.content.decode('utf-8')
                d=c.replace("jQuery22007343626478585873_1591514865046(","")
                e=d.replace(")","")
                power_username=json.loads(e)
                diff=power_username["oltRxPower"]-power_username["rxpower"]
                msg00="```"+usernames+":"+"\n\t"+str(power_username["rxpower"])[0:7]+"\t"+str(power_username["oltRxPower"])[0:7]+"\t"+str(diff)[0:5]+"```"
                postToSlack(channel=channel,message=msg00)                        
                i=i+10
                if i>len(users.table.find_all('td')):
                    break
            else:
                i=i+10    
                if i>len(users.table.find_all('td')):
                    break

        return(None)

    def masterusers(linksss):#function for master for displaying users of all distributions
        try:
            index_page4=s.get(linksss)
            soup4=BeautifulSoup(index_page4.content, 'html.parser')
    
    

    #for finding and displaying the usernames
            users_master=soup4.find('div',class_='container')
            i=16
            j=0
            
            for td in users_master.table.find_all('td'):
                random_number=randrange(16,len(users_master.table.find_all('td')),10)
                usernames=users_master.table.find_all('td')[random_number].text
                if(usernames!=""):
                    pwr=s.post("http://esupport.wlink.com.np/new_tickets/trouble_ticket_new/index.php/ajax/fttxConnectionInfo",data={"machine_name":str(usernames)})
                    c=pwr.content.decode('utf-8')
                    d=c.replace("jQuery22007343626478585873_1591514865046(","")
                    e=d.replace(")","")
                    power_username=json.loads(e)
                    diff=power_username["oltRxPower"]-power_username["rxpower"]
                    msg00="```"+usernames+":"+"\n\t"+str(power_username["rxpower"])[0:7]+"\t"+str(power_username["oltRxPower"])[0:7]+"\t"+str(diff)[0:5]+"```"
                    postToSlack(channel=channel,message=msg00)
                    i+=10
                    j=j+1
                else:
                    i=i+10    
                if(i>len(users_master.table.find_all('td'))):
                        break
                if (j>=1):
                        break
        except Exception as e:
            print(e)
            msgg="`"+"exception occured, Please try the command once more!!!"+"`"
            postToSlack(channel=channel,message=msgg)
                           
        return(None)
                
 
            
    with requests.Session() as s: #shortcut for requests
        browser=s.get('http://ftth.wlink.com.np/index.php/login/processLogin')
        response = s.post(login_basic_url , data)    

    #for verifying if the provided splitter is master or distribution    
        index_page2=s.get('http://ftth.wlink.com.np/index.php/splitters/updateSplitter/{0}'.format(x))
        soup2=BeautifulSoup(index_page2.content,'html.parser')
        types=soup2.find('ul',class_='form')
        splitter_type=("`"+"splitter type : "+types.findAll('option', selected=True)[1].text+"`"+"\n")#displays the splitter type if selection is true
        postToSlack(channel=channel,message=splitter_type)
        if(types.findAll('option', selected=True)[1].text)=='Distribution':
            usersassigned(x)
            logout=s.get('http://esupport.wlink.com.np/new_tickets/logout.php')
            print('esupport logged out')
        

        else:
            esupport=s.post("https://esupport.wlink.com.np/new_tickets/login.php",data={"username":"pratik.tamrakar","password":"Hyper2020$#@","redirecturi":""})
            print('esupport logged in')
            index_page3=s.get("http://ftth.wlink.com.np/index.php/splitters/splitterDetail/{0}".format(x))
            soup3=BeautifulSoup(index_page3.content,'html.parser')
            types2=soup3.find('table',class_='table')
            links=types2.findAll('a', href=re.compile('^http://ftth.wlink.com.np/index.php/splitters/splitterDetail'))
            i=0
            postToSlack(channel=channel,message="`"+"Showing Rx differences of some random users of the master : "+str(x)+"`")
            for link in links:
                links_master=link.get('href')#for getting all the filtered links one by one
                masterusers(links_master)#function call
            logout=s.get('http://esupport.wlink.com.np/new_tickets/logout.php')
            print('esupport logged out')
    return(None,None)        

def userdisabled(x,channel):
    with requests.Session() as s: 
        def usersassigned(y,chan):#function for 1 distributions only
    #splitter detail page in soup

            index_page= s.get('http://ftth.wlink.com.np/index.php/splitters/splitterDetail/{0}'.format(y))     
            soup = BeautifulSoup(index_page.content, 'html.parser')
    
    #for finding and displaying the usernames 
            users=soup.find('div',class_='container')
            i=16
    #print("Username\tstatus\tdays")
            for td in users.table.find_all('td'):
                if(users.table.find_all('td')[i].text!=""):           
                    usernames=users.table.find_all('td')[i].text
                    r=requests.get("https://api-int-beta.wlink.com.np/single_request/{0}".format(usernames))
                    statuss=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['STATUS'] #json value extraction
                    usr=(usernames+" "*19)[:22]
                    days_remaining=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['DAYS_LEFT']
                    sts=(statuss+" "*19)[:12]#for setting the space limit for better allignment
                    dys=(days_remaining+" "*19)[:16]
                    if(statuss=="Disabled"):
                        postToSlack(channel=chan,message=usr+sts+dys)
                    else:
                        postToSlack(channel=chan,message=usr+sts+dys)        
                i=i+10
                if i>len(users.table.find_all('td')):
                    break

        def masterusers(linkss,chann):#function for master for displaying users of all distributions
            index_page4=s.get(linkss)
            soup4=BeautifulSoup(index_page4.content, 'html.parser')
    
    #for finding and displaying the usernames
            users_master=soup4.find('div',class_='container')
            i=16
            for td in users_master.table.find_all('td'):
        
                if(users_master.table.find_all('td')[i].text!=""):
                 
                    usernames=users_master.table.find_all('td')[i].text
                    r=requests.get("https://api-int-beta.wlink.com.np/single_request/{0}".format(usernames))
                    try:
                        statuss=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['STATUS'] #json value extraction
                        usr=(usernames+" "*19)[:22]
                        days_remaining=r.json()['customer_details_arr'] ['ACCOUNT_INFO'] ['DAYS_LEFT']
                        sts=(statuss+" "*19)[:12]#for setting the space limit for better allignment
                        dys=(days_remaining+" "*19)[:16]
                        if(statuss=="Disabled"):
                            postToSlack(channel=chann,message=usr+sts+dys)
                        else:
                            postToSlack(channel=chann,message=usr+sts+dys)
                
                        i=i+10
                    except:
                        postToSlack(channel=chann,message=usernames)
                        i=i+10
                        break                              
                    if i>len(users_master.table.find_all('td')):
                        break 
        

        print("..."+x+"...")        
        browser=s.get('http://ftth.wlink.com.np/index.php/login/processLogin')
        response = s.post(login_basic_url , data)    

    #for verifying if the provided splitter is master or distribution    
        index_page2=s.get('http://ftth.wlink.com.np/index.php/splitters/updateSplitter/{0}'.format(x))
        soup2=BeautifulSoup(index_page2.content,'html.parser')
        types=soup2.find('ul',class_='form')
        postToSlack(channel=channel,message="splitter type : "+types.findAll('option', selected=True)[1].text+"\n")#displays the splitter type if selection is true

        if(types.findAll('option', selected=True)[1].text)=='Distribution':
           return (usersassigned(x,channel))
        

        else:
            index_page3=s.get("http://ftth.wlink.com.np/index.php/splitters/splitterDetail/{0}".format(x))
            soup3=BeautifulSoup(index_page3.content,'html.parser')
            types2=soup3.find('table',class_='table')
            links=types2.findAll('a', href=re.compile('^http://ftth.wlink.com.np/index.php/splitters/splitterDetail'))
            i=0
            for link in links:
                links_master=link.get('href')#for getting all the filtered links one by one
                masterusers(links_master,channel)
                #function call
    #ftth logout
        s.get("http://ftth.wlink.com.np/index.php/login/logout")            

def splitterdetails(chan,spp_no):
    driver=webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
    response=driver.get("http://ftth.wlink.com.np/index.php/login")
    username=driver.find_element_by_name("username")
    username.send_keys("pratik.tamrakar")
    password=driver.find_element_by_name("password")
    password.send_keys("Hyper2020$#@")
    login=driver.find_element_by_name("submit")
    login.click()
    driver.get("http://ftth.wlink.com.np/index.php/splitters/updateSplitter/{}".format(spp_no))
    time.sleep(3)
    select2 = Select(driver.find_element_by_xpath("//*[@id='splitterType']"))
    selected2_option = select2.first_selected_option
    postToSlack(channel=chan,message=("splitter type : "+selected2_option.text))
    if(selected2_option.text=="Distribution"):
        postToSlack(channel=chan,message=("OLT :"+driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/form/ul[1]/li[1]").text))
        postToSlack(channel=chan,message=("Splitter name : "+driver.find_element_by_xpath("//*[@id='splitterName']").get_attribute("value")))
        postToSlack(channel=chan,message=("Splitter id : "+driver.find_element_by_xpath("//*[@id='splitterName']").get_attribute("placeholder")))
        postToSlack(channel=chan,message=("GPS : "+driver.find_element_by_xpath("//*[@id='latlon']").get_attribute('value')))
        postToSlack(channel=chan,message=("core : "+driver.find_element_by_xpath("//*[@id='core']").get_attribute('value')))
        master=driver.find_element_by_xpath("//*[@id='masterSplitters1']").get_attribute('value')
        postToSlack(channel=chan,message=("Master : "+master))
        #get the selected value from drop down port number
        select = Select(driver.find_element_by_xpath("//*[@id='splitterPorts']"))
        selected_option = select.first_selected_option
        postToSlack(channel=chan,message=("port : "+selected_option.text))
        

        #get the selected value splitter type
        driver.get("http://ftth.wlink.com.np/index.php/splitters/updateSplitter/{}".format(master))
        postToSlack(channel=chan,message=("Master GPS : "+driver.find_element_by_xpath("//*[@id='latlon']").get_attribute('value')))
    elif(selected2_option.text=="Master"):
        postToSlack(channel=chan,message=("OLT :"+driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/form/ul[1]/li[1]").text))
        postToSlack(channel=chan,message=("Splitter name : "+driver.find_element_by_xpath("//*[@id='splitterName']").get_attribute("value")))
        postToSlack(channel=chan,message=("Splitter id : "+driver.find_element_by_xpath("//*[@id='splitterName']").get_attribute("placeholder")))
        postToSlack(channel=chan,message=("GPS : "+driver.find_element_by_xpath("//*[@id='latlon']").get_attribute('value')))
        postToSlack(channel=chan,message=("core : "+driver.find_element_by_xpath("//*[@id='core']").get_attribute('value')))
        ckt_id=driver.find_element_by_xpath("//*[@id='autocompleteckt']").get_attribute("value")
        driver.get("http://ftth.wlink.com.np/index.php/connection")
        ckt=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[1]/form/input[1]")
        ckt.send_keys(ckt_id)
        button=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[1]/form/button")
        button.click()
        update=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[3]/table/tbody/tr/td[7]/a[1]")
        update.click()
        postToSlack(channel=chan,message=("parent master GPS : "+driver.find_element_by_xpath("//*[@id='cktStart']").get_attribute("value")))
    # elif(selected2_option.text=="Extender"):

    else:
        postToSlack(channel=chan,message=("error in splitter number"))
#ftth logout
    logout=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/ul/li[9]/a")
    logout.click()
    driver.close()
    return(None,None)  

def weather_today(place,channel):
    browser=requests.get('https://www.weather-atlas.com/en/nepal/{0}'.format(place))
    soup=BeautifulSoup(browser.content,'html.parser')
    data=soup.find('div',itemtype="https://schema.org/Table")
    time=data.find_all('span',class_='block font_115_rem strong')
    sky=data.find_all('span',class_="font_150_rem strong block font_rem")
    temp=data.find_all('li',class_="font_200_rem")
    rep=("```Today's hourly weather forecast of : "+place+"```")
    postToSlack(channel=channel,message=rep)
    for (a, b, c) in itertools.zip_longest(time, sky, temp):
        reply="`TIME : "+a.text+"---"+b.text+"---"+c.text+"`"
        postToSlack(channel=channel,message=(reply ))
    return(None,None)

def weather_tomorrow(place,channel):
    browser=requests.get('https://www.weather-atlas.com/en/nepal/{0}-weather-tomorrow'.format(place))
    soup=BeautifulSoup(browser.content,'html.parser')
    data=soup.find('div',itemtype="https://schema.org/Table")
    time=data.find_all('span',class_='block font_115_rem strong')
    sky=data.find_all('span',class_="font_150_rem strong block font_rem")
    temp=data.find_all('li',class_="font_200_rem")
    rep=("```Tomorrow's hourly weather forecast of : "+place+"```")
    postToSlack(channel=channel,message=rep)
    for (a, b, c) in itertools.zip_longest(time, sky, temp):
        reply="`TIME : "+a.text+"---"+b.text+"---"+c.text+"`"
        postToSlack(channel=channel,message=(reply ))
    return(None,None)    
        
                   




def power(x,y):
    
    with requests.Session() as s: #shortcut for requests
        postToSlack(channel=y , message = "\n`Please wait..."+"`")
        browser=s.get('http://ftth.wlink.com.np/index.php/login/processLogin')
        response = s.post(login_basic_url , data)
        name_search=s.get("http://ftth.wlink.com.np/index.php/splitters/updateSplitter/{0}".format(x))
        soup2=BeautifulSoup(name_search.content,'html.parser')
        name=soup2.find('div',class_='main_content')
        olt_name=name.find_all('li')[2].text
        send=olt_name[16:20]#filter some characters from text olt name
        result=oltid_values(send)#function call


        #for verifying if the provided splitter is master or distribution
        url='http://ftth.wlink.com.np/index.php/reports/splitterRxPower'
        index_page=s.post(url,data={'olt':result,'splitter':x,'submit':'true'})
        soup=BeautifulSoup(index_page.content,'html.parser')
        table=soup.find('div',class_='main_content')
        i=8
        postToSlack(channel=y , message = "`Displaying power levels for splitter : "+x+"("+send+")"+"`")
        for td in table.find_all('td'):
            length=(table.find_all('td')[i+4].text+" "*22)[:18]
            length2=(table.find_all('td')[i+5].text+" "*19)[:18]          
            response=("```"+length+" : "+length2+"```")
            if(table.find_all('td')[i+5].text!=""):
                postToSlack(channel=y , message = response)
            i=i+7
            if i>len(table.find_all('td')):
                break              
        #ftth logout
        s.get("http://ftth.wlink.com.np/index.php/login/logout")  
    return(None,None)                           



#create read and write to slack methods
def postToSlack(channel, message):
    return sc.api_call("chat.postMessage", channel=channel, text=message, as_user=True)        

#Get bot id
def getBotID(botname):
    msg = sc.api_call("users.list").decode('utf-8') #decodes bytes object array to string
    msg2=json.loads(msg) #converts string to json
    users=msg2['members'] #json object call
    for user in users:
        if 'name' in user and user.get('deleted') == False and botname in user.get('name'):
            return user.get('id')
        # print(user)

def readAndReply(msg, botId):
    if('type' in msg[0] and msg[0].get('type') == 'message'):
        # print(msg[0].get('text'))
        channel = msg[0].get('channel')
        user = msg[0].get('user')
        if(user == botId):
            return ""

            ################## LUIS interaction ##########################
        #--------------- Send query to LUIS
        url = "https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/d8dd7f23-d8e5-497f-b1a7-a3203ea89bb0/slots/production/predict?subscription-key=f0e09835408347abad08eeb442db592a&verbose=true&show-all-intents=true&log=true&query="
        url += msg[0].get('text')
        myResponse = requests.get(url)
        #--------------- Prepare user response based on LUIS repons

        #--------------- Prepare user response based on LUIS reponse
        if (myResponse.ok):
            jData = json.loads(myResponse.content)
            print(jData)
            top_score = float(jData['prediction']['intents'][jData['prediction']['topIntent']]['score'])
            print(top_score)
            senti1=jData['prediction']['sentiment']['label']
            if (top_score > 0.5):
                if((jData['prediction']['topIntent']).lower() == 'weather today'):
                    if ' of ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('of',msg3)
                        weather_today(a,channel)
                    elif ' in ' in jData['query'].lower():#leave spaces ' in '
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('in',msg3)
                        weather_today(a,channel)
                    elif ' at ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('at',msg3)
                        weather_today(a,channel)
                    else:
                        weather_today('kathmandu',channel)
                    rep=""

                elif((jData['prediction']['topIntent']).lower() == 'weather tomorrow'):
                    if ' of ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('of',msg3)
                        weather_tomorrow(a,channel)
                    elif ' in ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('in',msg3)
                        weather_tomorrow(a,channel)
                    elif ' at ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('at',msg3)
                        weather_tomorrow(a,channel)
                    else:
                        weather_tomorrow('kathmandu',channel)
                    rep=""        
                                    
                elif (jData['prediction']['topIntent'].lower() == 'oltrxpower'):
                    msg200=jData['query'].lower()
                    msg300=msg200.split(" ")
                    a=nextword('oltrxpower',msg300)
                    oltRxPower(a,channel)
                    rep=""
 
                elif (jData['prediction']['topIntent'].lower() == 'bored'):
                    postToSlack(channel=channel,message="`Okey listen,I'll tell you a joke!!!`")
                    rep = "```"+jokes()+"```"

                elif(jData['prediction']['topIntent'].lower() == 'splitter details'):
                    message_splitterdetails=jData['query'].lower()
                    message_splitterdetails_1=message_splitterdetails.split(" ")
                    sp_no=nextword('of',message_splitterdetails_1)
                    splitterdetails(channel,sp_no)
                    rep=""
                    #rep ="```"+splitterdetails(channel,sp_no)+"```"

                elif (jData['prediction']['topIntent'].lower() == 'status'):
                    if ' of ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('of',msg3)
                        rep ="```"+userstatus(a)+esupportdata(a)+"```"

                        

                    else:
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('status',msg3)
                        rep ="```"+userstatus(a)+esupportdata(a)+"```"
                        # if rep==None:
                        #     a=previousword(('status',msg3))
                        #     rep=userstatus(a)

                elif (jData['prediction']['topIntent'].lower() == 'help'):
                    greetings="`Hi,greetings!!!`\n`Please feel free to use following commands : `\n\n"
                    powerhelp="```power of <splitter_no>```\n--Shows optical power of splitter.\n\n"
                    statushelp="```status of <username>```\n--Shows active or disabled, days remaining and outages if any.\n\n"
                    covidsts="```covid <country name>```\n--Shows covid data of that country\n\n"
                    weatherhelp="```weather of <placename> today```\n--Shows you the today's weather\n\n"
                    weatherhelp2="```weather of <placename> tomorrow```\n--Shows you the tomorrow's weather\n\n"
                    jokehelp="--ask for a joke. I can tell you one\n\n"
                    oltrxhelp="```oltrxpower <splitter_no>```\n--Gives you the difference in ont and olt Rx power of that splitter\n\n"
                    detailhelp="```details of <splitter_no>```\n--Gives you the gps,cores etc of splitter\n\n"
                    checkdisabledhelp="```checkdisabled <splitter_no>```\n--Gives you the active and disabled users of that splitter\n\n"
                    rep=greetings+powerhelp+checkdisabledhelp+statushelp+covidsts+weatherhelp+weatherhelp2+oltrxhelp+jokehelp+detailhelp

                        
                elif (jData['prediction']['topIntent'].lower() == 'checkdisabled'):
                    if ' of ' in jData['query'].lower():
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('of',msg3)
                        userdisabled(a,channel)
                        rep=""
                        

                    else:
                        msg2=jData['query'].lower()
                        msg3=msg2.split(" ")
                        a=nextword('checkdisabled',msg3)
                        userdisabled(a,channel)
                        rep=""     

                elif (jData['prediction']['topIntent'].lower() == 'covid'):
                    if ' of ' in jData['query'].lower():
                        msg4=jData['query'].lower()
                        msg5=msg4.split(" ")
                        cases=nextword('of',msg5)
                        rep=coronacases(cases)

                    elif ' in ' in jData['query'].lower():
                        msg4=jData['query'].lower()
                        msg5=msg4.split(" ")
                        cases=nextword('in',msg5)
                        rep=coronacases(cases)

                    elif 'covid' in jData['query'].lower(): 
                        msg4=jData['query'].lower()
                        msg5=msg4.split(" ")
                        cases=nextword('covid',msg5)
                        rep=coronacases(cases)
                        # if coronacases(cases)==None:
                        #     cases=previousword(('covid',msg3))
                        #     rep=coronacases(cases)

                    elif 'corona cases' in jData['query'].lower(): 
                        msg4=jData['query'].lower()
                        msg5=msg4.split(" ")
                        cases=nextword('corona cases',msg5)
                        rep=coronacases(cases)
                        # if rep==None:
                        #     cases=previousword(('coronacases',msg3))
                        #     rep=coronacases(cases)



                elif (jData['prediction']['topIntent'].lower() == 'power'):
                    if ' of ' in jData['query'].lower():
                        msg6=jData['query'].lower()
                        msg7=msg6.split(" ")
                        pwr=nextword('of',msg7)
                        power(pwr,channel)
                        rep=""

                    elif ' in ' in jData['query'].lower():
                        msg8=jData['query'].lower()
                        msg9=msg8.split(" ")
                        pwr1=nextword('in',msg9)
                        power(pwr1,channel)
                        rep=""

                    else:
                        msg10=jData['query'].lower()
                        msg11=msg10.split(" ")
                        pwr2=nextword('power',msg11)
                        power(pwr2,channel)
                        rep=""
                else:
                    rep ="Your sentiment is : "+senti1
            
            else:
                rep ="Your sentiment is : "+senti1
        else:
            print(myResponse)
            rep ="Your sentiment is : "+senti1
        ################## END LUIS interaction ######################
        postToSlack(channel=channel , message = rep)
        return (rep,channel)
    else:
        return ""
botId = getBotID('anjee_v0.1')





if sc.rtm_connect():
    READ_WEBSOCKET_DELAY = 1
    message=''
    while True:
        #     msg = sc.rtm_read()
        #     if(str(msg) != '[]' and str(msg) != "[{'type': 'hello'}]"):
        #         message = readAndReply(msg, botId)
                
        #     time.sleep(2)
        # except:
        #     channel = msg[0].get('channel')
        #     rep="I can't understand you, Can you please elaborate!!!"
        #     postToSlack(channel=channel,message=rep)
        
        try:
            
            msg = sc.rtm_read()
            if(str(msg) != '[]' and str(msg) != "[{'type': 'hello'}]"):
                message = readAndReply(msg, botId)
            time.sleep(READ_WEBSOCKET_DELAY)
        except websocket.WebSocketConnectionClosedException as e:
            print (e)
            print ('Caught websocket disconnect, reconnecting...')
            time.sleep(2)
            sc.rtm_connect()
        except ConnectionResetError as e:
            print(e)
            print("connection reset error caught")  
            time.sleep(2)
            sc.rtm_connect() 
        except Exception as e:
            print (e)
            print("")
            channel = msg[0].get('channel')
            rep="I can't understand you, Can you please elaborate!!!"
            postToSlack(channel=channel,message=rep)
            time.sleep(READ_WEBSOCKET_DELAY)
        except ConnectionAbortedError as e:
            print(e)
            print("Connection aborted Error caught")  
            time.sleep(2)
            sc.rtm_connect()              
else:
        print("Connection failed. Invalid Slack token or bot ID?")
                

            