from src.core.system_scanner import SystemScanner
from src.core.json_exporter import JSONExporter


def display_system_info(system_info):
    """Отображает системную информацию в консоли"""
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ СКАНИРОВАНИЯ СИСТЕМЫ")
    print("="*50)
    
    # Аппаратное обеспечение
    print("\nАППАРАТНОЕ ОБЕСПЕЧЕНИЕ:")
    print(f"  Процессор: {system_info.hardware.cpu_info['processor']}")
    print(f"  Ядра: {system_info.hardware.cpu_info['physical_cores']} физических, "
          f"{system_info.hardware.cpu_info['total_cores']} логических")
    print(f"  Память: {system_info.hardware.memory_info['total']} GB "
          f"({system_info.hardware.memory_info['percentage']}% использовано)")
    
    print(f"  Диски:")
    for disk in system_info.hardware.disk_info:
        print(f"    {disk['device']} - {disk['total_size']} GB "
              f"({disk['percent_used']}% использовано)")
    
    # Программное обеспечение
    print("\nПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ:")
    print(f"  ОС: {system_info.software.os_info['system']} {system_info.software.os_info['release']}")
    print(f"  Установленных программ: {len(system_info.software.installed_software)}")
    
    # Сетевые настройки
    print("\nСЕТЕВЫЕ НАСТРОЙКИ:")
    print(f"  Сетевых интерфейсов: {len(system_info.network.network_interfaces)}")
    print(f"  Активных подключений: {len(system_info.network.connections)}")
    
    print(f"\nВремя сканирования: {system_info.timestamp}")


def main():
    """Основная функция приложения"""
    print("Запуск SysInfo Collector")
    print("="*50)
    
    try:
        # Создаем сканер и запускаем полное сканирование
        scanner = SystemScanner()
        system_info = scanner.full_scan()
        
        # Отображаем результаты
        display_system_info(system_info)
        
        # Экспортируем в JSON
        print("\nЭкспорт данных...")
        exporter = JSONExporter(system_info)
        result = exporter.export()
        
        if result['success']:
            print(f"{result['message']}")
            print(f"Файл сохранен: {result['file_path']}")
        else:
            print(f"{result['message']}")
            
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return 1
    
    print("\nПрограмма завершена успешно!")
    return 0


if __name__ == "__main__":
    exit(main())