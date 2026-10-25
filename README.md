{
  "name": "lfr-pipeline",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/ffmpeg:1": {}
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/python/current/bin/python"
      }
    }
  }
}
