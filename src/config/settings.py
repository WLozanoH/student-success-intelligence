from pathlib import Path
import yaml

# ==========================================
# PROJECT ROOT
# ==========================================

# Obtener la raiz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parents[2]

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

DATASET_NAME = CONFIG["dataset"]["name"]
TARGET_COLUMN = CONFIG["dataset"]["target_column"]
EXPECTED_ROWS = CONFIG["dataset"]["expected_rows"]
EXPECTED_COLUMNS = CONFIG["dataset"]["expected_columns"]

# ==========================================
# DATA DIRECTORIES
# ==========================================

PATHS = CONFIG["paths"]

RAW_DATA_DIR =  PROJECT_ROOT / PATHS["raw_data"]
STAGING_DATA_DIR =  PROJECT_ROOT / PATHS["staging_data"]
PROCESSED_DATA_DIR =  PROJECT_ROOT / PATHS["processed_data"]

MODELS_DATA_DIR = PROJECT_ROOT / PATHS["models"]
NOTEBOOKS_DATA_DIR = PROJECT_ROOT / PATHS["notebooks"]
DOCS_DATA_DIR = PROJECT_ROOT / PATHS["docs"]
FIGURES_DATA_DIR = PROJECT_ROOT / PATHS["figures"]
LOGS_DATA_DIR = PROJECT_ROOT / PATHS["logs"]

# ==========================================
# RAW DATA FILES
# ==========================================
RAW_DATA_FILE = RAW_DATA_DIR / 'dataset.csv'