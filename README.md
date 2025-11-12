# 🖥️ SysInfo Collector

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**SysInfo Collector** — это мощная программа для автоматизированного сбора и анализа системной информации с локального компьютера. Разработана для системных администраторов, разработчиков и технических специалистов.

## ✨ Возможности

### 🔍 Сбор информации
- **Аппаратное обеспечение** — процессор, память, диски, графические карты
- **Программное обеспечение** — ОС, установленные приложения, версии
- **Сетевые настройки** — интерфейсы, активные подключения, конфигурации

### 💾 Экспорт данных
- **JSON** — структурированный формат для анализа
- **XML** — стандартизированный формат для интеграций
- **Автоматическое именование** файлов с временными метками

### 🎯 Особенности
- 🚀 **Быстрое сканирование** — полный анализ за секунды
- 🛡️ **Безопасность** — работа без прав администратора
- 📊 **Структурированные данные** — удобный формат для обработки
- 🔧 **Модульная архитектура** — легко расширяемый код

## 🏗️ Архитектура проекта
```plaintext
sysinfo-collector/
├── src/
│ ├── core/ # 🎯 Ядро приложения
│ │ ├── scanners/ # 🔍 Сканеры данных
│ │ │ ├── hardware_scanner.py
│ │ │ ├── software_scanner.py
│ │ │ └── network_scanner.py
│ │ ├── exporters/ # 💾 Экспортеры
│ │ │ ├── json_exporter.py
│ │ │ └── xml_exporter.py
│ │ └── system_manager.py # 🎮 Управляющий класс
│ ├── models/ # 📊 Модели данных
│ │ └── system_info.py
│ └── utils/ # 🛠️ Вспомогательные утилиты
│ └── helpers.py
├── main.py # 🚀 Точка входа
├── requirements.txt # 📦 Зависимости
└── README.md
```

## 🔧 Использование в коде
 
### Базовое использование
```python
from src.core.system_manager import SystemManager
from src.core.exporters import JSONExporter, XMLExporter

# Создаем менеджер и запускаем сканирование
manager = SystemManager()
system_info = manager.full_scan()

# Экспортируем данные
json_exporter = JSONExporter(system_info)
json_exporter.export("my_system_info.json")

xml_exporter = XMLExporter(system_info) 
xml_exporter.export("my_system_info.xml")
```
### Выборочное сканирование
```python
# Только аппаратное обеспечение
hardware_only = manager.scan_hardware()

# Выборочное сканирование
selective = manager.selective_scan(
    scan_hardware=True,
    scan_software=False, 
    scan_network=True
)
```

## 🛠️ Разработка

### Установка для разработки
```bash
git clone https://github.com/seWy-bit/Open_Source_Lab
cd sysinfo-collector
pip install psutil
```

### Планы по развитию
-**GUI интерфейс**

-**Поддержка Linux и macOS**

-**CSV экспорт**

-**Сетевое сканирование**

-**Плагины и расширения**
