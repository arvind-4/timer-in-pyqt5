"""PyQt5 timer application."""

import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QIcon, QPalette

ROOT_DIR = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT_DIR / "static" / "timer.png"
SECONDS_PER_MINUTE = 60
HOURS_PER_DAY = 24
TIMER_INTERVAL_MS = 1000


def format_elapsed(hours: int, minutes: int, seconds: int) -> str:
    """Format elapsed time as `HH:MM:SS`."""
    return f"{hours:02}:{minutes:02}:{seconds:02}"


class TimerWindow:
    """Render and control the timer window."""

    def __init__(self) -> None:
        """Build the widgets, signal bindings, and timer state."""
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.current_time = format_elapsed(0, 0, 0)

        self.window = QtWidgets.QWidget()
        self.window.setObjectName("timerWindow")
        self.window.setWindowTitle("Timer --Arvind")
        self.window.resize(360, 240)
        self.window.setMinimumSize(QtCore.QSize(360, 240))
        self.window.setMaximumSize(QtCore.QSize(360, 240))

        self.text_browser = QtWidgets.QTextBrowser(self.window)
        self.text_browser.setGeometry(QtCore.QRect(10, 190, 341, 41))
        self.text_browser.setObjectName("textBrowser")

        self.lcd_number = QtWidgets.QLCDNumber(self.window)
        self.lcd_number.setGeometry(QtCore.QRect(10, 10, 341, 141))
        self.lcd_number.setObjectName("lcdNumber")
        self.lcd_number.setDigitCount(len(self.current_time))
        self.lcd_number.display(self.current_time)

        button_container = QtWidgets.QWidget(self.window)
        button_container.setGeometry(QtCore.QRect(10, 160, 341, 25))
        button_container.setObjectName("buttonContainer")

        button_layout = QtWidgets.QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setObjectName("horizontalLayout")

        self.start_button = QtWidgets.QPushButton("Start", button_container)
        self.pause_button = QtWidgets.QPushButton("Pause", button_container)
        self.lap_button = QtWidgets.QPushButton("Lap", button_container)
        self.reset_button = QtWidgets.QPushButton("Reset", button_container)

        for button in (
            self.start_button,
            self.pause_button,
            self.lap_button,
            self.reset_button,
        ):
            button_layout.addWidget(button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.start_button.clicked.connect(self.start)
        self.pause_button.clicked.connect(self.pause)
        self.lap_button.clicked.connect(self.record_lap)
        self.reset_button.clicked.connect(self.reset)

        self.apply_icon()

    def apply_icon(self) -> None:
        """Apply the application icon when the asset is available."""
        if ICON_PATH.is_file():
            icon = QIcon(str(ICON_PATH))
            self.window.setWindowIcon(icon)

            app = QtWidgets.QApplication.instance()
            if app is not None:
                app.setWindowIcon(icon)

    def start(self) -> None:
        """Start counting elapsed time."""
        self.timer.start(TIMER_INTERVAL_MS)

    def pause(self) -> None:
        """Pause the timer."""
        self.timer.stop()

    def reset(self) -> None:
        """Reset the timer and clear lap history."""
        self.timer.stop()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.current_time = format_elapsed(self.hours, self.minutes, self.seconds)
        self.lcd_number.setDigitCount(len(self.current_time))
        self.lcd_number.display(self.current_time)
        self.text_browser.clear()

    def record_lap(self) -> None:
        """Record the current time as a lap."""
        if self.timer.isActive():
            self.text_browser.append(f"The Lap is : {self.current_time}")
        else:
            self.text_browser.clear()

    def tick(self) -> None:
        """Advance the timer by one second and refresh the display."""
        if self.seconds < SECONDS_PER_MINUTE - 1:
            self.seconds += 1
        elif self.minutes < SECONDS_PER_MINUTE - 1:
            self.seconds = 0
            self.minutes += 1
        elif self.hours < HOURS_PER_DAY:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        else:
            self.timer.stop()
            return

        self.current_time = format_elapsed(self.hours, self.minutes, self.seconds)
        self.lcd_number.setDigitCount(len(self.current_time))
        self.lcd_number.display(self.current_time)

    def show(self) -> None:
        """Show the timer window."""
        self.window.show()


def build_palette() -> QPalette:
    """Create the application's dark palette."""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(83, 83, 83))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.gray)
    return palette


def main() -> int:
    """Launch the timer application."""
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(build_palette())
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; "
        "border: 1px solid white; }"
    )

    timer_window = TimerWindow()
    timer_window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
