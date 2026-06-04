from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BUDGETS_DIR = ROOT / "budgets"
TEMPLATE = BUDGETS_DIR / "_template.md"


def validate_month(month: str) -> str:
    if not re.fullmatch(r"\d{4}-\d{2}", month):
        raise ValueError("Month must use YYYY-MM format")
    return month


def create_month(month: str) -> Path:
    month = validate_month(month)
    target = BUDGETS_DIR / f"{month}.md"
    if target.exists():
        raise FileExistsError(f"Budget already exists: {target}")

    shutil.copyfile(TEMPLATE, target)
    content = target.read_text(encoding="utf-8").replace("YYYY-MM", month)
    target.write_text(content, encoding="utf-8")
    return target


def check_month(month: str) -> str:
    month = validate_month(month)
    path = BUDGETS_DIR / f"{month}.md"
    if not path.exists():
        return f"No budget file found: {path}"

    content = path.read_text(encoding="utf-8")
    total_line = next((line for line in content.splitlines() if line.startswith("| Total |")), "")
    return total_line or "No total row found."


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="budget-planner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_month = subparsers.add_parser("new-month", help="Create a monthly budget file")
    new_month.add_argument("month", help="Month in YYYY-MM format")

    check = subparsers.add_parser("check", help="Print the monthly total row")
    check.add_argument("month", help="Month in YYYY-MM format")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "new-month":
        print(create_month(args.month))
        return 0
    if args.command == "check":
        print(check_month(args.month))
        return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

