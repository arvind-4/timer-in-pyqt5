"""Shared fixtures for the timer test suite."""

from __future__ import annotations

import sys
import pytest
from PyQt5 import QtWidgets


@pytest.fixture(scope="session")
def qapp():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    yield app


@pytest.fixture
def timer_window(qapp):
    from src.main import TimerWindow

    win = TimerWindow()
    yield win
    win.timer.stop()


@pytest.fixture
def timer_app_module():
    import src.main

    return src.main
