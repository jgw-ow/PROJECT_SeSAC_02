# 01. 프로젝트 개요

네이버 뉴스 데이터를 크롤링하여 **토픽 모델링(LDA)**을 수행하고, 다양한 주식 관련 데이터를 시각화하는 애플리케이션입니다. 위 서비스는 사용자가 뉴스 데이터를 분석하고, 실시간 주식 데이터를 직관적으로 시각화하여 쉽게 이해할 수 있도록 도와줍니다. 주요 기능은 다음과 같습니다:

- ## **네이버 뉴스 크롤링 및 LDA 기반 토픽 모델링**:  
  사용자가 선택한 뉴스 카테고리에서 최신 기사를 크롤링하여 LDA 모델을 통해 주요 토픽을 추출하고, 이를 **워드클라우드** 형태로 시각화합니다.
  
- ## **주식 데이터 시각화**:  
  실시간 주식 데이터를 바탕으로 다양한 시각화 차트를 제공합니다. 주식의 현재가, 글로벌 주식 차트, 주요 주가지수, 시가 총액 및 거래량을 직관적인 차트로 표현합니다.

# 02. 프로젝트 구조


```
📁PROJECT_SeSAC_02
│
├── 📄app.py                                          # 메인 애플리케이션 코드
├── 📄__init__.py                                     # 최상위 초기화 파일
│
├── 📁modules                                         # 모듈 관련 파일들이 있는 폴더
│   ├── 📁홈                                          # 홈 페이지 관련 모듈
│   │   ├── 📄display_home_01.py                      # 홈 페이지의 첫 번째 디스플레이 관련 코드
│   │   ├── 📄display_home_02.py                      # 홈 페이지의 두 번째 디스플레이 관련 코드
│   │   ├── 📄display_home_03.py                      # 홈 페이지의 세 번째 디스플레이 관련 코드
│   │   ├── 📄__init__.py                             # 홈 모듈 초기화 파일
│   │   └── 📁sub                                     # 서브 모듈
│   │       ├── 📄home_function_sub1.py               # 홈 관련 기능 1
│   │       ├── 📄home_function_sub2.py               # 홈 관련 기능 2
│   │       ├── 📄home_function_sub3.py               # 홈 관련 기능 3
│   │       ├── 📄home_function_sub4.py               # 홈 관련 기능 4
│   │       └── 📄__init__.py                         # 서브 모듈 초기화 파일
│   │
│   ├── 📁크롤링                                       # 웹 크롤링 관련 모듈
│   │   ├── 📄run_crawling.py                         # 크롤링 실행 관련 코드
│   │   ├── 📄__init__.py                             # 크롤링 모듈 초기화 파일
│   │   └── 📁sub                                     # 서브 모듈
│   │       ├── 📄crawling_function_sub1.py           # 크롤링 함수 1
│   │       ├── 📄crawling_function_sub2.py           # 크롤링 함수 2
│   │       └── 📄__init__.py                         # 서브 모듈 초기화 파일
│   │
│   └── 📁시각화                                       # 데이터 시각화 관련 모듈
│       ├── 📄run_visualization.py                    # 데이터 시각화 실행 관련 코드
│       ├── 📄__init__.py                             # 시각화 모듈 초기화 파일
│       └── 📁sub                                     # 서브 모듈
│           ├── 📄visualization_function_sub1.py      # 시각화 함수 1
│           ├── 📄visualization_function_sub2.py      # 시각화 함수 2
│           ├── 📄visualization_function_sub3.py      # 시각화 함수 3
│           ├── 📄visualization_function_sub4.py      # 시각화 함수 4
│           └── 📄__init__.py                         # 서브 모듈 초기화 파일
│
├── 📁datas                                           # 데이터 관련 파일들이 있는 폴더
│   ├── 📄stopwords.txt                               # 불용어(stop words) 목록 파일
│   ├── wordcloud_output.jpg                        # 생성된 워드클라우드 이미지 파일
│   └── 네이버로고.png                               # 네이버 로고 이미지 파일
│
├── 📄config.py                                       # 설정 관련 코드
└── requirements.txt                                # 필요한 패키지 목록 파일
```




