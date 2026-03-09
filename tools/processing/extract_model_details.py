#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

TOOLS_DIR = Path(__file__).resolve().parents[1]
if str(TOOLS_DIR) not in sys.path:
    sys.path.append(str(TOOLS_DIR))

from utils.file_discovery import export_directory, get_export_by_date, get_latest_export  # noqa: E402


def extract_details(data, module, field_name):
    if module in data:
        fields = data[module].get('fields', [])
        for field in fields:
            if field.get('api_name') == field_name:
                return field
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract selected field details from export")
    parser.add_argument("--date", help="Export date (YYYY-MM-DD). Defaults to latest export.")
    return parser.parse_args()


def main():
    args = parse_args()
    export = (
        get_export_by_date(args.date, export_directory()).ensure_both()
        if args.date
        else get_latest_export(export_directory()).ensure_both()
    )

    data = json.loads(export.data_model.read_text())
    details = {}

    status_field = extract_details(data, 'Registration_Records', 'Status')
    if status_field:
        details['Reg_Status'] = {
            'api_name': status_field.get('api_name'),
            'label': status_field.get('field_label'),
            'type': status_field.get('data_type'),
            'picklist_values': [p.get('display_value') for p in status_field.get('pick_list_values', [])]
        }

    course_code = extract_details(data, 'Registration_Records', 'Course_Code')
    if course_code:
        details['Reg_Course_Code'] = {
            'api_name': course_code.get('api_name'),
            'label': course_code.get('field_label'),
            'type': course_code.get('data_type')
        }

    courseaa = extract_details(data, 'Deals', 'Courseaa')
    if courseaa:
        details['Deals_Courseaa'] = {
            'api_name': courseaa.get('api_name'),
            'label': courseaa.get('field_label'),
            'type': courseaa.get('data_type')
        }

    deal_course = extract_details(data, 'Deals', 'Course')
    if deal_course:
        details['Deals_Course'] = {
            'api_name': deal_course.get('api_name'),
            'label': deal_course.get('field_label'),
            'type': deal_course.get('data_type')
        }

    inv_course = extract_details(data, 'Invoices', 'Course_Name')
    if inv_course:
        details['Inv_Course'] = {
            'api_name': inv_course.get('api_name'),
            'label': inv_course.get('field_label'),
            'type': inv_course.get('data_type')
        }

    inv_deal = extract_details(data, 'Invoices', 'Deal_Name__s')
    if inv_deal:
        details['Inv_Deal'] = {
            'api_name': inv_deal.get('api_name'),
            'label': inv_deal.get('field_label'),
            'type': inv_deal.get('data_type')
        }

    print(json.dumps(details, indent=2))


if __name__ == "__main__":
    main()
