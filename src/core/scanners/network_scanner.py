import psutil
from src.models.system_info import NetworkInfo


class NetworkScanner:
    def __init__(self):
        self.network_info = NetworkInfo()
    
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
    
    def scan(self):
        print("Сканирование сетевых настроек...")
        
        self.network_info.network_interfaces = self.scan_network_interfaces()
        self.network_info.connections = self.scan_network_connections()
        
        return self.network_info