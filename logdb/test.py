import logging
import graypy

graylog_server = os.environ.get("LOG_SERVER","127.0.0.1")
graylog_port = os.environ.get("LOG_PORT","12201")

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler(graylog_server, graylog_port)
my_logger.addHandler(handler)

my_logger.debug('This is a test from a Python script!')