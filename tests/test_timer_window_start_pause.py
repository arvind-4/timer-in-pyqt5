"""Tests for TimerWindow.start() and pause()."""

from src.main import TIMER_INTERVAL_MS


class TestStart:
    def test_timer_becomes_active(self, timer_window):
        timer_window.start()
        assert timer_window.timer.isActive()

    def test_interval_is_1000ms(self, timer_window):
        timer_window.start()
        assert timer_window.timer.interval() == TIMER_INTERVAL_MS

    def test_start_twice_stays_active(self, timer_window):
        timer_window.start()
        timer_window.start()
        assert timer_window.timer.isActive()


class TestPause:
    def test_timer_stops(self, timer_window):
        timer_window.start()
        timer_window.pause()
        assert not timer_window.timer.isActive()

    def test_pause_without_start_is_safe(self, timer_window):
        timer_window.pause()  # must not raise
        assert not timer_window.timer.isActive()

    def test_state_preserved_on_pause(self, timer_window):
        timer_window.start()
        timer_window.tick()
        timer_window.pause()
        assert timer_window.seconds == 1
