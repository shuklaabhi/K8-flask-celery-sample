import logging
import os

from flask.cli import cli

from katana import app

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    os.environ['FLASK_APP'] = __file__
    cli()
