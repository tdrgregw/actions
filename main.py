from help_rss import *
from help_utils import *

logger = init_logging()

if __name__ == "__main__":
    SOME_SECRET = check_tokens()
    logger.info(f"Token value: {SOME_SECRET}")
    
    load_feed()
    logger.info('RSS feed updated: {0}'.format('UK Economy RSS'))
