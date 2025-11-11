"""
Пакет models - содержит модели данных для хранения системной информации
"""

from .system_info import (
    SystemInfo,
    HardwareInfo,
    SoftwareInfo,
    NetworkInfo
)

__all__ = [
    'SystemInfo',
    'HardwareInfo', 
    'SoftwareInfo',
    'NetworkInfo'
]