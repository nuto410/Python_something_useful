import time
import pyperclip
import keyboard  # 用于监视键盘输入

while True:
    # 获取剪贴板上的文本
    clipboard_text = pyperclip.paste()
    
    # 检查剪贴板是否有新的文本
    if clipboard_text:
        print("當前複製文字",clipboard_text)
        # 去除文本中的换行符，并将多行文本合并成一行
        cleaned_text = ' '.join(clipboard_text.splitlines())
        
        # 将处理后的文本重新放回剪贴板
        pyperclip.copy(cleaned_text)
    
    # 检查键盘输入是否为 "break"，如果是就停止程序
    if keyboard.is_pressed('pause'):
        break
    
    # 每次处理间隔一秒
    time.sleep(1)

# 程序运行结束
print("程序已停止。")
