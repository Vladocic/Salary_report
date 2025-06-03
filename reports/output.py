import json

def to_json(report_data: dict) -> str:
    return json.dumps(report_data, indent=4, ensure_ascii=False)


def save_to_json(report_data: dict, path:str = "report.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

