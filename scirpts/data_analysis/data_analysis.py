import logging_module
import logging

logging_module.log_configuration()

logger = logging.getLogger('my_module')

print("Log INFO")

logger.warning("Test2")


