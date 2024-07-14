from typing import List, Dict
from pathlib import Path

FILE_NAME = Path('cats.txt')


def get_cats_info(path: Path) -> List[Dict]:
    if not Path.exists(path):
        print("File not found")
        return []

    cat_list = []
    with open(path, mode='r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            cat_data = line.split(',')
            cat_list.append({
                "id": cat_data[0],
                "name": cat_data[1],
                "age": cat_data[2]
            })
    return cat_list


get_cats_info(FILE_NAME)
