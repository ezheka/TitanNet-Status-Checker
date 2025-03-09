import json
import time
import signal
import os
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Загружаем список ID из файла
with open("device_ids.txt", "r") as f:
    DEVICE_IDS = [line.strip() for line in f.readlines() if line.strip()]

BASE_URL = "https://test1.titannet.io/nodeidDetail"
NUM_THREADS = 5  # Количество потоков

# Флаг для остановки при Ctrl+C
stop_flag = threading.Event()

# Функция для обработки Ctrl+C
def signal_handler(sig, frame):
    print("\n🛑 Принудительное завершение... Закрываем браузеры.")
    stop_flag.set()
    exit(0)

# Перехватываем Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Загружаем старые результаты (если есть)
try:
    with open("results.json", "r", encoding="utf-8") as f:
        results = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    results = defaultdict(list)

# Функция для получения статуса устройства
def get_device_status(index, total_ids, device_id):
    if stop_flag.is_set():  # Если остановили Ctrl+C, выходим
        return None

    print(f"🔍 [{index+1}/{total_ids}] Проверяю: {device_id}")

    # Настраиваем WebDriver
    options = Options()
    options.add_argument("--headless")  # Можно закомментировать, если хочешь видеть окна
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(EdgeChromiumDriverManager().install())
    if os.name == "nt":  
        service.creationflags = 0x08000000  # Отключаем DevTools логи

    driver = webdriver.Edge(service=service, options=options)

    url = f"{BASE_URL}?device_id={device_id}"
    attempts = 3  # Количество попыток

    for attempt in range(attempts):
        if stop_flag.is_set():
            driver.quit()
            return None

        try:
            driver.get(url)
            time.sleep(3)

            node_status_block = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Node Status:')]/following-sibling::div"))
            )

            status_text = node_status_block.find_elements(By.TAG_NAME, "span")[1].text.strip()
            driver.quit()
            
            print(f"✅ [{index+1}/{total_ids}] Проверено: {device_id} → {status_text}")
            return {status_text: device_id}

        except:
            print(f"⚠️ [{index+1}/{total_ids}] Ошибка. Повтор {attempt+1}/{attempts} для {device_id}")
            time.sleep(5)

    driver.quit()
    print(f"❌ [{index+1}/{total_ids}] Не удалось получить статус для {device_id}")
    return {"Статус не найден": device_id}

# Запуск многопоточного парсинга
formatted_results = defaultdict(list)

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    future_to_id = {
        executor.submit(get_device_status, index, len(DEVICE_IDS), device_id): device_id
        for index, device_id in enumerate(DEVICE_IDS)
    }

    try:
        for future in as_completed(future_to_id):
            result = future.result()
            if result and isinstance(result, dict):
                for status, device_id in result.items():
                    formatted_results[status].append(device_id)

    except KeyboardInterrupt:
        print("\n⏳ Завершаем потоки...")
        executor.shutdown(wait=False, cancel_futures=True)

# Сохранение результатов
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(formatted_results, f, indent=4, ensure_ascii=False)

print("\n✅ Готово! Результаты сохранены в 'results.json'")
