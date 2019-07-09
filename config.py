import os
from log import init_log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = BASE_DIR + '/evil_dns.log'
logger = init_log(LOG_FILE)

REBIND_DOMAIN = ['rebind.com']
FAKE_DOMAIN = {'test.com': "202.112.111.111"}
