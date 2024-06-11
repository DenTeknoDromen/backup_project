import logging
import utils

date_id = utils.get_currdate()
date_id = date_id.split("-")
date_id = date_id[0] + date_id[1]

logging.basicConfig(level=logging.DEBUG,
                    filename=f"logfiles/{date_id}_logfile.txt",
                    filemode="a", encoding="UTF-8",
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M")


def write_log(message):
    logging.info(message)
