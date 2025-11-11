import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.system_scanner import SystemScanner


def main():
    """Основная функция приложения"""
    print("Запуск SysInfo Collector")
    print("=" * 40)
    
    scanner = SystemScanner()
    system_info = scanner.scan_hardware()
    
    print("\nРезультаты сканирования:")
    print(f"Процессор: {system_info.hardware.cpu_info['processor']}")
    print(f"Ядер: {system_info.hardware.cpu_info['physical_cores']} физических, "
          f"{system_info.hardware.cpu_info['total_cores']} логических")
    print(f"Память: {system_info.hardware.memory_info['total']} GB "
          f"({system_info.hardware.memory_info['percentage']}% использовано)")
    
    print(f"Диски:")
    for disk in system_info.hardware.disk_info:
        print(f"   {disk['device']} - {disk['total_size']} GB "
              f"({disk['percent_used']}% использовано)")
    
    print(f"\nВремя сканирования: {system_info.timestamp}")


if __name__ == "__main__":
    main()