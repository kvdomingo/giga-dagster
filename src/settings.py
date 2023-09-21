import os

PYTHON_ENV = os.environ.get("PYTHON_ENV", "production")

AZURE_SAS_TOKEN = os.environ.get("AZURE_SAS_TOKEN")
AZURE_BLOB_SAS_HOST = os.environ.get("AZURE_BLOB_SAS_HOST")
AZURE_BLOB_CONTAINER_NAME = os.environ.get("AZURE_BLOB_CONTAINER_NAME")

AZURE_STORAGE_USE_EMULATOR = PYTHON_ENV == "production"
