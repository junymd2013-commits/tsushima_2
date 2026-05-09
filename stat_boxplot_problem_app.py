import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from matplotlib import font_manager
font_manager.fontManager.addfont("ipaexg.ttf")
plt.rcParams["font.family"] = "IPAexGothic"

st.title("箱ひげ図の問題自動生成（数学B）")

# データ生成
n = st.slider("データ数", 10, 50, 20)
mean = st.slider("平均値の中心", 40, 80, 60)
spread = st.slider("ばらつき（標準偏差）", 5, 20, 10)

data = np.random.normal(mean, spread, n).astype(int)

# 四分位数の計算
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
min_val = np.min(data)
max_val = np.max(data)

st.subheader("生成されたデータ")
st.write(sorted(data))

# 箱ひげ図の描画
fig, ax = plt.subplots(figsize=(6, 4))
ax.boxplot(data, vert=False)
ax.set_title("箱ひげ図（問題用）")
ax.set_xlabel("値")
st.pyplot(fig)

# 問題文の自動生成
st.subheader("問題文（授業でそのまま使える）")
st.write(f"""
次のデータについて、箱ひげ図を描きなさい。

データ：  
{sorted(data)}

（1）最小値、最大値を求めよ  
（2）第1四分位数 Q1、第3四分位数 Q3 を求めよ  
（3）中央値を求めよ  
（4）箱ひげ図を描け  
""")

# 解答
st.subheader("解答（教師用）")
st.write(f"""
最小値：{min_val}  
最大値：{max_val}  
Q1：{Q1:.1f}  
中央値：{Q2:.1f}  
Q3：{Q3:.1f}  
""")
