from modules.시각화.sub.visualization_function_sub1 import visualization_function_sub1
from modules.시각화.sub.visualization_function_sub2 import visualization_function_sub2
from modules.시각화.sub.visualization_function_sub3 import visualization_function_sub3
from modules.시각화.sub.visualization_function_sub4 import visualization_function_sub4

def run_visualization(sub_menu):
    if sub_menu == "📈주식 현재가":
        visualization_function_sub1()  # 첫 번째 시각화 함수 호출
    
    elif sub_menu == "🌍글로벌 주식차트":
        visualization_function_sub2()  # 두 번째 시각화 함수 호출
    
    elif sub_menu == "💲주요 주가 지수":
        visualization_function_sub3()  # 세 번째 시각화 함수 호출

    elif sub_menu == "📊시가 총액/주식 거래량":
        visualization_function_sub4()  # 세 번째 시각화 함수 호출    



        
