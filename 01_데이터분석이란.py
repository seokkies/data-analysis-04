# ============================================
# 01 단원. 데이터 분석이란 - "이걸 왜 배우나" 부터
# ============================================

import csv  # CSV 파일을 줄 칸으로 끊어 읽어 주는 파이썬 기본모듈
import os  # 파일 경로를 다루는 팡이썬 기본 모듈


def dp(name):
    """
    실행 위치가 어디든 data 폴더를 찾아주는 작은 도우미 함수
    "data/17_열처리.csv" 지금 있는 폴더 아래의 data를 뜻함.
    그래서 터미널이 어느 폴더에 서 있느냐에 따라 같은 코드가 도ㅚ기도 하고
    FileNotFoundError 가 나기도 합니다.
    폴더 배치 data`analysis-4/data 밑에 있음
    """

    here = os.path.dirname(os.path.abspath(__file__))
    for c in (
        os.path.join("data", name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):
        if os.path.exists(c):
            return c
    return os.path.join("data", name)


LOT = dp("17_열처리.csv")  # 데이터
PROC = dp("17_열처리_공정.csv")  # 공백있는 데이터
WIDE = dp("20_cmapss_fd001_sample.csv")  # 열 수만 세는 용도

# ============================================
# 0. 오늘 게속 만날 파이썬 표현 7가지 미리보기
# ============================================
print("=" * 60)
print("[0] 파이썬 표현 미리보기")

x = 859.5378  # 뒤에 나올 온도 평균
print(
    f" 1) {x:.2f} <- .2f 소수 둘째자리 | {x:10.1f} <- 10칸 폭, 첫째자리 반올림"
    f"| {44:>} <- 정수 5칸 오른쪽 | {0.00455:.1%} <- 0.0455를 퍼센트로"
)

# {x:.2f} -> 소수 둘째자리 까지만 보여달라 859.5318... -> 859.53
# {x:1-.1f} -> 10칸을 잡고 그 안에서 첫째 자리까지 모자란 칸은 왼쪽이 공백으로
# 표의 세로 줄을 맞추려고 쓰는 손잡이

#
# {44:>5d} -> d는 정수, 5는 칸 폭, > 는 그 칸에서 오른쪽에 붙이라는 뜻
# {0.0455:.1%} -> 퍼센트로 보여달라 -> 4.5%

with open(LOT, encoding="utf-8-sig") as f:
    r = csv.reader(f)
    header = next(r)  # 첫 줄은 열 이름
    rows = list(r)  # 나머지가 데이터

temps = [float(row[2]) for row in rows]  # 3번째 칸(온도)을 숫자로 바꿔 모음
print(" 2) 리스트 컴프리헨션:", temps[:5], "...총", len(temps), "개")
print(" 3) 조건을 붙이면:", [t for t in temps if t > 862])

pairs = [("온도", 1.39), ("OP값", 13.75), ("CP값", 0.01)]

print(
    " 4) 흔들림 큰 순:", sorted(pairs, key=lambda t: -t[1])
)  # t는 ("이름", 값) 한 쌍 // sorted가 오름차순이라 -1로 내림차순 변환

print(" 5) 삼항 연산자:", "넓다" if max(temps) - min(temps) > 10 else "좁다")

print(
    " 6) 슬라이싱: temps[:3] =",
    temps[:3],
    "| temps[-3:] =",
    temps[-3:],
    "| temps[::-1][:3] =",
    temps[::-1][:3],
)

kinds = {}  # 딕셔너리 개수 세기
for row in rows:
    kinds[row[1]] = kinds.get(row[1], 0) + 1
print(
    " 7) 딕셔너리로 세기:",
    kinds,
    "| set 으로 종류만",
    sorted(set(row[5] for row in rows)),
)

# ============================================
# 1. 왜 데이터 분석 하냐 - 설비가 멈추면 손해를 본다
# ============================================
print("=" * 60)
print("[1] 설비 관리 방식이 바뀌어 온 순서")
print("1. 사후보전")
print("2. 예방보전")
print("3. 예지보전")  # 스마트 팩토리의 방식

# 1) 사후보전 - 비용은 적지만 손실이 큼, 대비하기 어려움
# 2) 예방보전 - 정상부품 낭비 위험
# 3) 예지보전 = 센서 및 데이터 필요, 분석가 필요 -> 고장의 징조를 숫자로 파악

# ============================================
# 2. 파일 열어 데이터 확인
# ============================================
# csv 읽어 확인

print("=" * 60)
print("[2] 파일 첫 줄을 그냥 읽으면")
with open(LOT, encoding="utf-8-sig") as f:
    print("  ", repr(f.readline().strip()))  # repr() 로 감싸야 보임. print로 못봄

# f.readline() 파일에서 첫 줄 하나를 글자로 읽어오고 .strip()으로 그 글자의 앞 뒤에 붙은 공백과 줄바꿈을 제거
print("열 이름:", header)
print("행 수:", len(rows), "/ 열수 :", len(header))
print("첫 줄:", rows[0])

# 상태가 정상이 아닌 줄 확인
print()
print("[2-1] 상태가 정상이 아닌 줄")
for row in rows:
    if row[5] != "정상":
        print(" ", row)

# ============================================
# 3. 예측 목표 설정
# ============================================
# 목표가 정해져야 큰 그림을 그릴 수 있음
# 무엇을 물어보는지 // 정답의 생김새 // 문제의 이름
# 고장이 날것인가  // 예 아니오 // 분류
# 불량예측 // 불량 양품 // 분류
# 강도가 얼마일까 // 숫자 // 회귀(예측)
# 평소랑 다른가 // 정답없음 // 이상 탐지

# 판단 기준
# 정답이 범주형이면 분류
# 정답이 연속형이면 회귀(예측)
# 정답이 없으면 이상치 탐지

# (label)라벨이 비정상 일 경우 평가데이터를 의심해야하는 경우도 존재한다.
print("=" * 60)
print("[3] 같은 파일, 다른 문제")
print("분류 - 정답 칸을 '상태' 로 두면:", sorted(set(row[5] for row in rows)))
print(
    "회귀 - 정답 칸을 '온도' 로 두면:",
    min(temps),
    "~",
    max(temps),
    "사이의 연속된 숫자",
)
print("이상치 탐지 - 정답 칸을 안쓰면 : '평소와 다른 줄' 을 숫자만으로 찾습니다.")

# ============================================
# 4. 세 가지의 데이터
# ============================================

# 1) 센서 시계열 데이터
#    온도, 압력, 진동, 전류를 주기적으로 기록한 데이터(파일에서는 온도, OP, CP)
#    시간 순서가 의미를 가짐 -> 데이터가 섞이면 추세를 파악할 수 없음

# 2) 공정 조건 데이터
#    공정에 대한 설정값(파일에서는 로트 A/B/C)
#    해당 데이터로 여러가지 조건을 비교해 상태 파악 가능

# 3) 품질 측정 데이터
#    정답 데이터 -> 실무에서 데이터가 부족한 경우가 많음

print("=" * 60)
print("[4] 열 이름과 역할, 값의 종류 수")
roles = {
    "측정시각": "센서 시계열(시간축)",
    "배치": "공정조건",
    "온도": "센서 시계열",
    "OP값": "센서 시계열",
    "CP값": "센서 시계열",
    "상태": "품질 라벨 상태",
}
for i in range(len(header)):
    kinds = set(row[i] for row in rows)
    print(f"{header[i]:<6} 종류 {len(kinds):>3}가지 {roles[header[i]]}")

# ============================================
# 5. 데이터 눈으로 확인하기
# ============================================

# 온도 확인
import numpy as np

print("=" * 60)
print("[5] 온도 44개 전부")
print(temps)
top = max(temps)
low = min(temps)
span = top - low
avg = np.mean(temps)
print()
print(" [5-1] 세 숫자로 44개 요약")
print("합계:", round(sum(temps), 1), " / 개수:", len(temps))
print("평균:", avg)
print("평균(둘째 자리까지):", round(avg, 2))
print("최대:", top, "최소:", low, "범위:", span)

gaps = [abs(t - avg) for t in temps]
spread = sum(gaps) / len(gaps)

print()
print(" [5-2] 흩어진 정도")
print(" 평균에서 떨어진 거리 중 가장 먼 것:", round(max(gaps), 2))
print(" 평균에서 떨어진 거리의 평균:", round(spread, 2))

# ============================================
# 6. 배치별 비교
# ============================================


def stat(values):
    """
    숫자 리스트를 받아 개수, 평균, 최대, 최소, 범위, 흔들림을 딕셔너리로 반환하는 함수
    """
    cnt = len(values)
    mean = sum(values) / len(values)
    maxi = max(values)
    mini = min(values)
    boundary = maxi - mini
    mad = sum(abs(v - mean) for v in values) / len(values)

    return {
        "개수": cnt,
        "평균": mean,
        "최대": maxi,
        "최소": mini,
        "범위": boundary,
        "흔들림": mad,
    }


print("=" * 60)
print("[6] 배치별 온도 확인")
lots = ("로트A", "로트B", "로트C")
for lot in lots:
    picked = []
    for row in rows:
        if row[1] == lot:
            picked.append(row)

    lot_temps = []
    for row in picked:
        lot_temps.append(float(row[2]))

    s = stat(lot_temps)
    print(lot, s)
print("전체", stat(temps))
print()
print(" [6-2] 숫자 열의 흔들림 정도")
for name, idx in (("온도", 2), ("OP값", 3), ("CP값", 4)):
    print(name, "흔들림", stat([float(row[idx]) for row in rows])["흔들림"])


# ============================================
# 7. 라벨없이 이상치 탑지
# ============================================

print("=" * 60)
print("[7] 라벨을 보지 않고 찾아낸 수상한 줄")
for k in (2, 3):
    far = [row for row in rows if abs(float(row[2]) - avg) > k * spread]
    print(f"흔들림 {k}배 초과: {len(far)}건")

    for row in far:
        print(
            f"{row[1]} {row[0]} 온도 {row[2]:>6} "
            f"평균과 차이 {round(float(row[2]) -avg, 2):>6} 상태= {row[5]}"
        )
