import psutil
import platform
from src.models.system_info import HardwareInfo


class HardwareScanner:
    def __init__(self):
        self.hardware_info = HardwareInfo()
    
    def scan_cpu(self):
        cpu_info = {
            'physical_cores': psutil.cpu_count(logical=False),
            'total_cores': psutil.cpu_count(logical=True),
            'max_frequency': psutil.cpu_freq().max if psutil.cpu_freq() else None,
            'current_frequency': psutil.cpu_freq().current if psutil.cpu_freq() else None,
            'processor': platform.processor(),
            'architecture': platform.architecture()[0]
        }
        return cpu_info
    
    def scan_memory(self):
        memory = psutil.virtual_memory()
        memory_info = {
            'total': self._bytes_to_gb(memory.total),
            'available': self._bytes_to_gb(memory.available),
            'used': self._bytes_to_gb(memory.used),
            'percentage': memory.percent
        }
        return memory_info
    
    def scan_disks(self):
        disks = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info = {
                    'device': partition.device,
                    'mountpoint': partition.mountpoint,
                    'fstype': partition.fstype,
                    'total_size': self._bytes_to_gb(usage.total),
                    'used': self._bytes_to_gb(usage.used),
                    'free': self._bytes_to_gb(usage.free),
                    'percent_used': usage.percent
                }
                disks.append(disk_info)
            except PermissionError:
                continue
        return disks
    
    def _bytes_to_gb(self, bytes_value):
        return round(bytes_value / (1024 ** 3), 2)
    
    def scan(self):
        print("Сканирование аппаратного обеспечения...")
        
        self.hardware_info.cpu_info = self.scan_cpu()
        self.hardware_info.memory_info = self.scan_memory()
        self.hardware_info.disk_info = self.scan_disks()
        
        return self.hardware_info