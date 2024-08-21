import logging
import utils

def get_logname():
    date_id = utils.get_currdate()
    date_id = date_id.split("-")
    return f"{date_id[0] + date_id[1]}_logfile.txt"

logging.basicConfig(level=logging.DEBUG,
                    filename=f"logfiles/{get_logname()}",
                    filemode="a", encoding="UTF-8",
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M")

def write_log(message):
    logging.info(message)
