from reports.payout import PayoutReport


def test_generate_payout():
    data = {
        "HR": {
            "employees": [
                {"name": "Grace Lee", "hours": 160, "rate": 45},
                {"name": "Ivy Clark", "hours": 158, "rate": 38},
                {"name": "Liam Harris", "hours": 155, "rate": 42}
            ]
        }
    }

    report = PayoutReport()
    result = report.generate(data)
    assert result["HR"]["employees"][0]["payout"] == "$7200"
    assert result["HR"]["total_hours"] == 473
    assert result["HR"]["total_payout"] == "$19714"



def test_print_report_output(capsys):
    data = {
        "HR": {
            "employees": [
                {"name": "Grace Lee", "hours": 160, "rate": 45, "payout": "$7200"},
                {"name": "Ivy Clark", "hours": 158, "rate": 38, "payout": "$6004"},
                {"name": "Liam Harris", "hours": 155, "rate": 42, "payout": "$6510"}
            ],
            "total_hours": 473,
            "total_payout": "$19714"
        }
    }

    report = PayoutReport()
    report.print_report(data)

    captured = capsys.readouterr()
    assert "HR" in captured.out
    assert "Grace Lee" in captured.out
    assert "$19714" in captured.out