import requests
from bs4 import BeautifulSoup

#爬取网页内容
def get_html(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

#提取网页信息
def deal_html(list,html):
	soup = BeautifulSoup(html,'html.parser')
	info = soup.select('body .container')
	info3 = info.select('.layoutLeft')
	info2 = info3.select('.middle-focus-news')
	for li in info2.select('ul'):
		name = li.select('a')

		# plays = li.select('a')
		# b = plays.attrs['title']
		# c = b.split( )
			# list.append([rank[0].text,name[0].text,c[-1],info[0].text])
		list.append(name[0].text)

#输出结果
def print_html(list):
		# tplt = "{:^10}\t{:^25}\t{:^25}\t{:^25}"
		# print(tplt.format('排名','番剧名称','播放次数','更新情况'))
		tplt = "{:^10}"
		print(tplt.format('新闻'))
		for i in range(5):
			u = list[i]
			# print(tplt.format(u[0],u[1],u[2],u[3]))
			print(tplt.format(u[0]))

#主函数
def main():
	list1 = []
	url = 'http://www.qq.com/'
	r = requests.get(url)
	print(r.status_code)
	html = get_html(url)
	deal_html(list1,html)
	print_html(list1)
main()