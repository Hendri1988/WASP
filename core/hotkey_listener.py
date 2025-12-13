from pynput import keyboard
from PyQt6.QtCore import QObject, pyqtSignal

class HotkeyListener(QObject):
    stop_triggered = pyqtSignal()
    
    def __init__(self, hotkey='<f9>'):
        super().__init__()
        self.hotkey = hotkey
        self.listener = None
        
    def start(self):
        """Start listening for hotkey"""
        if self.listener is None:
            self.listener = keyboard.GlobalHotKeys({
                self.hotkey: self.on_hotkey_pressed
            })
            self.listener.start()
            
    def stop(self):
        """Stop listening for hotkey"""
        if self.listener is not None:
            self.listener.stop()
            self.listener = None
            
    def on_hotkey_pressed(self):
        """Called when hotkey is pressed"""
        self.stop_triggered.emit()