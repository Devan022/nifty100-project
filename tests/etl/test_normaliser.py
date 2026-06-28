import pytest
from src.etl.normaliser import DataNormaliser


def test_year_integer():
    assert DataNormaliser.normalize_year(2023) == 2023


def test_year_fy():
    assert DataNormaliser.normalize_year("FY2023") == 2023


def test_year_with_space():
    assert DataNormaliser.normalize_year("FY 2022") == 2022


def test_invalid_year():
    assert DataNormaliser.normalize_year("abcd") is None


def test_ticker_lower():
    assert DataNormaliser.normalize_ticker("reliance") == "RELIANCE"


def test_ticker_spaces():
    assert DataNormaliser.normalize_ticker(" reliance ") == "RELIANCE"


def test_ticker_ns():
    assert DataNormaliser.normalize_ticker("RELIANCE.NS") == "RELIANCE"


def test_ticker_bo():
    assert DataNormaliser.normalize_ticker("tcs.bo") == "TCS"