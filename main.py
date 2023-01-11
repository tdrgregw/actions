from help_rss import *
from help_utils import *

logger = init_logging()

if __name__ == "__main__":
    _snake_case = check_tokens()
    logger.info("Token value: %s", _snake_case)
    load_feed()
    logger.info('RSS feed updated UK Economy RSS')
