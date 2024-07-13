from typing import Tuple
from pathlib import Path

FILE_NAME = Path('salaries.txt')


def total_salary(path: Path) -> Tuple:
    if not Path.exists(path):
        print("File not found")
        return 0, 0

    devs_count = 0
    total = 0
    with open(path, mode='r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            total += int(line.split(',')[1])
            devs_count += 1
    return total, int(total / devs_count)


total_salary(FILE_NAME)
