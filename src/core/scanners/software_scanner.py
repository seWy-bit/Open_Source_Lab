import platform
import socket
import winreg
from src.models.system_info import SoftwareInfo


class SoftwareScanner:
    def __init__(self):
        self.software_info = SoftwareInfo()
    
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
    
    def scan(self):
        print("Сканирование программного обеспечения...")
        
        self.software_info.os_info = self.scan_os_info()
        self.software_info.installed_software = self.scan_installed_software()
        
        return self.software_info