#!/home/ubuntu/miniconda3/envs/flask_website/bin
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/flask_website/flask_website/")

from app import app as application
application.secret_key = 'yoyobuntay'
