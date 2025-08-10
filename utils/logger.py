import logging, sys
logger = logging.getLogger("c00lkidd")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(h)
    logger.propagate = False