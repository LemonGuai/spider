import json
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re
#获取页面
def get_one_page(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
#处理页面
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a.*?href="(.*?)"'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'ranking': item[0],
            'title': item[2],
            'actors': item[3].strip()[3:]  
        }
# 获取电影简介
def get_intro(item):
    intro_url = 'http://maoyan.com'+str(item[1])
    pattern = re.compile('.*?>(.*?)<span.*?>(.*?)</span>',re.S)
    intros = re.findall(pattern,html)
    for intro in intros:
        yield{'introduction':item[0].strip()[3:]}

#将结果存入文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()
#调用方法
def main(num):
    url = 'http://maoyan.com/board/4?offset='+str(num)
    html = get_one_page(url)
    intro = get_intro(item)
    for item in parse_one_page(html):
        print(item)
        print(intro)
        write_to_file(item)
#程序入口
if __name__ == '__main__':

    for i in range(10):
        main(i)