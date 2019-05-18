import sys
import logging
import traceback

from tabops.settings import DEFAULT_LOGGER, SALT_USER, SALT_PASSWORD, SALT_API_URL
from saltapi.salt_https_api import salt_api_token

logger = logging.getLogger(DEFAULT_LOGGER)

def token_id():
    s = salt_api_token(
        {
            "username": SALT_USER,
            "password": SALT_PASSWORD,
            "eauth": "pam"
        },
        SALT_API_URL + "login",
        {}
    )
    try:
        test = s.run()
    except Exception as e:
        logger.error("salt_api认证失败")
        logger.error(traceback.format_exc())
        sys.exit()
    else:
        return test["return"][0]["token"]
