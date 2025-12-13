import pyautogui
import random
import time
from PyQt6.QtCore import QThread, pyqtSignal

class KeyboardSimulator(QThread):
    """Thread for simulating keyboard activity"""
    
    status_update = pyqtSignal(str)
    keystroke_count = pyqtSignal(int)
    
    # Safe keys to press that won't cause issues
    SAFE_KEYS = [
        'ctrl', 'shift', 'alt',  # Modifier keys (safe when pressed alone)
    ]
    
    def __init__(self):
        super().__init__()
        self.running = False
        self.enabled = False
        self.keystroke_interval = 30  # seconds between keystrokes
        self.keystroke_counter = 0
        
    def set_enabled(self, enabled):
        """Enable or disable keyboard simulation"""
        self.enabled = enabled
        
    def set_keystroke_interval(self, interval):
        """Set the interval between keystrokes in seconds"""
        self.keystroke_interval = max(5, interval)
        
    def stop(self):
        """Stop the keyboard simulator"""
        self.running = False
        
    def run(self):
        self.running = True
        self.keystroke_counter = 0
        last_keystroke_time = time.time()
        
        if self.enabled:
            self.status_update.emit("Keyboard simulation enabled")
        
        while self.running:
            try:
                if self.enabled:
                    current_time = time.time()
                    
                    # Check if it's time for a keystroke
                    if current_time - last_keystroke_time >= self.keystroke_interval:
                        # Press a random safe key
                        key = random.choice(self.SAFE_KEYS)
                        
                        # Press and release the key
                        pyautogui.press(key)
                        
                        self.keystroke_counter += 1
                        self.keystroke_count.emit(self.keystroke_counter)
                        last_keystroke_time = current_time
                        
                        self.status_update.emit(f"Keystroke: {key.upper()}")
                
                # Small delay
                time.sleep(1)
                
            except Exception as e:
                self.status_update.emit(f"Keyboard error: {str(e)}")
                break
        
        if self.enabled:
            self.status_update.emit("Keyboard simulation stopped")