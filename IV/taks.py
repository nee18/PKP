import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)s-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()

class EventHandler(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_item_produced(self, item):
        logging.info('Item produced: {}'.format(item))

    def on_item_consumed(self, item):
        logging.info('Item consumed: {}'.format(item))
    
    def run(self):
        while True:
            with condition:
                condition.wait()
                if items:
                    item = items.pop()
                    self.on_item_consumed(item)
                else:
                    self.on_item_produced(item)

class Consumer(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()

            items.pop()
            logging.info('consumed 1 item')

            condition.notify()

    def run(self):
        for i in range(30):
            time.sleep(0.5)
            self.consume()


class Producer(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 10:
                logging.info('items produced {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total items {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(30):
            time.sleep(0.5)
            self.produce()

def main():
    eventhandler = EventHandler(name='Event')
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    eventhandler.start()
    producer.start()
    consumer.start()
    
    eventhandler.join()
    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
