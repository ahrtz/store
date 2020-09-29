from gensim.summarization.summarizer import summarize
from lexrankr import LexRank
from konlpy.tag import Twitter
from collections import Counter
from wordcloud import WordCloud
from mode_pdfconvert import isEnglishOrKorean

def summarize_function(result):
    # 문장 요약 : https://anpigon.github.io/blog/dclick/@anpigon/-textrank-summariser-1540351206980/
    return summarize(result, word_count=50)

def lexlank_function(result):
    # 참조 : https://wikidocs.net/72820
    # LexRank : https://github.com/theeluwin/lexrankr
    try:
        lexrank = LexRank()
        lexrank.summarize(result)
        
        summarize_data = []
        print("요약 진행중!")
        summaries = lexrank.probe(10)
        for i, summary in enumerate(summaries):
            summarize_data.append(summary)

        return summarize_data
    except:
        print("요약 내용이 부족합니다.")
        return []

def keywords_function(result):
    # 키워드 추출 : https://dalulu.tistory.com/108
    try:
        nlpy = Twitter()
        nouns = nlpy.nouns(result)
        count = Counter(nouns)

        tag_count = []
        tags = []

        for n, c in count.most_common(200):
            dics = {'tag': n, 'count': c}
            if len(dics['tag']) >= 2 and len(tags) <= 49:
                tag_count.append(dics)
                tags.append((dics['tag'], dics['count']))
        
        return tags
    except:
        return []

def visualize_function(summarize_tags):
    try:
        # 사이트 : https://liveyourit.tistory.com/58
        wc = WordCloud(font_path='C:\\Windows\\Fonts\\NanumGothicBold.ttf', \
            background_color="white", \
            width=1000, \
            height=1000, \
            max_words=100, \
            max_font_size=300)

        wc.generate_from_frequencies(dict(summarize_tags))
        wc.to_file('images/wordcloud.png')
    except:
        pass