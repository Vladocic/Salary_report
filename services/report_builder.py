from collections import defaultdict


def build_report_data(rows:dict, possible_keys: list[str]) -> dict:
    result = defaultdict(lambda: {"employees":[]})

    for row in rows:
        department = row["department"]
        name = row["name"]
        hours = int(row["hours_worked"])
        rate = extract_value(row=row, possible_keys=possible_keys)

        date = {"name":name, "hours":hours, "rate":rate}

        result[department]["employees"].append(date)

    return result



def extract_value(row: dict, possible_keys: list[str]) -> int:
    for key in possible_keys:
        if key in row:
            return int(row[key])
