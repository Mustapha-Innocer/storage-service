import asyncio
import json
import traceback

from lib.db.session import get_db
from lib.kafka.consumer import consumer
from lib.logging.logger import LOGGER
from lib.service import save
from lib.config.config import KAFKA_CONSUMER_TOPIC


async def heartbeat():
    while True:
        LOGGER.info("Heartbeat received ...")
        await asyncio.sleep(5)


async def consume():
    consumer.subscribe([KAFKA_CONSUMER_TOPIC])
    db = next(get_db())
    while True:
        try:
            msg = consumer.poll(5)

            if msg is None:
                LOGGER.info("No new message in the queue")
                await asyncio.sleep(30)
                continue

            if msg.error():
                LOGGER.error(f"Consumer error: {msg.error()}")
                continue

            data = json.loads(msg.value().decode("utf-8"))
            LOGGER.info(f"Received new strory: {data["url"]}")
            save(db, data)
            consumer.commit()
        except Exception:
            LOGGER.error(f"Unable to save {data["url"]}")
            traceback.print_exc()
            await asyncio.sleep(30)


async def main():
    await asyncio.gather(heartbeat(), consume())


if __name__ == "__main__":
    LOGGER.info(f"{'*' * 10} Starting Storage Service {'*' * 10}")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LOGGER.info(f"{'*' * 10} Storage Service closed {'*' * 10}")
