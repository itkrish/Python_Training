import matplotlib.pyplot as plt
import numpy as np

# 日本語フォント設定（Windows環境）
# 日本語フォントを設定しないと文字化けする
plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo']

# 一次関数のテスト y = 2x + 1
x = np.linspace(-5, 5, 100)
y = 2 * x + 1

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = 2x + 1')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('一次関数のグラフ')
plt.legend()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()
