from reports.output import save_to_json, to_json
import json


def test_to_json():
    data = {"HR": {"employees": [{"name": "Grace Lee", "hours": 160, "rate": 45, "payout": "$7200"}], "total_hours": 160, "total_payout": "$7200"}}
    json_str = to_json(data)
    obj = json.loads(json_str)
    assert obj["HR"]["total_payout"] == "$7200"

def test_save_to_json(tmp_path):
    data = {"HR": {"employees": [{"name": "Grace Lee", "hours": 160, "rate": 45, "payout": "$7200"}], "total_hours": 160, "total_payout": "$7200"}}
    file_path = tmp_path / "report.json"
    
    save_to_json(data, path=str(file_path))
    
    result = json.loads(file_path.read_text(encoding="utf-8"))
    assert result["HR"]["employees"][0]["name"] == "Grace Lee"