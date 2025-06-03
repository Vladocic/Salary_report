from services.report_builder import build_report_data


def test_build_report_data():
    rows = [
        {"name": "Alice Johnson", "department": "Marketing", "hours_worked": "160", "salary": "50"},
        {"name": "Bob Smith", "department": "Design", "hours_worked": "150", "salary": "40"},
        {"name": "Carol Williams", "department": "Design", "hours_worked": "170", "salary": "60"}
    ]
    result = build_report_data(rows, possible_keys=["salary"])
    assert "Design" and "Marketing" in result
    assert len(result["Design"]["employees"]) == 2
    assert len(result["Marketing"]["employees"]) == 1
    assert result["Marketing"]["employees"][0]["rate"] == 50