# 03. 각 파일 및 폴더 설명

## `app.py`
메인 애플리케이션 코드입니다. **Streamlit**을 사용하여 웹 애플리케이션을 실행하며, 애플리케이션의 주요 페이지를 연결합니다. 사용자가 선택한 메뉴에 따라 해당 기능(크롤링, 시각화, 홈)을 실행합니다.

## `modules`
애플리케이션의 핵심 기능들을 포함하는 모듈들입니다. 홈, 크롤링, 시각화 기능이 각기 다른 서브 모듈로 분리되어 관리됩니다.

## `홈`
- **홈/display_home_01.py, 홈/display_home_02.py**:  
  첫 번째 페이지(display_home_01.py)와 두 번째 페이지(display_home_02.py)는 웹 페이지의 UI 요소들을 담당합니다. display_home_01.py에서는 간단한 텍스트와 타이틀을 표시하며, display_home_02.py는 사용자 인터페이스(UI)와 관련된 버튼 및 선택 항목을 제공합니다.

## `크롤링`
- **크롤링/run_crawling.py**:  
  사용자가 선택한 네이버 뉴스 카테고리에서 최신 기사를 크롤링하는 기능을 담당합니다. 크롤링된 뉴스 데이터를 전처리하여 LDA 모델을 통해 주요 토픽을 추출하고, 이를 시각화합니다.

## `시각화`
- **시각화/run_visualization.py**:  
  다양한 차트 시각화 기능을 포함하고 있습니다. 주식 시장 데이터를 사용하여 여러 가지 차트를 제공합니다. 사용자가 선택한 데이터에 따라 주식 현재가 차트, 글로벌 주식차트, 주요 주가지수, 시가 총액/주식 거래량 등의 차트를 시각화합니다.

## `datas`
애플리케이션에서 사용하는 데이터와 이미지 파일들이 위치한 폴더입니다.
- **stopwords.txt**: 뉴스 크롤링과 텍스트 분석을 위한 불용어 목록 파일입니다.
- **wordcloud_output.jpg**: LDA 토픽 모델링을 통해 생성된 워드클라우드 이미지입니다.
- **네이버로고.png**: 네이버 로고 이미지 파일입니다.

### `config.py`
애플리케이션의 설정 파일로, 환경 변수나 주요 파라미터를 관리합니다. 예를 들어, 크롤링 대상 URL, LDA 모델 파라미터, 시각화에 사용되는 데이터 등의 설정을 관리합니다.

### `requirements.txt`
애플리케이션에서 필요한 Python 패키지 목록을 정의합니다. `pip install -r requirements.txt` 명령어를 통해 필요한 모든 라이브러리를 설치할 수 있습니다.

# 04. 주요 기능

- ## **홈페이지**  
   애플리케이션의 첫 번째 화면을 구성합니다. 초기에는 Splash Screen이 표시됩니다. 이후, 프로젝트 소개 및 각 기능에 대한 간략한 설명이 제공됩니다.

- ## **네이버 뉴스 크롤링**  
   사용자가 선택한 뉴스 카테고리에서 최신 기사를 크롤링하고, LDA 모델을 통한 텍스트 분석으로 뉴스의 주요 토픽을 추출합니다. 결과는 **워드클라우드** 형태로 시각화됩니다.

- ## **주식 데이터 시각화**  
   실시간 주식 데이터를 바탕으로 다양한 차트 시각화를 제공합니다. 사용자는 다음과 같은 주식 관련 차트를 선택하여 직관적으로 분석할 수 있습니다:
   - **주식 현재가**: 막대차트 형태로 주식의 현재가를 시각화합니다.
   - **글로벌 주식 차트**: 글로벌 증시의 움직임을 라인차트로 시각화합니다.
   - **주요 주가지수**: 주요 주가지수의 변화를 시각화합니다.
   - **시가 총액/거래량**: 주식 시장의 시가 총액과 거래량을 파이차트로 표현하여 시장의 규모와 변화를 직관적으로 분석할 수 있도록 합니다.


