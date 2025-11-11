import winreg
import psutil
import platform
import socket
import subprocess
from datetime import datetime
from ..models.system_info import SystemInfo, HardwareInfo, SoftwareInfo, NetworkInfo


class SystemScanner:
    
    def __init__(self):
        self.system_info = SystemInfo()
    
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
    
    def scan_os_info(self):
        os_info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'hostname': socket.gethostname()
        }
        return os_info
    
    def scan_installed_software(self):
        installed_software = []
        
        try:
            # Для Windows используем реестр для получения списка установленных программ
            import winreg
            
            # Ключи реестра для установленных программ
            registry_paths = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            ]
            
            for registry_path in registry_paths:
                try:
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            subkey = winreg.OpenKey(key, subkey_name)
                            
                            name = self._get_reg_value(subkey, "DisplayName")
                            version = self._get_reg_value(subkey, "DisplayVersion")
                            publisher = self._get_reg_value(subkey, "Publisher")
                            
                            if name:  
                                software_info = {
                                    'name': name,
                                    'version': version,
                                    'publisher': publisher
                                }
                                installed_software.append(software_info)
                                
                            winreg.CloseKey(subkey)
                        except WindowsError:
                            continue
                    winreg.CloseKey(key)
                except WindowsError:
                    continue
                    
        except ImportError:
            pass
        
        return installed_software
    
    def _get_reg_value(self, key, value_name):
        try:
            value, _ = winreg.QueryValueEx(key, value_name)
            return value
        except WindowsError:
            return None
    
    def scan_network_interfaces(self):
        interfaces = []
        for interface_name, interface_addresses in psutil.net_if_addrs().items():
            interface_info = {
                'name': interface_name,
                'addresses': []
            }
            
            for address in interface_addresses:
                address_info = {
                    'family': str(address.family),
                    'address': address.address,
                    'netmask': address.netmask,
                    'broadcast': address.broadcast
                }
                interface_info['addresses'].append(address_info)
            
            interfaces.append(interface_info)
        return interfaces
    
    def scan_network_connections(self):
        connections = []
        for conn in psutil.net_connections():
            connection_info = {
                'family': str(conn.family),
                'type': str(conn.type),
                'local_address': f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else None,
                'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None,
                'status': conn.status
            }
            connections.append(connection_info)
        return connections
    
    def _bytes_to_gb(self, bytes_value):
        return round(bytes_value / (1024 ** 3), 2)
    
    def scan_hardware(self):
        print("Сканирование аппаратного обеспечения...")
        
        self.system_info.hardware.cpu_info = self.scan_cpu()
        self.system_info.hardware.memory_info = self.scan_memory()
        self.system_info.hardware.disk_info = self.scan_disks()
        
        return self.system_info
    
    def scan_software(self):
        print("Сканирование программного обеспечения...")
        
        self.system_info.software.os_info = self.scan_os_info()
        self.system_info.software.installed_software = self.scan_installed_software()
        
        return self.system_info
    
    def scan_network(self):
        print("Сканирование сетевых настроек...")
        
        self.system_info.network.network_interfaces = self.scan_network_interfaces()
        self.system_info.network.connections = self.scan_network_connections()
        
        return self.system_info
    
    def full_scan(self):
        print("Запуск полного сканирования системы...")
        
        self.scan_hardware()
        self.scan_software()
        self.scan_network()
        
        self.system_info.timestamp = datetime.now().isoformat()
        
        print("Сканирование завершено!")
        return self.system_info