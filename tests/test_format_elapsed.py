"""Tests for the format_elapsed() helper."""

import pytest
from src.main import format_elapsed


class TestFormatElapsedZero:
    def test_returns_string(self):
        assert isinstance(format_elapsed(0, 0, 0), str)

    def test_all_zeros(self):
        assert format_elapsed(0, 0, 0) == "00:00:00"

    def test_length_is_eight(self):
        assert len(format_elapsed(0, 0, 0)) == 8


class TestFormatElapsedPadding:
    def test_hours_padded(self):
        assert format_elapsed(1, 0, 0) == "01:00:00"

    def test_minutes_padded(self):
        assert format_elapsed(0, 5, 0) == "00:05:00"

    def test_seconds_padded(self):
        assert format_elapsed(0, 0, 9) == "00:00:09"

    def test_all_single_digits_padded(self):
        assert format_elapsed(1, 2, 3) == "01:02:03"


class TestFormatElapsedTwoDigits:
    def test_hours_two_digits(self):
        assert format_elapsed(23, 0, 0) == "23:00:00"

    def test_minutes_two_digits(self):
        assert format_elapsed(0, 59, 0) == "00:59:00"

    def test_seconds_two_digits(self):
        assert format_elapsed(0, 0, 59) == "00:00:59"

    def test_all_two_digits(self):
        assert format_elapsed(12, 34, 56) == "12:34:56"


class TestFormatElapsedSeparators:
    def test_first_colon_at_index_2(self):
        assert format_elapsed(1, 2, 3)[2] == ":"

    def test_second_colon_at_index_5(self):
        assert format_elapsed(1, 2, 3)[5] == ":"

    def test_exactly_two_colons(self):
        assert format_elapsed(10, 20, 30).count(":") == 2


class TestFormatElapsedParametrized:
    @pytest.mark.parametrize(
        "h,m,s,expected",
        [
            (0, 0, 0, "00:00:00"),
            (0, 0, 1, "00:00:01"),
            (0, 1, 0, "00:01:00"),
            (1, 0, 0, "01:00:00"),
            (9, 9, 9, "09:09:09"),
            (23, 59, 59, "23:59:59"),
        ],
    )
    def test_various_inputs(self, h, m, s, expected):
        assert format_elapsed(h, m, s) == expected
