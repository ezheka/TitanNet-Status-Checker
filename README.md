# 🚗 TitanNet Status Checker

Этот скрипт парсит статусы устройств по `device_id` с сайта **TitanNet** и сохраняет их в `results.json`.  
Поддерживает **многопоточность** и корректно завершается при `Ctrl + C`.

## 📥 Установка

1. **Скачайте репозиторий** или создайте проект.

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt


## 🚀 Использование
1. **Добавьте список device_id** в device_ids.txt, каждый с новой строки.
   ```txt
   e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

2. **Запустите скрипт**:
   ```txt
   python main.py

3. **Ожидайте завершения.** В консоли появятся логи:
   ```txt
   🔍 [1/10] Проверяю: e_863d2b23-aeda-4e1a-b8ab-166583be43f6
   ✅ [1/10] Проверено: e_863d2b23-aeda-4e1a-b8ab-166583be43f6 → Online


## ⏹ Остановка скрипта

Если нужно **остановить выполнение**, нажмите `Ctrl + C`.  

Скрипт **корректно сохранит текущие результаты**.

## 📄 Формат results.json
   ```json
    {
        "Online": [
            "e_863d2b23-aeda-4e1a-b8ab-166583be43f6",
            "e_091e71ca-947d-4442-92b4-b7052056ea1d"
        ],
        "Offline": [
            "e_396aa29c-545d-4df7-a8b8-b529cebdc504"
        ],
        "Статус не найден": [
            "e_2b20b879-9ec2-428b-b46d-6e4347fff65e"
        ]
    }
   ```

## 🛠 Требования
- **Python 3.8+**
- **Google Chrome / Microsoft Edge**
- **Selenium**
- **WebDriver Manager**
