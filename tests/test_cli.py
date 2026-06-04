from budget_planner.cli import validate_month


def test_validate_month() -> None:
    assert validate_month("2026-06") == "2026-06"

