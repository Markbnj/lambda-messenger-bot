import handlers
import inspect
import json
import logging
import os
import sys


"""
Set up the logger.
TBD: Should move the level to a stage variable.
"""
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


"""
All code has to be relative to the root directory of the lambda function entry
point, and there can only be one file in the root path, so in order to make
modules located in subdirectories importable we make the top folder the first
entry in sys.path.
"""
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(0, current_dir)


"""
Read in the three secrets from config/tokens.json.
"""
settings = None
config_path = os.path.join(current_dir, "config")
with open("{}/settings.json".format(config_path), "rb") as f:
    settings = json.loads(f.read())


def handler(event, context):
    """
    Called for all requests against the attached API gateway
    endpoint. Expects the request data to be mapped to a json event
    record as defined by aws/api-gateway/request-mapping.json.
    """
    logger.debug("AWS request context: {}".format(context))
    my_access_token = settings.get("accessToken")
    access_token = event.get("accessToken")
    if not access_token:
        logger.debug("Missing access token")
        raise Exception("400 Bad Request; missing access token")
    if access_token != my_access_token:
        logger.debug("Access token check failed")
        raise Exception("403 Forbidden; bad access token")
    else:
        return handlers.dispatch(event, settings)

