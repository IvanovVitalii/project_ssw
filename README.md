# Инструкция
______
### 1. Установка и запуск приложения
______
(Windows) 
- Создаем виртуальное окружение
```bash
python -m venv venv
```
- Устанавливаем пакеты
```bash
pip install -r requirements.txt
```
- Переходим в нужную директорию (для дальнейшего удобства)
```bash
cd project_ssw
```
- Сождаем миграцию
```bash
python manager.py makemigrations
```
- Миграция
```bash
python manager.py migrate
```
- Создаем superuser
```bash
python manager.py createsuperuser
```
На данном этапе можно заполнить db демонстрационными данными
- Запуск приложния
```bash
python manager.py runserver
```
### 2. Описание приложения
______
После запуска приложения доступна единая [точка доступа.](http://127.0.0.1:8000/alias/)
Проверка работы осуществлялась с помощью программы Postman. Все методы CRUD доступны к использованию.
В приложении включены filter, search и ordering.
Ниже демонстрация функционала поиска target по alias и end.
```python
    def test_get_filter(self):
        url = reverse('alias-list')
        response = self.client.get(url, data={'alias': 'alias_2', 'end': self.end_alias_2})
        serializer_data = AliasSerializer(self.alias_2).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data['target'], response.data[0]['target'])
```
### 3. Тестирование и отчет
______
- Запуск тестов
```bash
python manager.py test .
```
- Генерируем отчет
```bash
coverage run --source='.' manager.py test .
coverage html
```
Для просмота отчета достаточно открыть в браузере файл - /project_ssw/htmlcov/index.html
### P.S. Итоги 
______
Приложение реализовано, но есть места, которые не нравятся по реализация. 
В идеале спросить ментора, но на данный момент Google - единственный ментор.
