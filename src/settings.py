from pathlib import Path
import yaml

# ==========================================
# PROJECT ROOT
# ==========================================

# Obtener la raiz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================
# LOAD CONFIGURATION
# ==========================================

# Localizar config.yaml
CONFIG_PATH = PROJECT_ROOT/"config.yaml"

# cargar configuraciones
with open(CONFIG_PATH, 'r', encoding= 'utf-8') as file:
    CONFIG = yaml.safe_load(file)


# ==========================================
# PROJECT CONFIGURATION
# ==========================================

DATASET_NAME = PROJECT_ROOT / CONFIG["dataset"]["name"]
TARGET_NAME = PROJECT_ROOT / CONFIG["dataset"]["target_column"]
ROWS_EXPECTED = PROJECT_ROOT / CONFIG["dataset"]["rows_expected"]
EXPECTED_FEATURES = PROJECT_ROOT / CONFIG["dataset"]["expected_features"]

# ==========================================
# DATA DIRECTORIES
# ==========================================

PATHS = CONFIG["paths"]

RAW_DATA_DIR =  PROJECT_ROOT / PATHS["raw_data"]
STAGING_DATA_DIR =  PROJECT_ROOT / PATHS["staging_data"]
PROCESSED_DATA_DIR =  PROJECT_ROOT / PATHS["processed_data"]

# ==========================================
# RAW DATA FILES
# ==========================================
RAW_DATA_DIR = RAW_DATA_DIR / 'dataset.csv'