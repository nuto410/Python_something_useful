import numpy as np
import matplotlib.pyplot as plt

# 創建一個5x5的相關矩陣（這裡使用隨機數填充）
correlation_matrix = np.random.rand(5, 5)

# 設定問題標籤
questions = ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5']

# 繪製熱力圖
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation')
plt.xticks(np.arange(len(questions)), questions, rotation=45)
plt.yticks(np.arange(len(questions)), questions)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()
