class HardwareInfo:  
    def __init__(self):
        self.cpu_info = {}
        self.memory_info = {}
        self.disk_info = []
        self.gpu_info = []
    
    def to_dict(self):
        return {
            'cpu': self.cpu_info,
            'memory': self.memory_info,
            'disks': self.disk_info,
            'gpu': self.gpu_info
        }


class SystemInfo:
    def __init__(self):
        self.hardware = HardwareInfo()
        self.timestamp = None
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'hardware': self.hardware.to_dict()
        }