import os
import xml.etree.ElementTree as ET
from datetime import datetime


class XMLExporter:
    def __init__(self, system_info):
        self.system_info = system_info
    
    def _dict_to_xml(self, parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key.replace(' ', '_'))
                self._dict_to_xml(child, value)
        elif isinstance(data, list):
            for item in data:
                child = ET.SubElement(parent, 'item')
                self._dict_to_xml(child, item)
        else:
            parent.text = str(data)
    
    def export(self, filename=None):
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"system_info_{timestamp}.xml"
        
        try:
            root = ET.Element("SystemInfo")

            system_data = self.system_info.to_dict()
            self._dict_to_xml(root, system_data)
            
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            
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
    
    def to_string(self):
        root = ET.Element("SystemInfo")
        system_data = self.system_info.to_dict()
        self._dict_to_xml(root, system_data)
        
        self._indent(root)
        return ET.tostring(root, encoding='utf-8').decode('utf-8')
    
    def _indent(self, elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i