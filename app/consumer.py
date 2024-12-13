import logging

import pika
from selenium import webdriver

from settings import SETTINGS

logging.basicConfig(level=logging.INFO)


def callback(ch, method, properties, body):
    url = body.decode('utf-8')
    logging.info(f"Fetching URL: {url}")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(command_executor=f"http://{SETTINGS.SELENIUM_HOST}:4444/wd/hub", options=options)

    driver.get(url)
    html = driver.page_source
    logging.info(f"HTML: {html}")


def main():
    credentials = pika.PlainCredentials(
        f"{SETTINGS.RABBITMQ_DEFAULT_USER}",
        f"{SETTINGS.RABBITMQ_DEFAULT_PASS.get_secret_value()}"
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=f"{SETTINGS.RABBITMQ_HOST}",
            credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='browse_queue')

    channel.basic_consume(queue='browse_queue', on_message_callback=callback, auto_ack=True)

    logging.info("Waiting for messages.")
    channel.start_consuming()


if __name__ == "__main__":
    main()
