#!/usr/bin/python
import sys
import logging

sys.stdout = sys.stderr
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/srv/www/registro/flaskapp/")

from __init__ import app as application
