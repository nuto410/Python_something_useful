import re

def preprocess_string(input_string):
    # 去除除文字外的標點符號等
    processed_string = re.sub(r'[^\w\s]', '', input_string)
    return processed_string.lower()  # 將字串轉為小寫

def compare_strings(reference_string, user_input):
    # 處理參考字串和使用者輸入
    processed_reference = preprocess_string(reference_string)
    processed_user_input = preprocess_string(user_input)

    # 計算差異閾值
    similarity_threshold = len(processed_reference) * 0.1
    
    # 比較兩個處理後的字串的差異
    differences = sum(c1 != c2 for c1, c2 in zip(processed_reference, processed_user_input))
    
    # 判斷是否相似
    if differences <= similarity_threshold:
        return True
    else:
        return False

# 設定參考字串
reference = "有些科別顯示預約額滿，是否有其他方式可以掛號?"

# 接受使用者輸入
user_input = input("請輸入一個字串：")

# 比較並顯示結果
if compare_strings(reference, user_input):
    print("相似度高，判定為相同。")
else:
    print("相似度不高，判定為不同。")
