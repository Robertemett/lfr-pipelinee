# Little Friends Rhymes – YouTube Shorts Pipeline (LTX 2.5)

Full end-to-end automation for the 30-day “JJ + Friends” nursery-rhyme Shorts.

**Supports multi-clip generation + automatic stitching → full ~40s Shorts.**

---

## Run from your phone with GitHub Codespaces

### Step-by-step (Android)

1. **Create a GitHub repo** (if you don’t have one yet)
   - Go to [github.com/new](https://github.com/new) on your phone
   - Name it `lfr-pipeline` → Create repository

2. **Upload this project**
   - On your computer (or using the GitHub mobile web):
     - Upload the whole `lfr_pipeline` folder
     - Or push it with git

3. **Open in Codespaces**
   - Open your repository on GitHub
   - Tap the green **Code** button
   - Switch to the **Codespaces** tab
   - Tap **Create codespace on main**
   - Wait 1–2 minutes (it installs Python + FFmpeg automatically)

4. **Set your LTX key**
   Inside the Codespace terminal type:
   ```bash
   export LTX_API_KEY="your_key_here"
   ```

5. **Generate a video**
   ```bash
   # Preview prompts (free)
   python scripts/run_pipeline.py --day 1 --dry-run

   # Full ~40s multi-clip Short
   python scripts/run_pipeline.py --day 1

   # Single short clip (cheaper test)
   python scripts/run_pipeline.py --day 1 --single-clip --duration 10
   ```

6. **Download the result**
   - In the left file explorer open `output/day_01/`
   - Long-press `video_ltx.mp4` → Download
   - Same for `thumbnail.png`

---

## Commands cheat-sheet

| Command | What it does |
|---------|--------------|
| `python scripts/run_pipeline.py --day 1 --dry-run` | Show the 4 prompts (no cost) |
| `python scripts/run_pipeline.py --day 1` | Full ~40s multi-clip Short |
| `python scripts/run_pipeline.py --day 1 --single-clip` | One short clip only |
| `python scripts/run_pipeline.py --from 1 --to 3` | Generate days 1–3 |
| `python scripts/run_pipeline.py --day 5 --model ltx-2-5-pro` | Higher quality model |

---

## Multi-clip structure (default)

| Segment | Duration | Content |
|---------|----------|---------|
| hook    | 8 s      | Opening |
| main_a  | 12 s     | First half of the dance |
| main_b  | 12 s     | Second half + teaching |
| finale  | 10 s     | Happy ending |

After crossfades ≈ **38–40 seconds**.

---

## Project structure

```
lfr_pipeline/
├── data/content_calendar.json   ← 30 days content
├── scripts/run_pipeline.py      ← main command
├── utils/
│   ├── ltx_client.py            ← LTX 2.5 + stitching
│   ├── tts.py
│   └── thumbnail.py
├── output/                      ← finished videos appear here
└── .devcontainer/               ← Codespaces config
```

---

## Tips for phone use

- Keep the Codespace open in a browser tab
- Use landscape mode for easier typing
- Download videos to your Gallery, then upload to YouTube Shorts app
- Free Codespaces hours are usually enough for testing several days

---

## Cost note

LTX charges per second of generated video.  
Start with `--single-clip --duration 8` to test cheaply before running full multi-clip days.
