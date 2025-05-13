import requests
import time
import random

TOKENS_FILE = "api.txt"

repo_url = input("Введите URL репозитория (например, https://github.com/s4evers/termux-packages): ").strip()

# Получаем owner и repo из URL
try:
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    API_URL = f"https://api.github.com/user/starred/{owner}/{repo}"
except IndexError:
    print("❌ Некорректный URL!")
    exit()

# Читаем токены
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
        print(f"⭐ Звезда поставлена с токеном {token[:10]}...")
    elif response.status_code == 403 and "rate limit exceeded" in response.text:
        print("⏳ Превышен лимит API, ждём 1 минуту...")
        time.sleep(60)
    else:
        print(f"❌ Ошибка {response.status_code} ({token[:10]}): {response.text}")

    # Пауза для избежания блокировки
    time.sleep(random.uniform(1, 3))
