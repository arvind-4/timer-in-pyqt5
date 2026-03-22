"""Tests for TimerWindow.record_lap()."""


def _content(tw) -> str:
    return tw.text_browser.toPlainText().strip()


class TestRecordLap:
    def test_lap_appended_when_running(self, timer_window):
        timer_window.start()
        timer_window.tick()
        timer_window.record_lap()
        assert "00:00:01" in _content(timer_window)

    def test_lap_contains_label(self, timer_window):
        timer_window.start()
        timer_window.record_lap()
        assert "The Lap is" in _content(timer_window)

    def test_multiple_laps_recorded(self, timer_window):
        timer_window.start()
        timer_window.tick()
        timer_window.record_lap()
        timer_window.tick()
        timer_window.record_lap()
        assert _content(timer_window).count("The Lap is") == 2

    def test_lap_clears_browser_when_paused(self, timer_window):
        timer_window.start()
        timer_window.record_lap()
        timer_window.pause()
        timer_window.record_lap()
        assert _content(timer_window) == ""

    def test_no_lap_when_never_started(self, timer_window):
        timer_window.record_lap()
        assert _content(timer_window) == ""
