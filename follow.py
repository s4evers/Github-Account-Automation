import requests
import time
import random

USERNAME = "s4evers"
TOKENS_FILE = "api.txt"
API_URL = f"https://api.github.com/user/following/{USERNAME}"

# Читаем токены из файла
with open(TOKENS_FILE, "r") as file:
    tokens = [line.strip() for line in file.readlines() if line.strip()]

for token in tokens:
    headers = {"Authorization": f"token {token}"}
    
    # Проверяем токен перед использованием
    user_check = requests.get("https://api.github.com/user", headers=headers)
    if user_check.status_code != 200:
        print(f"🚫 Токен {token[:10]} невалиден!")
        continue  # Пропускаем этот токен
    
    response = requests.put(API_URL, headers=headers)
    
    if response.status_code == 204:
        print(f"✅ Успешно подписались с токеном {token[:10]}...")
    elif response.status_code == 403 and "rate limit exceeded" in response.text:
        print("⏳ Превышен лимит API, ждём 1 минуту...")
        time.sleep(60)
    else:
        print(f"❌ Ошибка {response.status_code} ({token[:10]}): {response.text}")
    
    # Пауза для избежания блокировки
    time.sleep(random.uniform(1, 3))
