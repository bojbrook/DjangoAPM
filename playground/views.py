from django.shortcuts import render
from django.http import HttpResponse
import logging
# from pythonjsonlogger import jsonlogger

# initializing logging
# formatter = json_log_formatter.JSONFormatter()
# json_handler = logging.FileHandler(filename='/var/log/my-log.json')
# json_handler.setFormatter(formatter)
# Get an instance of a logger

# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)



def index(request):
  return HttpResponse("Hello, world!!")