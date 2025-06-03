# 💼 Salary Report Generator

Скрипт на Python для генерации отчётов по CSV-данным сотрудников.  
Модульная структура проекта позволяет легко добавлять новые типы отчётов и форматы вывода.

---

## 🚀 Быстрый запуск

```bash
python main.py data1.csv data2.csv --report payout
```

Можно указать один или несколько CSV-файлов.

---

## ⚙️ Форматы вывода

По умолчанию:

- Отчёт выводится **в читаемом табличном виде** через метод `.print()` внутри класса `PayoutReport`.
- Также поддерживается **вывод в формате JSON** — возвращается **строка**, сформированная через `json.dumps(...)`, которую можно вывести в консоль или сохранить в файл.

### 📤 Пример: вывод в консоль

```python
from reports.output import to_json

json_string = to_json(data)
print(json_string)  # читаемый JSON-формат
```

### 💾 Пример: сохранение в файл

```python
import json

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
```

---

## 🧩 Расширяемость

### ➕ Как добавить новый тип отчёта

1. Создайте файл в `reports/`, например `efficiency.py`
2. Наследуйте `BaseReport` и реализуйте метод `generate(self, data: dict) -> dict`
3. Реализуйте метод `print_report(self, data: dict)` — если нужен собственный способ отображения
4. Добавьте имя отчёта в `AVAILABLE_REPORTS` в `config.py`
5. Обновите `main.py`, добавив обработку нового отчёта

---

## 🧱 Структура проекта

| Путь                            | Назначение |
|---------------------------------|------------|
| `data/`                         | Входные CSV-файлы |
| `readers/csv_reader.py`         | Чтение CSV |
| `services/report_builder.py`    | Построение структуры отчёта |
| `reports/base.py`               | Абстрактный базовый класс для всех отчётов |
| `reports/payout.py`             | Отчёт по выплатам (`.generate()` и `.print_report()`) |
| `reports/output.py`             | Альтернативные форматы вывода (например, JSON) |
| `utils/validation_script.py`    | Проверка аргументов и файлов |
| `config.py`                     | Константы, поддерживаемые отчёты и поля |
| `main.py`                       | Точка входа и CLI-интерфейс |

---

## ⚠️ Обработка ошибок

Скрипт проверяет:

- Наличие всех указанных CSV-файлов
- Корректность имени отчёта (`--report`)
- Неизвестные аргументы

При наличии ошибок:

```bash
❌ Файл не найден: data_missing.csv
❌ Отчёт 'invalid' не поддерживается.
```

---

## 📄 Пример CSV-файла

```csv
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60
```


## ✅ Покрытие тестами

```
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
readers/__init__.py              0      0   100%
readers/csv_reader.py           13      0   100%
reports/__init__.py              0      0   100%
reports/base.py                  5      1    80%   6
reports/output.py                6      0   100%
reports/payout.py               23      0   100%
services/__init__.py             0      0   100%
services/report_builder.py      15      0   100%
utils/__init__.py                0      0   100%
utils/validation_script.py      17      0   100%
----------------------------------------------------------
TOTAL                           79      1    99%
```