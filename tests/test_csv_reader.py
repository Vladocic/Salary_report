from readers.csv_reader import read_csv_files


def test_read_csv_files(tmp_path):
    csv_content = "id,email,name,department,hours_worked,hourly_rate\n1,alice@example.com,Alice Johnson,Marketing,160,50"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    result = read_csv_files(["test.csv"], data_dir=str(tmp_path))
    assert len(result) == 1
    assert result[0]["name"] == "Alice Johnson"
    assert result[0]["hourly_rate"] == "50"