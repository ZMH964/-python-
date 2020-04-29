import requests
from bs4 import BeautifulSoup


def youdao_ying():
    word_yin = jie.find('h2',class_='wordbook-js')
    word = word_yin.find('span').text
    ying = word_yin.find('span',class_='pronounce').find('span')
    mei_yin = word_yin.find_all('span',class_='phonetic')[1]
    fan_yi = jie.find('div',class_='trans-container').text

    print(ci_dian.strip()+':')
    print(word)
    print('英:'+ying.text,end='   美:'+mei_yin.text)
    print(fan_yi.replace(' ',''))


def youdao_zhong():
    word_yin = jie.find('h2',class_='wordbook-js').text
    fan_yi = jie.find('div',class_='trans-container').find('ul').find_all('span',class_='contentTitle')
    print(ci_dian.strip()+':')
    print(word_yin)
    for gh in fan_yi:
        fan = gh.find('a').text
        print(fan)

while True:
    while True:
        try:
            words = input('请输入你要查的单词或中文:')

            headers = {    
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
            url = 'http://dict.youdao.com/w/{}/#keyfrom=dict2.top'.format(words)
            res = requests.get(url,headers=headers)
            jie = BeautifulSoup(res.text,'html.parser')
            ci_dian = jie.find('div',id = 'authTrans').find('h3').text
        except:
            print('--------------------------输入有误，请重新输入--------------------------')
        else:
            break
    try:
        youdao_ying()
    except:
        youdao_zhong()
    ed = input('继续请按enter,退出请输入q:')
    if ed == 'q':
        break
    else:
        continue

