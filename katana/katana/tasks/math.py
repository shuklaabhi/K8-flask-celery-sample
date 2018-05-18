import logging
from katana import celery

logger = logging.getLogger(__name__)

@celery.task
def add(x, y):
    sum = x + y
    logger.info("{x} + {y} = {sum}".format(x=x, y=y, sum=sum))
    return sum
