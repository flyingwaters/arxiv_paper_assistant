## Arxiv_Paper_Assistant
### 检索Arxiv中不同领域和技术的paper，并根据abstract生成一句话总结

******************

1. api.py 调用chatgpt来做摘要的一句话总结
2. query.py 根据query 和 start end time max_results 检索相应的papers
3. test.py 根据query 和 max_results 检索相应的papers 的信息，存储在output.txt文件中，
包括名称，一句话总结，发表时间，和url. python test.py 生成output.txt

******************

