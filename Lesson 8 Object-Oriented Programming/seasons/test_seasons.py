import pytest
from datetime import date, timedelta
from season import calculate_minutes

def test_valid_date_returns_string():
    result = calculate_minutes("2000-01-01")
    assert isinstance(result, str)
    assert result.endswith("minutes")

def test_invalid_date_returns_none():
    assert calculate_minutes("invalid-date") is None
    assert calculate_minutes("2020/01/01") is None
    assert calculate_minutes("01-01-2000") is None

def test_minutes_calculation_today():
    today_str = date.today().strftime("%Y-%m-%d")
    result = calculate_minutes(today_str)
    # 0 days difference means 0 minutes
    assert result.startswith("Zero")

def test_minutes_calculation_known_date():
    # Calculate difference manually for a known date, e.g. 10 days ago
    ten_days_ago = (date.today() - timedelta(days=10)).strftime("%Y-%m-%d")
    result = calculate_minutes(ten_days_ago)
    # 10 days * 24 * 60 = 14400 minutes
    # Number in words should include 'fourteen thousand four hundred'
    assert "fourteen thousand, four hundred" in result.lower()

