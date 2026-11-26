import csv
import os
import numpy as np
import pandas as pd


def dp(name):
    """
    실행 위치가 어디든 data 폴더를 찾아주는 작은 도우미 함수
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


MCT = dp("10_mct_tool.csv")

# ============================================
# 0. 리스트는 곱셈이 불가능한 상황
# ============================================

print("=" * 60)
print(" [0] 리스트로 묶음 계산")
temps = [30, 30, 31, 29]
temps2 = [5, 6, 7, 8]
doubled = []

for t in temps:
    doubled.append(t * 2)
print(doubled)
print(temps * 2)

print(" [0-1] 배열로 묶음 계산")
arr = np.array(temps)
arr2 = np.array(temps2)
print("배열", arr)
print("arr * 2", arr * 2)
print("arr + 5", arr + 5)
print("화씨로 바꾸기", arr * 1.8 + 32)
print("배열 곱 확인", arr * arr2)


# ============================================
# 1. 리스트와 배열의 차이
# ============================================
print("=" * 60)
print(" [1] 리스트와 배열은 무엇이 다른가")
print("type(temps): ", type(temps).__name__)
print("type(arr): ", type(arr).__name__)
print("arr.dtype: ", arr.dtype)

box = [1, 2.5, "삼십"]
print("리스트에 섞어 담기:", box, "/ 값의 자료형:", {type(v).__name__ for v in box})

mixed = np.array([1, 2, 3.5])
print("배열에 정수와 소수를 섞으면: ", mixed, "/ dtype", mixed.dtype)

# ============================================
# 2. 배열 만들기
# ============================================
# np.arange(시작, 끝, 간격) #끝 값 안들어감 - 측정, 순번, 줄번호 등에 쓰임
# np.linespace(시작, 끝, 간격) #끝 값 포함 - 그래프 가로축 설정할때
# np.zeros(개수) #전부 0
# np.ones(개수) #전부 1
# np.full(개수, 값) # 전부 값으로

print("=" * 60)
print("[2] 규칙적인 배열을 한 줄로 만들기")
print("    np.arange(5)           :", np.arange(5))
print("    np.arange(0, 10, 2)    :", np.arange(0, 10, 2))
print("    np.arange(0, 1, 0.3)   :", np.arange(0, 1, 0.2))
print("    np.linspace(0, 1, 5)   :", np.linspace(0, 1, 5))
print("    np.linspace(0, 100, 5) :", np.linspace(0, 99, 5))
print("    np.zeros(3)            :", np.zeros(3))
print("    np.ones(3)             :", np.ones(3))
print("    np.full(3, 7)          :", np.full(3, 7))

print()
print("[2-1] 끝값이 포함되나")
print("    np.arange(0, 12, 3)   :", np.arange(0, 12, 3), "<- 12 가 없습니다")
print("    np.linspace(0, 12, 5) :", np.linspace(0, 12, 5), "<- 12 가 있습니다")
print("    개수:", len(np.arange(0, 12, 3)), "개 /", len(np.linspace(0, 12, 5)), "개")
print("    dtype:", np.arange(0, 12, 3).dtype, "/", np.linspace(0, 12, 5).dtype)

# ============================================
# 3. dtype - 배열 하나에 하나의 자료형
# ============================================

print("=" * 60)
print("[3] 배열 하나에는 한 가지 자료형만 들어갑니다")
ints = np.array([1, 2, 3])
print("    ints        :", ints, "/ dtype", ints.dtype)
ints[0] = 2.7  # 정수 배열의 첫 칸에 소수를 넣어 봅니다
print("    ints[0] = 2.7 한 뒤:", ints, "<- 2.7 이 2 가 됐습니다")
print("    ints.dtype  :", ints.dtype, "<- 정수 배열은 끝까지 정수입니다")

flo = np.array([1.0, 2.0, 3.0])  # 같은 일을 실수 배열에 해 봅니다
flo[0] = 2.7
print("    실수 배열에 같은 일:", flo, "<- 이쪽은 2.7 이 그대로 들어갑니다")

print()
print("[3-1] 나눗셈은 자료형을 바꿉니다")
odd = np.array([7, 8])
print("    np.array([7, 8])     :", odd, "/ dtype", odd.dtype)
print("    np.array([7, 8]) / 2 :", odd / 2, "/ dtype", (odd / 2).dtype)

# ============================================
# 4. asdtype - 자료형 변경
# ============================================

print("=" * 60)
print("[4] astype - 자료형을 바꾼 새 배열을 받습니다")
raw = np.array([1.7, -1.7, 2.3, 3.9])
print("    원본          :", raw, "/ dtype", raw.dtype)
print(
    "    astype(int)   :", raw.astype(int), "<- 1.7 이 2 가 아니라 1 입니다"
)  # 소수점 버림
print("    np.round      :", np.round(raw), "<- 반올림은 이쪽")  # 반올림
print(
    "    np.floor      :", np.floor(raw), "<- 내림은 또 다릅니다. -1.7 을 보세요"
)  # 내림
print("    원본은 그대로 :", raw, "<- astype 은 원본을 바꾸지 않습니다")

# ============================================
# 5. 배열 정보 확인 shape ndim size attribute
# ============================================

print("=" * 60)
print("[5] 배열에게 물어보는 네 가지")
table = np.array(
    [[30, 15.44, 4603], [30, 18.69, 4603]]
)  # 데이터 파일 앞 두 줄에서 세 칸만 떼 온 것입니다
print("    table")
print(table)
print("    table.shape :", table.shape, "<- (행, 열)")
print("    table.ndim  :", table.ndim, "<- 몇 차원인가")
print("    table.size  :", table.size, "<- 값이 모두 몇 개인가")
print("    table.dtype :", table.dtype, "<- 어떤 자료형인가")
print(
    "    검산:",
    table.shape[0],
    "x",
    table.shape[1],
    "=",
    table.shape[0] * table.shape[1],
)

print()
print("[5-1] 괄호를 붙이면")
try:
    table.shape()  # 속성에 괄호를 붙이면 터집니다
except TypeError as e:
    print("    table.shape() :", type(e).__name__, "-", e)


# =====================================================================
# 6. 모양 바꾸기 - reshape · flatten (값은 그대로, 모양만)
# =====================================================================
# 같은 12개 숫자를 한 줄로 늘어놓을 수도 있고, 3줄 4칸 표로 접을 수도 있습니다.
# 값은 그대로고 보는 모양만 바뀝니다. 그게 reshape입니다.
print("=" * 60)
print("[6] 모양 바꾸기 - 값은 그대로, 모양만")
seq = np.arange(12)
print("    seq                  :", seq)
print("    seq.reshape(3, 4)")
print(seq.reshape(3, 4))
print(
    "    seq.reshape(-1, 2).shape :", seq.reshape(-1, 2).shape, "<- -1 은 '알아서 계산'"
)
print("    reshape(3, 4).flatten()  :", seq.reshape(3, 4).flatten())
print("    원본 seq             :", seq, "<- reshape 도 원본을 바꾸지 않습니다")

print()
print("[6-1] 개수가 안 맞으면")
try:
    seq.reshape(5, 3)  # 12개를 15칸에 넣으라는 말이 됩니다
except ValueError as e:
    print("    seq.reshape(5, 3) :", type(e).__name__, "-", e)
print("    12 는 3x4, 2x6, 1x12 로는 접히고 5x3 = 15 로는 안 접힙니다")

print("=" * 60)
print("[7] CSV 파일을 배열로 읽기")
full = np.loadtxt(MCT, delimiter=",", skiprows=1, encoding="utf-8-sig")
print("    shape:", full.shape, "/ dtype:", full.dtype)
print("    앞 2줄")
print(full[:2])

# 위 결과가 눈에 안 들어옵니다. 보기 설정을 한 줄 바꿉니다.
print()
print("[7-1] 같은 배열인데 보기가 달라집니다")
np.set_printoptions(suppress=True)  # 지수 표기를 끄는 설정. 값은 안 바뀝니다
print(full[:2])

print()
print("[7-2] 열 이름은 따로 읽습니다")
with open(MCT, encoding="utf-8-sig") as f:
    head = next(csv.reader(f))  # 첫 줄만 꺼냅니다. 8단원에서 한 그 방법

print("    열 이름:", head)
print(
    "    공구번호 종류:",
    np.unique(full[:, 0]),
    "->",
    len(np.unique(full[:, 0])),
    "가지",
)

mct = np.loadtxt(
    MCT, delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5), encoding="utf-8-sig"
)
cols = head[1:]  # 열 이름도 공구번호를 뺀 5개로 맞춥니다
print("    공구번호를 뺀 배열:", mct.shape, "/ 열 이름", cols)
print("    앞 3줄")
print(mct[:3])

# 빈 칸이 있는 파일은 loadtxt 로 못 읽습니다. 지금 확인해 둡니다.
print()
print("[7-3] 빈 칸이 섞여 있으면")
sample = ["1,2,3", "4,,6"]  # 파일 대신 글자 두 줄로 흉내를 냅니다
# ★ 위 sample 이 파일 이름이 아니라 글자 두 줄인 게 눈에 걸리실 겁니다.
#   loadtxt 는 파일을 받으면 한 줄씩 꺼내 읽습니다. 그래서 '한 줄씩 꺼낼 수 있는 것'
#   이면 파일이 아니어도 받아 줍니다. 리스트도 한 줄씩 꺼낼 수 있으니 되는 거예요.
#   빈 칸이 있는 CSV 를 따로 만들지 않으려고 두 줄로 대신한 겁니다.
#   "4,,6" 의 쉼표 두 개가 붙어 있는 데를 보세요. 그 사이가 빈 칸입니다.
try:
    np.loadtxt(sample, delimiter=",")
except ValueError as e:
    print("    loadtxt    :", type(e).__name__, "-", e)
print("    genfromtxt :")
print(np.genfromtxt(sample, delimiter=","))


# ====================================
# 실습 1 - 전류 40개를 배열로 다루기
# ====================================
# [문제]
# 0번 ~ 7번에서 배운 것만 씁니다. 통계는 아직 안 씁니다.
#
# 1 - np.arrange 로 측정 순번 0~39를 만드세요. 앞 5개와 뒤 3개, shape, dtype을 찍으세요.
a = np.arange(1, 40)
print(" 앞 5개", a[:5], "뒤 3개", a[-3:], "shape", a.shape, "dtype", a.dtype)
# 2 - 10_mct_tool.csv에서 전류 열(3번 열)만 배열로 읽어 앞 5개를 찍으세요.
arr = np.array(mct[:, 3])
print("배열 앞 5개", arr[:5])
# 3 - 그 배열의 shape, ndim, size, dtype을 한 줄에 찍으세요.
print(f"shape: {arr.shape}, ndim: {arr.ndim}, size: {arr.size}, dtype: {arr.dtype}")
# 4 - 전류 40개를 8줄 5칸으로 접고, flatten 해서 원본과 같은지 확인하세요.
print(arr.reshape(8, 5).flatten())
# 5 - 7줄 6칸으로 접어 보고 어떤 오류가 나는지 확인하세요.
try:
    arr.reshape(7, 6)
except Exception as e:
    print(type(e).__name__)
    print(e)

# ====================================
# 8. 필요한 칸만 꺼내기 - 인덱싱 슬라이싱
# ====================================
# (40, 5) 배열에서 전류 한 열만, 또는 첫 줄만 꺼내고 싶습니다.
# 리스트에서 쓰던 대괄호를 그대로 씁니다. 다만 쉼표로 두 방향을 같이 줄 수 있습니다.
#
# 1차원 배열 arr[번호]   한 값
#          arr[시작:끝] 구간.  끝 번호는 안 들어갑니다.
#
# 2차원 배열 arr[행,열] 한 값
#          arr[행] 그 줄 전체
#          arr[:,열]  그 열 전체  <- 앞의 콜론이 "모든 행" 입니다.
print("=" * 60)
print("[8] 필요한 칸만 꺼내기")
cur = mct[:, 2]  # 전류 열 전체. 열 번호 2 는 cols 의 세 번째
print("    mct[0, 2]     :", mct[0, 2], "<- 0번 줄 2번 열 = 첫 줄 전류")
print("    mct[0]        :", mct[0], "<- 0번 줄 전체")
print("    mct[:, 2][:5] :", cur[:5], "<- 전류 열에서 앞 5개")
print("    mct[-1]       :", mct[-1], "<- 마지막 줄")
print("    cur[1:4]      :", cur[1:4], "<- 1번부터 3번까지 (4번은 빠집니다)")
print("    cur[::10]     :", cur[::10], "<- 10칸씩 건너뛰며")
print("    mct[:, 1:3][:3]")
print(mct[:, 1:3][:3])

print()
print("[8-1] 번호를 넘기면")
try:
    mct[40, 0]  # 줄은 0~39 까지입니다
except IndexError as e:
    print("    mct[40, 0] :", type(e).__name__, "-", e)
try:
    mct[0, 5]  # 열은 0~4 까지입니다
except IndexError as e:
    print("    mct[0, 5]  :", type(e).__name__, "-", e)
print("    mct[38:50].shape :", mct[38:50].shape, "<- 슬라이싱은 넘겨도 조용합니다")

# 여기서 나머지 열도 이름을 붙여 둡니다. 뒤에서 계속 씁니다.
cyc = mct[:, 0]  # 사이클타임
tmp = mct[:, 1]  # 온도
rpm = mct[:, 3]  # 회전수
tq = mct[:, 4]  # 토크


# ===========================================
# 9. 브로드캐스팅 - 짝이 안 맞는 계산을 늘려서 맞춥니다.
# ===========================================
# 0번에서 arr + 5 가 됐습니다. 그게 왜 되는지 이제 이름을 붙입니다.
#
# 브로드캐스팅 = 모양이 다른 것끼리 계산할 때
# NumPy가 작은 쪽을 늘려서 짝을 맞춰 주는 것.
# 방송처럼 "전체에 퍼뜨린다"는 뜻입니다.
# arr + 5 는 40개로 늘려서 같은 자리끼리 더한 것과 같습니다.
# * 실제로 5를 40개 복사해 메모리에 늘어놓는 건 아닙니다. 늘린 것처럼
# 계산만 합니다. 그래서 값이 400만 개여도 메모리가 두 배로 안 늘어납니다.
print("=" * 60)
print("[9] 브로드캐스팅 - 짝이 안 맞는 계산을 늘려서 맞춥니다")
three = np.array([70, 72, 71])
print("    three             :", three)
print("    three + 5         :", three + 5, "<- 5 가 세 개로 늘어났습니다")
print("    three + [1, 2, 3] :", three + np.array([1, 2, 3]), "<- 같은 자리끼리")
try:
    three + np.array([1, 2])  # 3개와 2개는 늘릴 방법이 없습니다
except ValueError as e:
    print("    three + [1, 2]    :", type(e).__name__, "-", e)
# 브로드캐스팅으로 실제로 하는 일 두 가지를 해 봅니다. 둘 다 현장에서 매일 씁니다.
# cur.min  cur.max cur.mean() cur.std() 가 나옵니다.
# 지금은 2를 넘는 것만 골라 찍었다로 읽으면 됩니다. 몰라도 안 막힘.
print()
print("[9-1] 전류를 0~1 사이로 옮기기 (최소-최대 정규화)")
scaled = (cur - cur.min()) / (cur.max() - cur.min())
print("    전류 앞 5개  :", cur[:5])
print("    옮긴 값 앞 5개:", np.round(scaled[:5], 2))
print("    최소", scaled.min(), "/ 최대", scaled.max(), "/ 개수", scaled.size)

print()
print("[9-2] 평균 0, 표준편차 1 로 옮기기 (표준화)")
z = (cur - cur.mean()) / cur.std()
print("    앞 8개:", np.round(z[:8], 2))
print("    2 를 넘는 값:", np.round(z[z > 2], 2), "/", (z > 2).sum(), "건")

# ==================================
# 10. 조건으로 고르기 - 불리언 인덱싱
# ==================================
# 01 단원에서는 이렇게 했습니다 - [t for t in temps if t > 862]
# NumPy 는 이렇게 씁니다 - cur[cur > 50]
# 같은 일인데 생김새가 아주 다릅니다. 둘로 끊어서 봅시다.
# 불리언 인덱싱 = 참/거짓 배열을 대괄호에 넣어 "참인 자리만" 꺼내는 것
# 두 단계로 돌아갑니다
# 1) cur > 50 이 먼저 계산돼서 [False False False True ...]가 만들어짐
# 2) cur[그 배열] 이 True 자리의 값만 모아 새 배열을 만듭니다.
print("=" * 60)
print("[10] 조건으로 고르기")
print("    cur > 50 (앞 10개):", (cur > 50)[:10])
print("    cur[cur > 50]     :", cur[cur > 50])
print("    몇 건인가         :", (cur > 50).sum(), "건")
print("    몇 퍼센트인가     :", round((cur > 50).mean() * 100, 1), "%")
print("    몇 번째 줄인가    :", np.where(cur > 50)[0])
print("    np.where(조건,1,0):", np.where(cur > 50, 1, 0)[:10])

print()
print("[10-1] 조건 두 개를 겹칠 때")
print("    전류>50 그리고 토크>100:", ((cur > 50) & (tq > 100)).sum(), "건")
print("    전류>50 또는   토크>100:", ((cur > 50) | (tq > 100)).sum(), "건")
try:
    (cur > 50) and (tq > 100)  # and 는 배열에 못 씁니다
except ValueError as e:
    print("    and 로 쓰면:", type(e).__name__, "-", e)

# =====================================
# 11. 조건에 맞는 '줄'을 통째로 꺼내기
# =====================================
# 10번에서는 전류 값만 꺼냈습니다. 그런데 분석에서 정말 궁금한 건 이거예요
# "그 줄의 다른 칸은 어땠냐?"
# 전류가 튄 그 순간, 회전수는 어땠고 토크는 어땠는지.
# 참/거짓 배열을 2차원 배열의 대괄호에 그냥 넣으면 '줄' 이 뽑힙니다. 한 줄입니다.
print("=" * 60)
print("[11] 조건에 맞는 '줄' 을 통째로 꺼내기")
print("    열 이름:", cols)
print("    토크가 100 넘는 줄")
print(mct[tq > 100])

# 01단원에서 로트A/B/C 로 나눠 재던 걸 여기서도 하고 싶습니다.
# 그런데 공구번호가 한 종류뿐이라(7-2) 그걸로는 못 나눕니다. 회전수를 보니 길이 있었습니다.
print()
print("[11-1] 회전수로 두 묶음을 나눠 재 봅니다")
usual = rpm == 4603  # 가장 많이 나온 회전수. 아래 검산으로 확인합니다
print("    회전수 4603 인 줄:", usual.sum(), "줄 / 아닌 줄:", (~usual).sum(), "줄")
print(
    "    4603 묶음  : 전류 평균",
    round(cur[usual].mean(), 2),
    "/ 토크 평균",
    round(tq[usual].mean(), 2),
)
print(
    "    나머지 묶음: 전류 평균",
    round(cur[~usual].mean(), 2),
    "/ 토크 평균",
    round(tq[~usual].mean(), 2),
)
print(
    "    검산:",
    usual.sum(),
    "+",
    (~usual).sum(),
    "=",
    usual.sum() + (~usual).sum(),
    "/ 전체",
    len(mct),
)

# ==============================================
# 12. 통계 한 번에 - 그리고 평균 10.7, 중앙값 2.0 함정 3,4
# ==============================================
# 01 단원에서는 평균을 이렇게 냈습니다 - sum(temps) / len(temps)
# 최대 최소는 max() min(), 흔들림은 for를 돌려 직접 만들었습니다.
# NumPy 는 전부 매서드 한 개씩입니다.
#   cur.sum()      합계           cur.min()  최소
#   cur.mean()     평균           cur.max()  최대
#   cur.std()      표준편차       cur.var()  분산
#   np.median(cur) 중앙값  <- 이것만 앞에 np. 가 붙습니다.
#   왜 median 만 생김새가 다른가 -> 외워야함.
# 중앙값 -> 값듫을 줄 세웠을 때 가운대 있는 값.
#          평균과 다릅니다. 아주 다릅니다.
# 표준편차(std)  = 값들이 평균에서 평균적으로 얼마나 떨어져 있나.
# 분산(var) = 표준편차에 제곱근을 씌우기 전의 값. 표준편차의 제곱.
print("=" * 60)
print("[12] 통계는 메서드 한 개씩입니다")
print("    전류 합계    :", round(cur.sum(), 2))
print("    전류 개수    :", cur.size)
print("    전류 평균    :", round(cur.mean(), 2))
print("    전류 중앙값  :", np.median(cur))
print("    전류 최소/최대:", cur.min(), "/", cur.max())
print("    전류 표준편차:", round(cur.std(), 2))

# 다섯 열을 한 번에 재 봅니다. for 는 '열을 돌기' 위한 것이고 계산은 전부 NumPy 가 합니다.
print()
print("[12-1] 다섯 열을 한 줄씩 재 봅니다")
for i in range(len(cols)):
    c = mct[:, i]
    print(
        f"    {cols[i]:<6} 평균 {c.mean():>9.2f}  중앙값 {np.median(c):>9.2f}"
        f"  표준편차 {c.std():>8.2f}  최소 {c.min():>8.2f}  최대 {c.max():>8.2f}"
    )

# 위 표에서 한 줄만 다시 봅니다. 오늘 세 번째 함정입니다.
print()
print("[12-2] 토크 한 줄만 다시 보세요")
print("    토크 평균:", round(tq.mean(), 2), "/ 중앙값:", np.median(tq))
print("    줄 세워서 작은 쪽 5개:", np.sort(tq)[:5], "/ 큰 쪽 5개:", np.sort(tq)[-5:])
print(
    "    평균보다 큰 줄:",
    (tq > tq.mean()).sum(),
    "건 / 작은 줄:",
    (tq < tq.mean()).sum(),
    "건",
)

# 네 번째 함정. 같은 데이터에서 표준편차가 두 개 나옵니다.
print()
print("[12-3] 표준편차는 두 가지가 있습니다")
print("    cur.std()       :", round(cur.std(), 4), "<- 분모가 40")
print("    cur.std(ddof=1) :", round(cur.std(ddof=1), 4), "<- 분모가 39")
print(
    "    cur.var()       :",
    round(cur.var(), 4),
    "/ var(ddof=1):",
    round(cur.var(ddof=1), 4),
)

# ======================================
# 13. axis - 어느 방향으로 재는가
# ======================================
#
# 축(axis) = 배열에서 세는 방향
# 2차원 배열에서는 두 방향뿐입니다
# axis=0 줄 방향(위에서 아래로) -> 결과가 '열별'로 나옵니다.
# axis=1 칸 방향(왼쪽에서 오른쪽으로) -> 결과가 '행별'로 나옵니다.
# axis는 '무엇을 기준으로'가 아니라 '무엇을 따라 훑어 없앨지'입니다.
# axis=0 을 주면 줄 방향이 없어지고 열만 남습니다. 그래서 '열별 평균'이 됩니다.
# (40,6)
print("=" * 60)
print("[13] axis - 어느 방향으로 재는가")
print("    mct.shape:", mct.shape, "<- 40줄 5열")
down = mct.mean(axis=0)  # 줄 방향으로 훑어 없앰 -> 열별 평균 5개
across = mct.mean(axis=1)  # 칸 방향으로 훑어 없앰 -> 행별 평균 40개
print("    mct.mean(axis=0) -> 값", len(down), "개")
for i in range(len(cols)):
    print(f"        {cols[i]:<6} {down[i]:>10.2f}")
print(
    "    mct.mean(axis=1) -> 값", len(across), "개 / 앞 3개:", np.round(across[:3], 2)
)
print(
    "    mct.mean()       ->", round(mct.mean(), 2), "<- 축을 안 주면 200개 전부의 평균"
)

# 바꿔 써 봅니다. 여기가 오늘의 함정입니다.
print()
print("[13-1] 바꿔 쓰면 어떻게 되나")
print("    열별 평균 첫 값(사이클타임):", round(down[0], 2))
print("    행별 평균 첫 값(첫 줄)     :", round(across[0], 2))
print("    첫 줄:", mct[0])
print("    손으로 검산:", round(mct[0].sum() / 5, 2), "<- 행별 평균 첫 값과 같습니다")

# =====================================================================
# 14. for 문 없이 - 01단원에서 for 로 하던 일을 다시
# =====================================================================
# 오늘의 마지막 섹션입니다. 01단원에서 한 일을 두 방법으로 나란히 해 봅니다.
# 숫자가 같은지, 코드가 얼마나 줄었는지 둘 다 보세요.
print("=" * 60)
print("[14] 01단원에서 for 로 하던 일")
with open(MCT, encoding="utf-8-sig") as f:  # 01단원 방식: csv 모듈로 읽기
    r = csv.reader(f)
    next(r)  # 열 이름 줄을 버립니다
    rows = list(r)

vals = []  # 1) 빈 리스트를 만들고
for row in rows:  # 2) for 로 돌면서
    vals.append(float(row[3]))  # 3) 전류 칸을 숫자로 바꿔 담습니다
avg = sum(vals) / len(vals)  # 4) 평균
gaps = []  # 5) 또 빈 리스트
for v in vals:  # 6) 또 for
    gaps.append(abs(v - avg))  # 7) 평균에서 떨어진 거리

print(
    "    순수 파이썬: 개수",
    len(vals),
    "/ 평균",
    round(avg, 2),
    "/ 최대",
    max(vals),
    "/ 최소",
    min(vals),
    "/ 흔들림",
    round(sum(gaps) / len(gaps), 2),
)

print()
print("[14-1] 같은 일을 NumPy 로")
print(
    "    NumPy      : 개수",
    cur.size,
    "/ 평균",
    round(cur.mean(), 2),
    "/ 최대",
    cur.max(),
    "/ 최소",
    cur.min(),
    "/ 흔들림",
    round(np.abs(cur - cur.mean()).mean(), 2),
)

print()
print("[14-2] 두 평균을 끝자리까지 비교하면")
print("    순수 파이썬:", avg)
print("    NumPy      :", cur.mean())
print()
# ======================================
# 실습 2 토크가 튀는 줄 확인
# ======================================
# [문제]
# 11번에서 "회전수가 떨어지고 전류가 올라간 순간에 토크가 튀었다"를 두 줄로 봤습니다.
# 이번엔 두 줄이 아니라 40줄 전체로 확인하세요. 그리고 축을 한 번 확인합니다.
#
# 1. 토크가 100 넘는 줄을 통째로 꺼내고 몇 건인지 세세요.
#                 0       1   2   3   4
# print(mct)  # 사이클타임,온도,전류,회전수,토크
tok = mct[:, 4]
mct_tok_100 = mct[np.where(tok > 100)]
print("토크가 100 넘는 줄", len(mct_tok_100))

# 2. 그 줄들의 회전수와 전류를 전체 평균과 나란히 찍으세요.
print(f"회전수: {mct_tok_100[:,3]} 전체 회전수 평균: {mct[:,3].mean()} ")
print(f"전류: {mct_tok_100[:,2]} 전체 전류 평균: {mct[:,2].mean()} ")

# 3. 회전수 4000 미만인 줄과 4000 이상인 줄의 토크 평균을 각각 내세요.
cyl = mct[:, 3]
mct_tok_4000_u = tok[cyl >= 4000]
mct_tok_4000_d = tok[cyl < 4000]
print(
    f"회전수 4000 미만 토크 평균:{mct_tok_4000_d.mean()}  // 4000 이상인 줄의 토크 평균: {mct_tok_4000_u.mean()}"
)

# 4. 열별 평균과 행별 평균의 '개수'를 찍어 어느 쪽이 열별인지 확인하세요.
cnt_row = mct.mean(axis=1)
cnt_col = mct.mean(axis=0)
print("열 평균:", len(cnt_col), "행 평균:", len(cnt_row))

# 5. 검산 두 줄 - 줄 수의 합, 그리고 토크 합계의 합.
print(f"{len(mct_tok_4000_d)} + {len(mct_tok_4000_u)} = 40")
print(f"{mct_tok_4000_d.sum()} + {mct_tok_4000_u.sum()} = 428.0")
