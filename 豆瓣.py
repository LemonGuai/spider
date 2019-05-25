import requests
from bs4 import BeautifulSoup

#爬取网页
def gethtml(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""


#提取网页信息
def dealhtml(list,html):
	soup = BeautifulSoup(html,'html.parser')
	for tag in soup.select('.item'):
		number = tag.select('em')
		name = tag.select('.title')
		stri = tag.select('.bd p')
		b = stri[0].text
		dic = b.split( ) #切片,将导演提取出来
		if len(name)>0:
			list.append([number[0].text,name[0].text,dic[1]])

#输出信息
def printlist(list):
	tplt = "{:^10}\t{:^50}\t{:^50}"
	print(tplt.format('排名','电影名称','导演'))
	for i in range(250):
		u=list[i]
		print(tplt.format(u[0],u[1],u[2]))
		# print("")


#主函数
def main():
	uinfo=[]
	for i in range(10):
		url="https://movie.douban.com/top250?start="+str(i*25)
		html = gethtml(url)
		dealhtml(uinfo,html)
	printlist(uinfo)
main()
