import os
import re

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # 處理 print 陳述式
    modified_content = re.sub(r'(?<!#)(print\s+)([^(\n]*)(\n|$)', r'\1(\2)\3', content, flags=re.MULTILINE)
    if modified_content != content:
        with open(file_path, 'w') as f:
            f.write(modified_content)
        print(f"已處理檔案: {file_path}")
    else:
        print(f"未執行處理: {file_path}")


def process_files_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_file(file_path)


if __name__ == '__main__':
    folder_path = input("請輸入包含子資料夾的目錄路徑: ")
    process_files_in_folder(folder_path)
