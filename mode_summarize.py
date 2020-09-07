from gensim.summarization.summarizer import summarize

# 요약 : https://anpigon.github.io/blog/dclick/@anpigon/-textrank-summariser-1540351206980/

fileIn = open('output.txt', 'r', encoding='utf-8')
data = fileIn.read()
print(summarize(data, word_count=50))
fileIn.close()