import logging
import dagshub
from dotenv import load_dotenv


# Initialize DagsHub with credentials
dagshub.init(
	repo_owner='jordanmsouza',
	repo_name='mlops_project2'
)
# Load environment variables from .env file
load_dotenv()  

# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
