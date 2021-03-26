# Import Standard Modules
import os
import json
import logging

# Load Logging Configuration
if os.path.exists('logging_configuration.json'):

    logging.basicConfig(filename='logging_configuration.json', level=logging.INFO)