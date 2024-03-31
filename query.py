import feedparser
from api import chat_paper

""" query 的parameters 对应arxiv 官网
prefix	explanation
ti	Title
au	Author
abs	Abstract
co	Comment
jr	Journal Reference
cat	Subject Category
rn	Report Number
id	Id (use id_list instead)
all	All of the above
"""
# max_results 一次最大300000 超过分次导出

# 定义搜索关键词
query = 'ti:benchmark+AND+cat:cs.CL'
start_time = "20231101"
end_time = "20240329"



# 定义arXiv搜索的URL
url = f'http://export.arxiv.org/api/query?search_query={query}+AND+submittedDate:[{start_time}+TO+{end_time}]&start=0&max_results=50000'

# 使用feedparser库解析URL
feed = feedparser.parse(url)

f = open("output.txt", "w")

# 输出搜索结果
for entry in feed.entries:
    f.write("Title:  "+entry.title)
    f.write("\n")
    f.write("Authors: "+entry.author)
    f.write("\n")
    f.write("Summary: "+chat_paper(entry.summary))
    f.write("\n")
    f.write("arXiv Link: "+str(entry.link))
    f.write("\n")
    f.write("\n")
f.close()
