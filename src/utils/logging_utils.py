import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {"level": record.levelname, "message": record.getMessage(), "time": self.formatTime(record)}
        return json.dumps(log_obj)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ])

logger = logging.getLogger(__name__)

