from typing import List
from pathlib import Path
from colorama import Fore
import sys


def get_project_structure(sys_args: List[str]) -> str:
    if len(sys.argv) < 2:
        print(sys_args)
        return 'Please pass correct project path argument'

    path = Path(sys_args[1])
    if not Path.exists(path):
        return 'Project path does not exist'

    structure = f"{Fore.YELLOW}{Path.cwd().name}/{Fore.RESET}\n"
    for el in path.glob('*'):
        item = ""
        if Path.is_dir(el):
            item = f"{" " * 4}{Fore.YELLOW}{el.name}/{Fore.RESET}\n"
        if Path.is_file(el):
            item = f"{" " * 4}{Fore.CYAN}{el.name}{Fore.RESET}\n"
        structure += item

    return structure


get_project_structure(sys.argv)
