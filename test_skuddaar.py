import pytest

from skuddaar import isLeapYear


def test_year_divisible_by_4_not_100():
    assert isLeapYear(40) == True
    assert isLeapYear(100) == False

def test_year_divisible_by_400():
    assert isLeapYear(1600) == True
    assert isLeapYear(1300) == False
    assert isLeapYear(400) == False


def test_year_not_divisible_by_4():
    assert isLeapYear(400) == True
    assert isLeapYear(1935) == False


def test_year__divisible_by_100_not_400():
    assert isLeapYear(800) == True
    assert isLeapYear(500) == False


