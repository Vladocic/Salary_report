import argparse
import os
from config import AVAILABLE_REPORTS, POSSIBLE_RATE_KEYS, DATA_DIR
from readers.csv_reader import read_csv_files
from reports.output import save_to_json, to_json
from services.report_builder import build_report_data
from utils.validation_script import validation_all
from reports.payout import PayoutReport

parser = argparse.ArgumentParser(description="Скрипт для генерации отчётов")

parser.add_argument("files", nargs="+")
parser.add_argument("--report", required=True)

args, unknown = parser.parse_known_args()

files = args.files
report = args.report


validation_all(files=files,unknown=unknown,report_name=report, available_reports=AVAILABLE_REPORTS, data_dir=DATA_DIR)
rows = read_csv_files(files=files, data_dir=DATA_DIR)
rows = build_report_data(rows=rows, possible_keys=POSSIBLE_RATE_KEYS)

if report == "payout":
    report_payout = PayoutReport()
    final_report = report_payout.generate(data=rows)
    report_payout.print_report(data=final_report)
    save_to_json(report_data=final_report)
