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
            "e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ],
        "Offline": [
            "e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ],
        "Статус не найден": [
            "e_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ]
    }
   ```

## 🛠 Требования
- **Python 3.8+**
- **Google Chrome / Microsoft Edge**
- **Selenium**
- **WebDriver Manager**
