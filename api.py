import openai

open_ai_key="sk-NXXrb0gyGwNQeCmJ549a5c17927d4a94A73d14Aa323dF6F8"
openai.api_key = open_ai_key
openai.api_base = "https://openkey.cloud/v1" # 换成代理，一定要加v1

# g = 
def chat_paper(abstract):
    sentence = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=[
                                      {"role": "user", "content": "使用一句中文总结下文: "+abstract}
                                    ],
                                    # 流式输出
                                    stream = False)
    return sentence["choices"][0]["message"]["content"]

