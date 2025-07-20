# storage.py
import json
from datetime import datetime

def save_fragments(fragments: dict, prefix: str = "chaos"):
    """Saves fragments to a timestamped JSON file"""
    filename = f"{prefix}_fragments_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(filename, 'w') as f:
        json.dump(fragments, f, indent=2)
    print(f"💾 Saved to {filename}")
    