import logging

logging.basicConfig(
    format="[%(name)s] [%(levelname)s] : %(message)s",
    level=logging.INFO,
)
LOGS = logging.getLogger("KuKu-DL")