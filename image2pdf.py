from PIL import Image
import os

def images_to_pdf(input_folder, output_pdf):
    # 支援的圖片格式
    supported_formats = ('.jpg', '.jpeg', '.png')

    # 獲取所有圖片檔案並排序
    image_files = sorted(
        [f for f in os.listdir(input_folder) if f.lower().endswith(supported_formats)]
    )

    if not image_files:
        print("未找到任何 jpg 或 png 格式的圖片！")
        return

    # 讀取並打開圖片
    images = []
    for file in image_files:
        image_path = os.path.join(input_folder, file)
        img = Image.open(image_path).convert("RGB")  # 確保圖片格式為 RGB
        images.append(img)

    # 儲存為 PDF
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"已成功將圖片合併為 PDF：{output_pdf}")

# 設定輸入資料夾和輸出 PDF 檔名
input_folder = "image_files"
output_pdf = "output.pdf"

images_to_pdf(input_folder, output_pdf)
