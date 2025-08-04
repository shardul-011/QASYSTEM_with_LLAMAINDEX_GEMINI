import os
import logging
from datetime import datetime

# Configure logging
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
    