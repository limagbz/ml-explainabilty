"""Downloads the PhiUSIIL Phishing URL (Website) from UCI Repository."""

import json
import logging
import logging.config
import sys
from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo

logging.config.fileConfig(".logger.conf")
logger = logging.getLogger(__name__)

DATASET_NAME = "PhiUSIIL Phishing URL (Website)"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = PROJECT_ROOT / Path("data/raw/phishing")
REFERENCES_DIR = PROJECT_ROOT / Path("references")
DATASET_PATH = DOWNLOAD_DIR / "PhishingURLPhiUSIIL.csv"
VARIABLES_PATH = REFERENCES_DIR / "VARIABLES_PhishingURLPhiUSIIL.csv"
METADATA_PATH = REFERENCES_DIR / "METADATA_PhishingURLPhiUSIIL.json"

if __name__ == "__main__":
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    if DATASET_PATH.exists():
        logger.warning("Dataset %s already downloaded! Skipping...", DATASET_NAME)
        sys.exit()

    try:
        logger.info("Downloading %s on %s...", DATASET_NAME, DOWNLOAD_DIR)
        downloaded_data = fetch_ucirepo(name="PhiUSIIL Phishing URL (Website)")
    except Exception as e:  # noqa: BLE001
        logger.error("Error downloading dataset! %s", e)

    df = pd.DataFrame(downloaded_data.data.features)
    df.insert(len(df.columns), "TargetIsPhishing", downloaded_data.data.targets)
    df.to_csv(DATASET_PATH, index=False)

    var_df = pd.DataFrame(downloaded_data.variables)
    var_df.to_csv(VARIABLES_PATH, index=False)

    with Path.open(METADATA_PATH, "w") as file:
        json.dump(downloaded_data.metadata, file, indent=4, sort_keys=True)
