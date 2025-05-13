# GitHub Multi-Account Automation

Этот проект содержит два Python-скрипта — `stars.py` и `follow.py`, которые позволяют ставить звёзды на репозитории и подписываться на пользователей GitHub от имени **нескольких аккаунтов**, используя личные API токены.

## Описание скриптов

### `stars.py`
Ставит звезду (★) на указанный GitHub-репозиторий от каждого аккаунта, токен которого добавлен в `api.txt`.

- Вводите URL репозитория вручную.
- Скрипт автоматически извлекает `owner` и `repo`.
- Проверяет валидность каждого токена.
- Отправляет PUT-запрос на установку звезды.
- Добавляет паузы между запросами и обрабатывает превышение лимитов API.

### `follow.py`
Подписывается на заданного пользователя GitHub от имени всех токенов, указанных в `api.txt`.

- Имя пользователя задаётся в переменной `USERNAME` внутри скрипта.
- Проверяется валидность токенов.
- Отправляется PUT-запрос на подписку.
- Поддерживает задержки и повтор в случае превышения лимита.

## Как использовать

1. **Создайте файл `api.txt`** в корне проекта.
2. Вставьте в него **по одному GitHub API токену на строку**. Например:
    ```
    ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ghp_yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    ```
3. Убедитесь, что у токенов есть права на `public_repo` и `user:follow`.
4. Установите зависимости:
    ```bash
    pip install requests
    ```

### Запуск

**Поставить звезду:**
```bash
python stars.py
```
**Подписаться**
```bash
python follow.py
```


# Подписывайте:
[![Instagram](https://img.shields.io/badge/INSTAGRAM-FOLLOW-red?style=for-the-badge&logo=instagram)](https://instagram.com/cs.mer6)
[![Instagram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/Networking_Security)
<a href="https://youtube.com/@nukotz?si=1Z6uz0wO2NpOeJUY"><img title="YouTube" src="https://img.shields.io/badge/YouTube-Channel-red?style=for-the-badge&logo=Youtube"></a>
