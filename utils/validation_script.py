import sys
import os


def validation_all(files: list[str], unknown: list[str], report_name: str, available_reports: list[str], data_dir="data"):
    errors = []
    
    for file in files:
        file_path = os.path.join(data_dir, file)
        if not os.path.isfile(file_path):
            errors.append(f"❌ Файл не найден: {file}")

    if unknown:
        errors.append(f"❌ Неизвестные аргументы: {unknown}")

    if report_name not in available_reports:
        errors.append(f"❌ Отчёт '{report_name}' не поддерживается.\n✅ Доступные отчёты: {', '.join(available_reports)}")

    if errors:
        print("Обнаружены ошибки:")
        for err in errors:
            print(err)
        sys.exit(1)