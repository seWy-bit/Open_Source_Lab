from src.core.system_manager import SystemManager
from src.core.exporters import JSONExporter, XMLExporter


def display_system_info(system_info):
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
    print(f"  Хостнейм: {system_info.software.os_info['hostname']}")
    print(f"  Установленных программ: {len(system_info.software.installed_software)}")
    
    # Сетевые настройки
    print("\nСЕТЕВЫЕ НАСТРОЙКИ:")
    print(f"  Сетевых интерфейсов: {len(system_info.network.network_interfaces)}")
    print(f"  Активных подключений: {len(system_info.network.connections)}")
    
    print(f"\nВремя сканирования: {system_info.timestamp}")


def export_data(system_info, format_type='json'):
    if format_type.lower() == 'json':
        exporter = JSONExporter(system_info)
        file_extension = 'json'
    elif format_type.lower() == 'xml':
        exporter = XMLExporter(system_info)
        file_extension = 'xml'
    else:
        print(f"Неподдерживаемый формат: {format_type}")
        return None
    
    print(f"\nЭкспорт данных в {format_type.upper()}...")
    result = exporter.export()
    
    if result['success']:
        print(f"{result['message']}")
        print(f"Файл сохранен: {result['file_path']}")
    else:
        print(f"{result['message']}")
    
    return result


def main():
    print(" Запуск SysInfo Collector")
    print("="*50)
    
    try:
        # Создаем системный менеджер и запускаем полное сканирование
        manager = SystemManager()
        system_info = manager.full_scan()
        
        # Отображаем результаты
        display_system_info(system_info)
        
        # Экспортируем в JSON
        json_result = export_data(system_info, 'json')
        
        # Экспортируем в XML
        xml_result = export_data(system_info, 'xml')
            
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return 1
    
    print("\nПрограмма завершена успешно!")
    return 0


if __name__ == "__main__":
    exit(main())