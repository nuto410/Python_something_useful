import os

def replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r',encoding = 'utf-8') as file:
        file_data = file.read()
    
    updated_data = file_data.replace(old_string, new_string)
    
    with open(file_path, 'w',encoding = 'utf-8') as file:
        file.write(updated_data)

def replace_string_in_files(directory, old_string, new_string):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                replace_string_in_file(file_path, old_string, new_string)

if __name__ == "__main__":
    target_directory = input("請輸入位置：")
    old_string = input("請輸入要被取代的特定字串：")
    new_string = input("請輸入要修改為的字串：")

    replace_string_in_files(target_directory, old_string, new_string)

    print("字串取代完成！")
