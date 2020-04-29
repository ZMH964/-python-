import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule,time


account = input('请输入你的qq邮箱')
password = input('请输入你qq邮箱的授权码')
to_addr = input('请输入收件人')
#爬取财经头条基金页面的内容与链接
def weat():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
    } 
    res = requests.get('http://www.weather.com.cn/weather/101281601.shtml',headers=headers)
    res.encoding='utf-8'
    jie = BeautifulSoup(res.text,'html.parser')
    di_qu = jie.find('div',class_='crumbs fl').find('a',href = 'http://www.weather.com.cn/weather/101281601.shtml').text
    jk = jie.find('ul',class_='t clearfix').find('li',class_='sky skyid lv3 on')
    day = jk.find('h1').text
    wea = jk.find(class_='wea').text
    tem = jk.find(class_='tem').text
    return di_qu,day,wea,tem
    

#编写发送邮件
def mail(di_qu,day,wea,tem):
    mailhost = 'smtp.qq.com'
    qq_mail = smtplib.SMTP()
    qq_mail.connect(mailhost,25)
    qq_mail.login(account,password)
    weather = di_qu+day+wea+tem
    massge = MIMEText(weather,'plain','utf-8')
    title = '今日天气预报'
    massge['subject'] = Header(title,'utf-8')
    try:
        qq_mail.sendmail(account,to_addr,massge.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qq_mail.quit()



#设置定时任务
def job():
    print('任务开始')
    di_qu,day,wea,tem = weat()
    mail(di_qu,day,wea,tem)
    print('任务完成')


# schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("08:28").do(job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)    

