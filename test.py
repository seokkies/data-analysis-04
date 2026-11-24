# 빅분기 2유형 복습하기
import pandas as pd

# 데이터 불러오기
train_df = pd.read_csv(
    "https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_train.csv"
)
test_df = pd.read_csv(
    "https://raw.githubusercontent.com/YoungjinBD/data/main/exam/9_2_test.csv"
)

print(train_df.head()) #  ID  지역 등급   농업면적    연도  라벨 target -> 라벨
print(train_df.describe()) #1680 데이터, 결측치 없음
print(train_df.info()) # 지역, 등급 -> 범주형

#데이터 분리
