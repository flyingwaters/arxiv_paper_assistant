from arxiv_paper_assistant.arxiv_paper_assistant.api import  search_by_url, search_by_api, open_ai_setting
import arxiv
# max_results 一次最大300000 超过分次导出

# 定义搜索关键词
def search_in_arxiv(query = 'ti:benchmark+AND+cat:cs.CL', start_time = "20230201", end_time = "", max_result = 10, sort_order="ascending", output_name ="output.txt"):
    """
    http://export.arxiv.org/api/query restrict the max_results<=10000 if you have to get it larger 
    we will use arxiv api in this project
    query: the search query, you can refer to the readme file to understand the usage
    start_time: submiitedDate range 
    end_time: submiitedDate range 
    max_results: the limit of papers search result number default = 100
    """
    # arxiv url api require max_results<= 10000
    # 定义arXiv搜索的URL
    if max_result<=10000 and start_time and end_time:
        url = f'http://export.arxiv.org/api/query?search_query={query}+AND+submittedDate:[{start_time}+TO+{end_time}]&start=0&max_results={max_result}&sortOrder={sort_order}'
        search_by_url(url, output_name)
    else:
        query = query.replace("+", " ")
        search_by_api(query, max_result, output_name, sort_order)

if __name__ == "__main__":
    open_ai_setting(open_ai_key="sk-JD4xQJ5Baie2mvnU75Fa3fA9767d40DcB5Ad1e8610Bf0101", open_ai_base_url="https://openkey.cloud/v1" )
    search_in_arxiv()
