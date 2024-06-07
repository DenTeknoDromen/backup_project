import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename="test_logging.txt", 
                    filemode="a", encoding="UTF-8", 
                    format="%(asctime)s %(message)s", 
                    datefmt="%Y-%m-%d %H:%M")

def write_log(message):
    logging.info(message)