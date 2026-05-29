import plyvel
import json
import time
from datetime import datetime


class LevelDBManager:
    def __init__(self, db_path='transliteration_db'):
        # Создаём или открываем базу данных
        self.db = plyvel.DB(db_path, create_if_missing=True)

    def save_transliteration(self, original, transliterated):
        """Сохраняет запись транслитерации с timestamp"""
        timestamp = int(time.time() * 1000)  # миллисекунды
        key = f"trans_{timestamp}"

        data = {
            'original': original,
            'transliterated': transliterated,
            'timestamp': timestamp,
            'datetime': datetime.now().isoformat()
        }

        self.db.put(key.encode('utf-8'), json.dumps(data).encode('utf-8'))

    def get_last_n_transliterations(self, n=5):
        """Получает последние N транслитераций"""
        results = []

        # Получаем все ключи и сортируем по убыванию (самые новые первыми)
        keys = [k for k in self.db.iterator(include_value=False)]
        keys.sort(reverse=True)  # сортировка по убыванию

        # Берём первые N ключей
        selected_keys = keys[:n]

        for key in selected_keys:
            value = self.db.get(key)
            if value:
                data = json.loads(value.decode('utf-8'))
                results.append(data['transliterated'])

        return results

    def close(self):
        """Закрывает соединение с базой данных"""
        self.db.close()

# Создаём глобальный экземпляр сервиса
leveldb_manager = LevelDBManager()