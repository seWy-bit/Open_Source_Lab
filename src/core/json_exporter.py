import json
import os
from datetime import datetime


class JSONExporter:
    def __init__(self, system_info):
        self.system_info = system_info
    
    def export(self, filename=None):
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"system_info_{timestamp}.json"
        
        data = self.system_info.to_dict()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            file_path = os.path.abspath(filename)
            return {
                'success': True,
                'filename': filename,
                'file_path': file_path,
                'message': f'Данные успешно экспортированы в {filename}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': f'Ошибка при экспорте: {str(e)}'
            }
    
    def to_json_string(self):
        return json.dumps(self.system_info.to_dict(), indent=2, ensure_ascii=False)