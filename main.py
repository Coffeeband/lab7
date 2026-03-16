import logging
import time
import random

# 1. Налаштування логування (Частина 2, пункт 1-2)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def search_projects():
    # Логування основної дії (Частина 2, пункт 2)
    logger.info("SmartHunt: Пошук нових проєктів на біржах...")
    time.sleep(1)

    # Імітація знахідки
    if random.choice([True, False]):
        logger.info("Знайдено новий проєкт: 'Розробка Telegram-бота'")
    else:
        logger.warning("Наразі нових проєктів не знайдено.")


def main():
    # Повідомлення про запуск (Частина 2, пункт 2)
    logger.info("Програма SmartHunt запущена (Release v1.0)")

    try:
        search_projects()
    except Exception as e:
        # Логування помилки (Частина 2, пункт 2)
        logger.error(f"Виникла помилка: {e}")
    finally:
        logger.info("Програма завершила роботу.")


if __name__ == "__main__":
    main()