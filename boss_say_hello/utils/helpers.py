import re
import cv2
import yaml
import openslide
import numpy as np
import pytesseract
from PIL import Image
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract.exe'

# 加载yaml文件数据
def load_yaml_file(file_path):

    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f'文件不存在：{file_path}')
    
    with open(file=file_path, mode='r', encoding='utf-8') as fb:
        return yaml.safe_load(fb)

# 扫描图片中的文字内容
def OCR_image(image_path, lang='chi_sim+eng'):
    
    # img = Image.open(f'{image_path}')
    img = cv2.imread(image_path)

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, lang=lang, config='--oem 1 --psm 6')
    text = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  # 只相信置信度高于60%的结果
            # print(f"文本: {data['text'][i]}, 置信度: {data['conf'][i]}")
            text.append(data['text'][i])
    # print(''.join(text))
    return ''.join(text)

# 判断文本中是否有指定的字符串匹配的内容
def is_matched_string_list(text, pattern, flags='re.MULTILINE'):
    
    try:
        matches = re.findall(pattern=pattern, string=text, flags=flags)
        return True
    except re.error as e:
        print(f'正则表达式错误：{e}')
        return  False

if __name__ == '__main__':
    # result = OCR_image(image_path='./resume_png_lib/test_data_4.PNG')
    # print(result)
    result = load_yaml_file(file_path='./test_data/condition_data.yaml')
    with_condition = [ x for x in result['conditionData'] if '&' in x]
    or_condition = [y for y in result['conditionData'] if '&' not in y]
    print(result, with_condition, '|'.join(or_condition))