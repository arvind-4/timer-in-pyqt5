"""Tests for TimerWindow initialisation state."""


class TestInitialState:
    def test_hours_zero(self, timer_window):
        assert timer_window.hours == 0

    def test_minutes_zero(self, timer_window):
        assert timer_window.minutes == 0

    def test_seconds_zero(self, timer_window):
        assert timer_window.seconds == 0

    def test_current_time(self, timer_window):
        assert timer_window.current_time == "00:00:00"

    def test_timer_not_active(self, timer_window):
        assert not timer_window.timer.isActive()

    def test_window_title(self, timer_window):
        assert timer_window.window.windowTitle() == "Timer --Arvind"

    def test_window_min_size(self, timer_window):
        assert timer_window.window.minimumWidth() == 360
        assert timer_window.window.minimumHeight() == 240

    def test_window_max_size(self, timer_window):
        assert timer_window.window.maximumWidth() == 360
        assert timer_window.window.maximumHeight() == 240

    def test_lcd_digit_count(self, timer_window):
        assert timer_window.lcd_number.digitCount() == 8

    def test_text_browser_empty(self, timer_window):
        assert timer_window.text_browser.toPlainText().strip() == ""

    def test_button_labels(self, timer_window):
        assert timer_window.start_button.text() == "Start"
        assert timer_window.pause_button.text() == "Pause"
        assert timer_window.lap_button.text() == "Lap"
        assert timer_window.reset_button.text() == "Reset"
