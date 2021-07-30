# Instructions
______
### 1. Installing and running the application
______
(Windows) 
- Create a virtual environment
```bash
python -m venv venv
```
- Install packages
```bash
pip install -r requirements.txt
```
- Go to the desired directory (for further convenience)
```bash
cd project_ssw
```
- Create migration
```bash
python manager.py makemigrations
```
- Migration
```bash
python manager.py migrate
```
- Create superuser
```bash
python manager.py createsuperuser
```
At this stage, you can fill the db with sample data
- Application launch
```bash
python manager.py runserver
```
### 2. App Description
______
After launching the application, a single [access point.](http://127.0.0.1:8000/alias/)
The work was checked using the Postman program. All CRUD methods are available for use.
The app includes filter, search and ordering.
Below is a demonstration of the functionality of `target` search by `alias` and `end`.
```python
    def test_get_filter(self):
        url = reverse('alias-list')
        response = self.client.get(url, data={'alias': 'alias_2', 'end': self.end_alias_2})
        serializer_data = AliasSerializer(self.alias_2).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data['target'], response.data[0]['target'])
```
### 3. Testing and Reporting
______
- Running tests
```bash
python manager.py test .
```
- Generating a report
```bash
coverage run --source='.' manager.py test .
coverage html
```
To view the report, just open the file in the browser - `/project_ssw/htmlcov/index.html`
### P.S. Outcomes
______
The application is implemented, but there are places that are not pleasant for the implementation.
