from datetime import datetime
from src.models.system_info import SystemInfo
from src.core.scanners import HardwareScanner, SoftwareScanner, NetworkScanner


class SystemManager:
    def __init__(self):
        self.system_info = SystemInfo()
        self.hardware_scanner = HardwareScanner()
        self.software_scanner = SoftwareScanner()
        self.network_scanner = NetworkScanner()
    
    def scan_hardware(self):
        print("Сканирование аппаратного обеспечения...")
        self.system_info.hardware = self.hardware_scanner.scan()
        return self.system_info
    
    def scan_software(self):
        print("Сканирование программного обеспечения...")
        self.system_info.software = self.software_scanner.scan()
        return self.system_info
    
    def scan_network(self):
        print("Сканирование сетевых настроек...")
        self.system_info.network = self.network_scanner.scan()
        return self.system_info
    
    def full_scan(self):
        print("Запуск полного сканирования системы...")
        
        self.scan_hardware()
        self.scan_software() 
        self.scan_network()
        
        self.system_info.timestamp = datetime.now().isoformat()
        
        print("Сканирование завершено!")
        return self.system_info
    
    def selective_scan(self, scan_hardware=True, scan_software=True, scan_network=True):
        print("Запуск выборочного сканирования системы...")
        
        if scan_hardware:
            self.scan_hardware()
        if scan_software:
            self.scan_software()
        if scan_network:
            self.scan_network()
        
        self.system_info.timestamp = datetime.now().isoformat()
        
        print("Выборочное сканирование завершено!")
        return self.system_info