"""
Завдання 1. Рекурсивне копіювання файлів із сортуванням за розширенням.

Скрипт приймає два аргументи: вихідну директорію та (необов'язково) директорію
призначення (за замовчуванням 'dist'). Рекурсивно обходить вихідну директорію
і копіює кожен файл у піддиректорію, названу за його розширенням.

Запуск:
    python task_1.py <вихідна_директорія> [директорія_призначення]
"""

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли та сортує їх у піддиректорії за розширенням."
    )
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument(
        "dest",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Шлях до директорії призначення (за замовчуванням: dist)",
    )
    return parser.parse_args()


def copy_file(file_path: Path, dest_root: Path) -> None:
    """Копіює один файл у піддиректорію, названу за його розширенням."""
    # розширення без крапки; файли без розширення -> папка 'no_extension'
    extension = file_path.suffix[1:].lower() or "no_extension"
    target_dir = dest_root / extension
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, target_dir / file_path.name)
    except (OSError, shutil.Error) as e:
        print(f"[!] Не вдалося скопіювати {file_path}: {e}")


def process_directory(src: Path, dest_root: Path) -> None:
    """Рекурсивно обходить директорію та копіює знайдені файли."""
    try:
        for item in src.iterdir():
            # не заходимо в теку призначення, якщо вона всередині вихідної
            if item.resolve() == dest_root.resolve():
                continue
            if item.is_dir():
                process_directory(item, dest_root)
            elif item.is_file():
                copy_file(item, dest_root)
    except PermissionError as e:
        print(f"[!] Немає доступу до {src}: {e}")
    except OSError as e:
        print(f"[!] Помилка читання {src}: {e}")


def main() -> None:
    args = parse_args()
    source: Path = args.source
    dest: Path = args.dest

    if not source.exists() or not source.is_dir():
        print(f"[!] Вихідна директорія не існує або не є директорією: {source}")
        return

    process_directory(source, dest)
    print(f"Готово. Файли скопійовано та розсортовано в: {dest.resolve()}")


if __name__ == "__main__":
    main()
