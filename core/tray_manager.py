import sys
import threading
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QObject, pyqtSignal

class TrayManager(QObject):
    """Manages system tray icon and stealth mode"""
    
    toggle_visibility = pyqtSignal()
    exit_requested = pyqtSignal()
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.tray_icon = None
        self.is_hidden = False
        
    def setup_tray(self, icon_path="icon.ico"):
        """Setup system tray icon"""
        # Create tray icon
        self.tray_icon = QSystemTrayIcon(self.app)
        
        # Load icon
        if icon_path and os.path.exists(icon_path):
            self.tray_icon.setIcon(QIcon(icon_path))
        else:
            # Create a generic icon
            pixmap = QPixmap(16, 16)
            pixmap.fill(Qt.transparent)
            self.tray_icon.setIcon(QIcon(pixmap))
        
        # Create context menu
        menu = QMenu()
        
        show_action = menu.addAction("Show/Hide")
        show_action.triggered.connect(self.toggle_visibility.emit)
        
        menu.addSeparator()
        
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(self.exit_requested.emit)
        
        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()
        
    def toggle_window(self, window):
        """Toggle window visibility"""
        if window.isVisible():
            window.hide()
            self.is_hidden = True
        else:
            window.show()
            window.activateWindow()
            self.is_hidden = False
            
    def hide_to_tray(self, window):
        """Hide window to system tray"""
        window.hide()
        self.is_hidden = True