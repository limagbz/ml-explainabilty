"""Downloads the Ames Housing Dataset from Kaggle.

For this script to run properly you should provide a KAGGLE_API_TOKEN in a .env file. See
[How to use Kaggle (Public API)](https://www.kaggle.com/docs/api) for how to setup
an API Token.
"""

import logging
import logging.config
from pathlib import Path

import kagglehub
from dotenv import load_dotenv

logging.config.fileConfig(".logger.conf")
logger = logging.getLogger(__name__)
load_dotenv()

DATASET_NAME = "shashanknecrothapa/ames-housing-dataset"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = PROJECT_ROOT / Path("data/raw/housing")

if __name__ == "__main__":
    try:
        logger.info("Downloading %s on %s...", DATASET_NAME, DOWNLOAD_DIR)
        path = kagglehub.dataset_download(
            handle=DATASET_NAME, output_dir=str(DOWNLOAD_DIR)
        )
        logger.info("Dataset %s downloaded successfully!", DATASET_NAME)
    except FileExistsError:
        logger.warning("Dataset %s already downloaded! Skipping...", DATASET_NAME)
    except Exception as e:  # noqa: BLE001
        logger.error("Error downloading dataset! %s", e)
