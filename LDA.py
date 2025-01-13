import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re
import os
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from wordcloud import WordCloud
import streamlit as st
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Streamlit에서 한글 깨짐 방지)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 불용어 파일 경로 (직접 경로 설정)
stopwords_path = "C:/Users/SJ/Downloads/stopwords.txt"  # 경로를 여기서 설정

# 카테고리와 그에 해당하는 sid 값 설정
category_sid_map = {
    "정치": "100",
    "경제": "101",
    "사회": "102",
    "생활/문화": "103",
    "IT/과학": "105",
    "세계": "104"
}

# 사용자 입력을 받아 sid 결정
category = st.selectbox("크롤링할 카테고리를 선택하세요", options=["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"])
sid = category_sid_map.get(category, "100")  # 기본값은 정치(100)으로 설정

# 기본 URL 및 헤더 설정
url = "https://news.naver.com/section/template/SECTION_ARTICLE_LIST"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
}

# 현재 시간을 'YYYYMMDDHHMMSS' 형식으로 변환하여 next 초기값으로 사용
current_time = datetime.now().strftime("%Y%m%d%H%M%S")

# 첫 페이지 파라미터 설정
params = {
    "sid": sid,
    "pageNo": "1",
    "next": current_time,
    "_": str(int(time.time())),
}

# 불용어 파일을 읽어들이는 함수 (경로를 직접 사용)
def load_stopwords(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stop_words = set(line.strip() for line in f)
        return stop_words
    except FileNotFoundError:
        st.warning(f"불용어 파일을 찾을 수 없습니다: {file_path}")
        return set()

# 텍스트 전처리 함수
def preprocess_text(text, stopwords):
    tokenizer = RegexpTokenizer(r'\w+')
    text = re.sub(r'\[.*?\]', '', text)  # 대괄호 내용 제거
    text = re.sub(r'\d+', '', text)  # 숫자 제거
    tokens = tokenizer.tokenize(text)  # 토큰화
    tokens = [word for word in tokens if word not in stopwords]  # 불용어 제거
    return tokens

# 뉴스 크롤링 함수
def fetch_page(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("a", attrs={"data-clk": True})
    article_urls = [article.get("href") for article in articles if article.get("href")]
    div_tag = soup.find("div", attrs={"data-cursor": True})
    next_cursor = div_tag.get("data-cursor", "").strip('"') if div_tag else None
    next_cursor = re.sub(r'[\\"]', '', next_cursor) if next_cursor else None
    article_urls = list(set(article_urls))
    return article_urls, next_cursor

def fetch_article_details(article_url):
    article_url = re.sub(r'[\\"]', '', article_url)
    if article_url.startswith("/"):
        article_url = "https://n.news.naver.com" + article_url
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_title = soup.select_one('h2#title_area').text.strip() if soup.select_one('h2#title_area') else '제목을 찾을 수 없습니다.'
    news_article = soup.select_one('div#newsct_article').text.strip() if soup.select_one('div#newsct_article') else '본문을 찾을 수 없습니다.'
    return news_title, news_article

# 크롤링을 통해 최대 50개 기사 가져오기
def crawl_news(max_articles=50):
    articles = []
    page_no = 1
    while len(articles) < max_articles:
        params["pageNo"] = str(page_no)
        html = fetch_page(url, headers, params)
        article_urls, next_cursor = parse_html(html)
        
        for article_url in article_urls:
            title, content = fetch_article_details(article_url)
            preprocessed_content = preprocess_text(content, stopwords)
            articles.append(" ".join(preprocessed_content))
            if len(articles) >= max_articles:
                break
        
        # 페이지를 넘길 때마다 page_no 증가
        page_no += 1
        
        # 만약 더 이상 기사가 없다면 종료
        if not article_urls:
            break

    return articles[:max_articles]  # 최대 max_articles 개수만 반환

# 워드클라우드 생성 함수
def generate_wordcloud(text_data):
    text = " ".join(text_data)
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", width=800, height=400, background_color="white", colormap="Blues").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

# 스트림릿 UI
stopwords = load_stopwords(stopwords_path)  # 불용어 로드
if stopwords:
    st.write("불용어 파일이 정상적으로 로드되었습니다.")
    
    articles = crawl_news()
    st.write(f"총 {len(articles)}개의 기사를 크롤링하였습니다.")
    
    # 워드클라우드 생성
    generate_wordcloud(articles)

else:
    st.warning("불용어 파일을 찾을 수 없습니다. 경로를 확인해 주세요.")
