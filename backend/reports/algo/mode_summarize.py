from gensim.summarization.summarizer import summarize
from konlpy.tag import Twitter
from collections import Counter
from wordcloud import WordCloud

def summarize_function(result):
    # 문장 요약 : https://anpigon.github.io/blog/dclick/@anpigon/-textrank-summariser-1540351206980/
    return summarize(result)

def keywords_function(result):
    # 키워드 추출 : https://dalulu.tistory.com/108
    nlpy = Twitter()
    nouns = nlpy.nouns(result)
    count = Counter(nouns)

    tag_count = []
    tags = []

    for n, c in count.most_common(100):
        dics = {'tag': n, 'count': c}
        if len(dics['tag']) >= 2 and len(tags) <= 49:
            tag_count.append(dics)
            tags.append((dics['tag'], dics['count']))
    
    return tags

def visualize_function(summarize_tags):
    # 사이트 : https://liveyourit.tistory.com/58
    wc = WordCloud(font_path='C:\\Windows\\Fonts\\NanumGothicBold.ttf', \
        background_color="white", \
        width=1000, \
        height=1000, \
        max_words=100, \
        max_font_size=300)

    wc.generate_from_frequencies(dict(summarize_tags))
    wc.to_file('images/wordcloud.png')