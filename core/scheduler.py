from PyQt6.QtCore import QTimer, QTime, pyqtSignal, QObject
from datetime import datetime

class Scheduler(QObject):
    start_triggered = pyqtSignal()
    stop_triggered = pyqtSignal()
    status_update = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_schedule)
        self.timer.setInterval(1000)  # Check every second
        
        self.enabled = False
        self.start_time = QTime(9, 0)
        self.end_time = QTime(17, 0)
        self.is_running = False
        
    def set_schedule(self, start_time, end_time):
        """Set the start and end times"""
        self.start_time = start_time
        self.end_time = end_time
        
    def enable_scheduler(self, enabled):
        self.enabled = enabled
        if enabled:
            self.timer.start()
            self.status_update.emit("Scheduler enabled")
        else:
            self.timer.stop()
            self.status_update.emit("Scheduler disabled")
            
    def check_schedule(self):
        if not self.enabled:
            return
            
        current_time = QTime.currentTime()
        
        # Check if within scheduled time range
        if self.start_time <= current_time < self.end_time:
            if not self.is_running:
                self.is_running = True
                self.start_triggered.emit()
                self.status_update.emit(f"Scheduler: Started at {current_time.toString('hh:mm:ss')}")
        else:
            if self.is_running:
                self.is_running = False
                self.stop_triggered.emit()
                self.status_update.emit(f"Scheduler: Stopped at {current_time.toString('hh:mm:ss')}")