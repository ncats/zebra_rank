from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class ZrConfig(AppConfig):
    name = 'zr'

    def ready(self):
        logger.debug('#### %s ready...' % (self.name))
