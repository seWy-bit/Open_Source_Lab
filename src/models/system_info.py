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


class SoftwareInfo:
    def __init__(self):
        self.os_info = {}
        self.installed_software = []
    
    def to_dict(self):
        return {
            'operating_system': self.os_info,
            'installed_software': self.installed_software
        }


class NetworkInfo:
    def __init__(self):
        self.network_interfaces = []
        self.connections = []
    
    def to_dict(self):
        return {
            'network_interfaces': self.network_interfaces,
            'connections': self.connections
        }


class SystemInfo:    
    def __init__(self):
        self.hardware = HardwareInfo()
        self.software = SoftwareInfo()
        self.network = NetworkInfo()
        self.timestamp = None
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'hardware': self.hardware.to_dict(),
            'software': self.software.to_dict(),
            'network': self.network.to_dict()
        }