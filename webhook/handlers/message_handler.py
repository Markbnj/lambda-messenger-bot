from config import settings
import logging
from platform import profiles


logger = logging.getLogger()


def received(page_id, time, envelope):
    """
    Processes a single received message.
    Params:
        page_id: the page id, corresponds to $.entry[i].id in the callback data
        time: the update time, corresponds to $.entry[i].time in the callback data
        envelope: the message content container, $.entry[i].messaging[i] in the callback data
        settings: contains the page token in "pageToken"
    """
    logger.debug("Message recv: page_id: {}, time: {}, envelope: {}".format(page_id, time, envelope))
    profile = profiles.get(envelope["sender"]["id"])
    logger.debug("Hello {}".format(profile["first_name"]))


def delivered(page_id, time, receipt):
    """
    Processes a single message delivery receipt (callback)
    Params:
        page_id: the page id, corresponds to $.entry[i].id in the callback data
        time: the update time, corresponds to $.entry[i].time in the callback data
        receipt: the delivery receipt, $.entry[i].messaging[i] in the callback data
        settings: contains the page token in "pageToken"
    """
    logger.debug("Message delivered: page_id: {}, time: {}, receipt: {}".format(page_id, time, receipt))