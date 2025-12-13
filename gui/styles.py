MAIN_STYLE = """
QMainWindow {
    background-color: #2b2b2b;
}

QWidget {
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 9pt;
}

QTabWidget::pane {
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 5px;
    background-color: #2b2b2b;
}

QTabBar::tab {
    background-color: #3a3a3a;
    color: #aaaaaa;
    padding: 8px 16px;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background-color: #3daee9;
    color: #ffffff;
    font-weight: bold;
}

QTabBar::tab:hover:!selected {
    background-color: #4a4a4a;
}

QGroupBox {
    border: 1px solid #3a3a3a;
    border-radius: 6px;
    margin-top: 8px;
    padding: 10px;
    font-weight: bold;
    font-size: 9pt;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #3daee9;
}

QPushButton {
    background-color: #3daee9;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
    font-size: 9pt;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #4fc3f7;
}

QPushButton:pressed {
    background-color: #0288d1;
}

QPushButton:disabled {
    background-color: #555555;
    color: #888888;
}

QPushButton#stopButton {
    background-color: #e74c3c;
}

QPushButton#stopButton:hover {
    background-color: #f85f4f;
}

QPushButton#stopButton:pressed {
    background-color: #c0392b;
}

QLabel {
    color: #ffffff;
    padding: 2px;
}

QLabel:disabled {
    color: #555555;
}

QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled {
    background-color: #2b2b2b;
    color: #555555;
    border: 1px solid #3a3a3a;
}

QSpinBox, QDoubleSpinBox, QTimeEdit {
    background-color: #3a3a3a;
    border: 1px solid #555555;
    border-radius: 3px;
    padding: 4px;
    min-width: 60px;
    font-size: 9pt;
}

QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus {
    border: 1px solid #3daee9;
}

QCheckBox {
    spacing: 6px;
    font-size: 9pt;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 3px;
    border: 1px solid #555555;
    background-color: #3a3a3a;
}

QCheckBox::indicator:checked {
    background-color: #3daee9;
    border: 1px solid #3daee9;
}

QCheckBox::indicator:checked:hover {
    background-color: #4fc3f7;
}

QTextEdit {
    background-color: #1e1e1e;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 5px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
}

QFrame {
    background-color: transparent;
}
"""
