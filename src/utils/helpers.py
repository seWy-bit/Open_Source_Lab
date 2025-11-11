def bytes_to_gb(bytes_value):
    """Конвертирует байты в гигабайты"""
    return round(bytes_value / (1024 ** 3), 2)

def format_timestamp(timestamp):
    """Форматирует timestamp в читаемый вид"""
    from datetime import datetime
    if isinstance(timestamp, str):
        dt = datetime.fromisoformat(timestamp)
    else:
        dt = timestamp
    return dt.strftime("%Y-%m-%d %H:%M:%S")