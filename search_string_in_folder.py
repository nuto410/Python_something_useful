import os

def find_matching_files(folder_path, search_string):
    matching_files = []
    
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):  # 只处理.py文件
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r',encoding = 'utf-8') as f:
                    content = f.read()
                    if search_string in content:
                        matching_files.append(file_path)
    
    return matching_files

if __name__ == "__main__":
    # 输入文件夹位置和特定字符串
    folder_path = input("请输入文件夹位置：")
    search_string = input("请输入要搜索的特定字符串：")

    # 调用函数查找匹配的.py文件
    matching_files = find_matching_files(folder_path, search_string)

    # 输出匹配的文件列表
    if len(matching_files) > 0:
        print("找到以下匹配的文件：")
        for file in matching_files:
            print(file)
    else:
        print("未找到匹配的文件。")
