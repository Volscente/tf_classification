# Import Standard Modules
import os
import json
import logging

# Import Configuration
from configuration.configuration import logging_configuration_file


def log_configuration():

    try:

        print("Import Logging Configuration")

        logging.config.fileConfig(logging_configuration_file)

    except Exception as e:

        print(e)
