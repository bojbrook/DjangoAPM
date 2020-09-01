from django.shortcuts import render
from django.http import HttpResponse
import logging
import json_log_formatter

from ddtrace import tracer
# 

# initializing logging
formatter = json_log_formatter.JSONFormatter()
json_handler = logging.FileHandler(filename='my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)
# Get an instance of a logger

# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)
@tracer.wrap()
def hello_world():
  logger.info("This is a log")
  print("Hello World")



def index(request):
  logger.info("Please inject this log")
  hello_world()
  return HttpResponse("Hello, world!!")
