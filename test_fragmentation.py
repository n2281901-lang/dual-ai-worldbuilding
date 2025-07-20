from fragmentation import suggest_fragments

def validate_fragments(fragments: dict):
    """Quality checks for chaos cat fragments"""
    required_keywords = ['Chaos', 'Cat', 'Quantum', 'Void', 'probability']
    
    for name, content in fragments.items():
        # Check naming conventions
        assert '|' not in name, f"Fragment name contains invalid '|': {name}"
        assert '_' in name or name.isupper(), f"Name should be CAPITALIZED or use snake_case: {name}"
        
        # Check content
        assert 100 < len(content) < 16000, f"Fragment size out of bounds: {name} ({len(content)} chars)"
        assert any(kw in content for kw in required_keywords), f"Missing chaos cat keywords in: {name}"
    
    print(f"✅ Validated {len(fragments)} fragments")

# Test data
test_text = (
    "Chaos cats are feline entities that manipulate reality through quantum entanglement. "
    "Their primary habitat is the Void Nexus, where they weave probability strands into tangible effects. "
    "Seven known breeds exist: 1) Vortex Weavers, 2) Entropy Singers, 3) Paradox Pouncers, "
    "4) Quantum Purrers, 5) Temporal Toms, 6) Singularity Sires, and 7) Probability Matriarchs. "
    "Each breed manipulates a specific aspect of spacetime, with Matriarchs coordinating group effects." * 100
)

# Run tests
print("🧪 Testing fragmentation...")
suggestions = suggest_fragments(test_text)

print("\n[LIBRARIAN] Generated fragments:")
for name, content in suggestions.items():
    print(f"=== {name} [{len(content)} chars] ===")
    print(content[:200].replace('\n', ' ') + "...\n")

# New validation step
validate_fragments(suggestions)