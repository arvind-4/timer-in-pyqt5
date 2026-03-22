"""Tests for the build_palette() helper."""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette


class TestBuildPaletteType:
    def test_returns_qpalette(self, timer_app_module):
        assert isinstance(timer_app_module.build_palette(), QPalette)


class TestBuildPaletteColors:
    def test_window(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Window) == QColor(83, 83, 83)

    def test_window_text_white(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.WindowText) == QColor(Qt.white)

    def test_base(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Base) == QColor(25, 25, 25)

    def test_alternate_base(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.AlternateBase) == QColor(53, 53, 53)

    def test_tooltip_base_white(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.ToolTipBase) == QColor(Qt.white)

    def test_tooltip_text_white(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.ToolTipText) == QColor(Qt.white)

    def test_text_white(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Text) == QColor(Qt.white)

    def test_button(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Button) == QColor(53, 53, 53)

    def test_button_text_white(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.ButtonText) == QColor(Qt.white)

    def test_bright_text_red(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.BrightText) == QColor(Qt.red)

    def test_link(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Link) == QColor(42, 130, 218)

    def test_highlight(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.Highlight) == QColor(42, 130, 218)

    def test_highlighted_text_gray(self, timer_app_module):
        p = timer_app_module.build_palette()
        assert p.color(QPalette.HighlightedText) == QColor(Qt.gray)


class TestBuildPaletteIdempotency:
    def test_two_calls_produce_equal_palettes(self, timer_app_module):
        p1 = timer_app_module.build_palette()
        p2 = timer_app_module.build_palette()
        for role in [
            QPalette.Window,
            QPalette.Base,
            QPalette.Button,
            QPalette.Link,
            QPalette.Highlight,
        ]:
            assert p1.color(role) == p2.color(role)
