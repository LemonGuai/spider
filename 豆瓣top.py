import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for item in soup.select('.item'):
        title = item.select('.title')
        em = item.select('em')
        rating_num = item.select('.rating_num')
        if(len(title)>1):
            ulist.append([em[0].text,title[0].text,title[1].text,rating_num[0].text])
        else:
            ulist.append([em[0].text,title[0].text,'null',rating_num[0].text])

            
    
    

        
        
    
    

def printUnivList(ulist,num):
    tplt = "{:5}\t{:^12}\t{:^38}\t{:^4}"
    print(tplt.format('电影排名','电影名称','电影副称','电影评分'))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3]))
        print ("\n")
        
          



def main():
    uinfo =[]
    page = 9
    for i in range(page):
        
        url = 'https://movie.douban.com/top250?start=' + str(i*25)
        html = getHTMLText(url)
        fillUnivList(uinfo,html)
    printUnivList(uinfo,250)
main()
