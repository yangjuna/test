import requests
import pyquery
from pyquery import PyQuery as pq




#拿到该界面
def get_zhihu_page(url,headers):
    try:
        page = requests.get(url,headers=headers)
        if page.status_code == 200:
            return page.text
        else:
            return None
    except RequestException:
        return None
#解析界面
def parse_one_page(html):
    doc =pq(html)
    items =doc('.explore-tab .explore-feed.feed-item').items()

    for item in items:
        question = item.find('.question_link').text()
        write_to_file(question)
        author = item.find('.author-link-line').text()
        write_to_file(author)
        answer = pq(item.find('.content').html()).text()
        write_to_file(answer)
#写入文件
def write_to_file(result):
    with open('D:\project/yangjun.txt','a',encoding='utf8')as  f:
        f.write(result)
        f.write('\n' + '=' * 50 + '\n')


url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}



html =get_zhihu_page(url,headers)
parse_one_page(html)