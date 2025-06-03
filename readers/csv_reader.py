import os


def read_csv_files(files:list[str], data_dir:str) -> list[dict]:
    rows = []

    for file in files:
        file_path = os.path.join(data_dir, file)
        with open (file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

            header = lines[0].strip().split(",")
            for line in lines[1:]:
                value = line.strip().split(",")
                row_dict = dict(zip(header, value))
                rows.append(row_dict)

    return rows 


