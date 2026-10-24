#!/bin/bash
echo "Installing Python packages..."
pip install -r requirements.txt --quiet
echo "✅ Ready!"
echo ""
echo "Next steps:"
echo "1. export LTX_API_KEY='your_key_here'"
echo "2. python scripts/run_pipeline.py --day 1 --dry-run"
