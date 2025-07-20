from dual_ai_test import ask_librarian
import re

def suggest_fragments(large_text: str) -> dict:
    """Improved fragment parser with format flexibility"""
    prompt = (
        "Generate exactly 3 thematic fragments from this chaos cat lore. "
        "Use this EXACT format for each fragment:\n"
        "===FRAGMENT_START===\n"
        "FRAGMENT_NAME|description\n"
        "---\n"
        "Full content...\n"
        "===FRAGMENT_END===\n\n"
        f"{large_text[:48000]}"
    )
    
    response = ask_librarian(prompt)
    fragments = {}
    
    # Extract fragments using delimiters
    fragment_blocks = re.split(r'===FRAGMENT_(?:START|END)===', response)
    for block in fragment_blocks:
        if not block.strip():
            continue
            
        # Split header from content
        parts = block.split('---', 1)
        if len(parts) == 2:
            header, content = parts
            if '|' in header:
                name = header.split('|', 1)[0].strip()
                fragments[name] = content.strip()
    
    return fragments

def warn_if_large(fragments: dict, threshold: int = 12000):
    """Prints warnings for nearing-limit fragments"""
    for name, content in fragments.items():
        size = len(content)
        if size > threshold:
            print(f"⚠️ {name}: {size} chars (>{threshold})")

# Usage: warn_if_large(fragments) after generation