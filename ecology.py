import json
import warnings
from fragmentation import suggest_fragments, warn_if_large
from storage import save_fragments  # Will add this next

# Suppress LibreSSL warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

def generate_ecology():
    """Generates 3-5 ecology fragments with chaos cat lore"""
    prompt = """
    Generate fragments about chaos cat ecosystems, including:
    - Void Nexus habitats
    - Reality bubble creation
    - Inter-breed social dynamics
    Use ===FRAGMENT_START=== format
    """
    return suggest_fragments(prompt)

# Main execution
if __name__ == "__main__":
    print("🌿 Chaos Cat Ecology:")
    fragments = generate_ecology()  # Single API call
    print(json.dumps(fragments, indent=2))
    warn_if_large(fragments)
    save_fragments(fragments)  # Coming next