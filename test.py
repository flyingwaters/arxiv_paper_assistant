import arxiv
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

query = "ti:benchmark AND cat:cs.CL"
max_results = 100000


search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
h = search_engine.results()
print("start..")
f = open("output.txt", "w")
for result in h:
        paper_id = result.get_short_id()
        paper_title = result.title
        paper_url = result.entry_id
        print(paper_title)
        paper_abstract = result.summary.replace("\n", " ")
        primary_category = result.primary_category

        publish_time = result.published.date()
        update_time = result.updated.date()
        f.write("title: "+paper_title)
        f.write("\n")
        f.write("abstract: "+chat_paper(paper_abstract))
        f.write("\n")
        f.write("link: "+paper_url)
        f.write("\n")
        f.write("publish_time: "+str(publish_time))
        f.write("\n")
        f.write("\n")
f.close()

print("end..")