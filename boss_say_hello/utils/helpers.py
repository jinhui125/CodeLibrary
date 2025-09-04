import yaml
from pathlib import Path

# 加载yaml文件数据
def load_yaml_file(file_path):

    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f'文件不存在：{file_path}')
    
    with open(file=file_path, mode='r', encoding='utf-8') as fb:
        return yaml.safe_load(fb)


if __name__ == '__main__':

    test_data = load_yaml_file(file_path='../test_data/test_data.yaml')
    print(test_data)