"""Tests for TimerWindow.reset()."""


class TestReset:
    def test_timer_stopped(self, timer_window):
        timer_window.start()
        timer_window.reset()
        assert not timer_window.timer.isActive()

    def test_hours_zeroed(self, timer_window):
        timer_window.hours = 5
        timer_window.reset()
        assert timer_window.hours == 0

    def test_minutes_zeroed(self, timer_window):
        timer_window.minutes = 30
        timer_window.reset()
        assert timer_window.minutes == 0

    def test_seconds_zeroed(self, timer_window):
        timer_window.seconds = 45
        timer_window.reset()
        assert timer_window.seconds == 0

    def test_current_time_zeroed(self, timer_window):
        timer_window.start()
        timer_window.tick()
        timer_window.reset()
        assert timer_window.current_time == "00:00:00"

    def test_text_browser_cleared(self, timer_window):
        timer_window.start()
        timer_window.record_lap()
        timer_window.reset()
        assert timer_window.text_browser.toPlainText().strip() == ""

    def test_reset_without_start_is_safe(self, timer_window):
        timer_window.reset()  # must not raise
        assert timer_window.current_time == "00:00:00"

    def test_lcd_digit_count_reset(self, timer_window):
        timer_window.reset()
        assert timer_window.lcd_number.digitCount() == 8
