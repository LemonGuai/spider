import requests
import re
import json
from os.path import exists


# 获取网页
def get_url(url):
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def write_into_txt(txt):
    with open('E:\\computer\\Python\\programs\\爬虫\\猫眼爬虫\\test.txt',
              'a',
              encoding='utf-8') as file:
        file.write(txt)


def read_txt(file_name):
    if exists(file_name):
        print("> 爬虫文件存在")
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    return 0


# 提取数据
def parser_text(html):
    # 正则表达式
    pattern = re.compile(
        r'<i class="board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?class="board-img".*?class="name">.*?>(.*?)<.*?class="star">(.*?)<.*?class="releasetime">上映时间：(.*?)</p>.*?class="integer">(.*?)</.*?class="fraction">(.*?)<',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        dic = {
            '排名': item[0],
            '图片': item[1],
            '电影名称': item[2].strip(),
            '主演': item[3].strip()[3:],
            '上映时间': item[4].strip()[:10],
            '评分': item[5] + item[6]
        }
        print(dic)
        # 存入文件中
        book_list = json.dumps(dic, ensure_ascii=False)
        path = 'E:\\computer\\Python\\programs\\爬虫\\猫眼爬虫\\result.txt'
        with open(path, 'a', encoding='utf-8') as file:
            file.write(book_list + "\n")
        if exists(path):
            print(f"> 数据结果已经保存至{path}")


# 主函数
def main():
    for a in range(5):
        num = a * 10
        url = f"https://maoyan.com/board/4?offset={num}"
        html = get_url(url)
        write_into_txt(html)
        file = 'E:\\computer\\Python\\programs\\爬虫\\猫眼爬虫\\test.txt'
        html_read = read_txt(file)
        # print(html_read)
    dic = parser_text(html_read)
    print(dic)
    # create_txt(dic)
    # write_into_txt(dic)


if __name__ == "__main__":
    main()