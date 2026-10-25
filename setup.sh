#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

printf '\n✅ Environment ready.\n'
printf 'Run the demo with:\n'
printf '  python scripts/run_pipeline.py --day 1 --dry-run\n'
printf '\nSet your API key before generating real output:\n'
printf '  export LTX_API_KEY="your_key_here"\n'
