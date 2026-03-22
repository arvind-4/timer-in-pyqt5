"""Tests for TimerWindow.tick()."""


class TestTickBasic:
    def test_increments_seconds(self, timer_window):
        timer_window.tick()
        assert timer_window.seconds == 1

    def test_updates_current_time(self, timer_window):
        timer_window.tick()
        assert timer_window.current_time == "00:00:01"

    def test_updates_lcd_digit_count(self, timer_window):
        timer_window.tick()
        assert timer_window.lcd_number.digitCount() == len(timer_window.current_time)

    def test_multiple_ticks_accumulate(self, timer_window):
        for _ in range(5):
            timer_window.tick()
        assert timer_window.seconds == 5
        assert timer_window.current_time == "00:00:05"


class TestTickRollover:
    def test_seconds_roll_over_to_minutes(self, timer_window):
        timer_window.seconds = 59
        timer_window.tick()
        assert timer_window.minutes == 1
        assert timer_window.seconds == 0

    def test_minutes_roll_over_to_hours(self, timer_window):
        timer_window.minutes = 59
        timer_window.seconds = 59
        timer_window.tick()
        assert timer_window.hours == 1
        assert timer_window.minutes == 0
        assert timer_window.seconds == 0

    def test_current_time_after_minute_rollover(self, timer_window):
        timer_window.seconds = 59
        timer_window.tick()
        assert timer_window.current_time == "00:01:00"

    def test_current_time_after_hour_rollover(self, timer_window):
        timer_window.minutes = 59
        timer_window.seconds = 59
        timer_window.tick()
        assert timer_window.current_time == "01:00:00"


class TestTickAtMax:
    def test_stops_timer_at_24_hours(self, timer_window):
        # All three conditions must be exhausted to reach the else: timer.stop()
        timer_window.hours = 24
        timer_window.minutes = 59
        timer_window.seconds = 59
        timer_window.start()
        timer_window.tick()
        assert not timer_window.timer.isActive()

    def test_state_unchanged_after_max(self, timer_window):
        timer_window.hours = 24
        timer_window.minutes = 59
        timer_window.seconds = 59
        timer_window.tick()
        assert timer_window.hours == 24
        assert timer_window.minutes == 59
        assert timer_window.seconds == 59
