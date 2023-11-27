# PP-LR-1-api-hello-world

## Інструкція по розгортанню проекту

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/Diancent/PP-LR-1-api-hello-world
3. Перейдіть у директорію проекту:
   ```bash
   cd назва_проекту
5. Створіть віртуальне оточення:
   ```bash
   python3 -m venv venv
7. Активуйте віртуальне оточення:
   ```bash
   source venv/bin/activate
9. Встановіть залежності:
   ```bash
   pip install -r requirements.txt
11. Запустіть додаток:
    ```bash
    gunicorn -w 4 -b 127.0.0.1:5000 app:app
12. Якщо виникають проблеми, Flask і Werkzeug несумісні. Потрібно оновити версії цих бібліотек у віртуальному середовищі:
    ```bash
    pip install --upgrade Flask Werkzeug
14. Відкрийте браузер і перейдіть за адресою:
    ```bash
    http://127.0.0.1:5005/api/v1/hello-world-10
