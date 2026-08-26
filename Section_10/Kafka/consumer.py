from kafka import KafkaConsumer  # pyright: ignore[reportMissingModuleSource]

KAFKA_TOPIC = "demo-topic"
KAFKA_SERVER = "localhost:9092"


def consume_from_kafka():
    """Consumes messages from Kafka and processes them."""

    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )

    print("Waiting for messages...")

    for message in consumer:
        email = message.value.decode("utf-8")
        print(f"New SignUp with Email: {email}")


if __name__ == "__main__":
    consume_from_kafka()