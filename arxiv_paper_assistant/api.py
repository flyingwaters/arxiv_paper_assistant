import arxiv
import openai
import feedparser
from tqdm import tqdm



def open_ai_setting(open_ai_key="", open_ai_base_url=""):
    """
    open_ai_key=""
    open_ai_base_url:if you own the token from openai, this param shoulld not be assigned.
    otherwise you need to buy agent like "https://openkey.cloud/v1"
    在中国推荐可以在https://openkey.cloud/v1 购买
    """
    openai.api_key = open_ai_key
    openai.api_base = open_ai_base_url #

# g = 
def chat_paper(abstract):
    
    sentence = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                      {"role": "user", "content": "使用不超过25个字的一句中文总结下文: "+abstract}
                                    ],
                                    # 流式输出
                                    stream = False)
    return sentence["choices"][0]["message"]["content"]

def search_by_url(url, output_file):
    feed = feedparser.parse(url)
    f = open(output_file, "w", encoding="utf-8")
        # 输出搜索结果
    print("Start feedparser Search: ")
    for entry in tqdm(feed.entries):
            try:
                print()
                print(f"Title*: {entry.title}")
                f.write("Title: "+entry.title)
                f.write("\n")
            except:
                pass
            try:
                f.write("Authors: "+str(entry.author))
                f.write("\n")
            except:
                print("#######################################")
                print(entry)
                print("发生错误")
            try:
                f.write("Summary: "+chat_paper(str(entry.summary)))
                f.write("\n")
            except:
                pass
    
            try:
                f.write("arXiv Link: "+str(entry.link))
                f.write("\n")
                f.write("\n")
            except:
                pass
    print("End Search!!!")
    f.close()

def search_by_api(query, max_results, output_file, sort_order):
    """ 
    基于arxiv api搜索的function 
    """
    print("query:", query)
    print("max_num:", max_results)
    assert sort_order in ["descending", "ascending"], "wrong sort_order"
    sort_dic = {"descending":arxiv.SortOrder.Descending, "ascending":arxiv.SortOrder.Ascending}
    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=sort_dic[sort_order]
    )
    h = search_engine.results()
    
    print("api search start..")
    f = open(output_file, "w", encoding="UTF-8")
    for result in h:
        paper_title = result.title
        paper_url = result.entry_id
        paper_abstract = result.summary.replace("\n", " ")
        publish_time = result.published.date()
        
        print("title: ", paper_title)
        f.write("title: "+paper_title)
        f.write("\n")
        f.write("abstract: "+chat_paper(str(paper_abstract)))
        f.write("\n")
        f.write("link: "+paper_url)
        f.write("\n")
        f.write("publish_time: "+str(publish_time))
        f.write("\n")
        f.write("\n")
    f.close()

    print("end..")