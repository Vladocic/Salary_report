import pytest
from utils.validation_script import validation_all


def test_validation_all_valid(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("id,email,name,department,hours_worked,hourly_rate\n")
    validation_all(files=["test.csv"], unknown=[], report_name="payout", available_reports=["payout"], data_dir=str(tmp_path))


def test_validation_all_invalid_file(tmp_path):
    with pytest.raises(SystemExit):
        validation_all(files=["file.csv"], unknown=[], report_name="payout", available_reports=["payout"], data_dir=str(tmp_path))


def test_validation_all_invalid_report(tmp_path):
    with pytest.raises(SystemExit):
        validation_all(files=[], unknown=[], report_name="wrong", available_reports=["payout"], data_dir=str(tmp_path))


def test_validation_all_unknown_args(tmp_path):
    with pytest.raises(SystemExit):
        validation_all(files=[], unknown=["--bad"], report_name="payout", available_reports=["payout"], data_dir=str(tmp_path))
