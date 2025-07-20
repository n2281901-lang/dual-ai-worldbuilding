import os  
import requests  
from dotenv import load_dotenv  
# Add this to the top of your file
import sys

# Add to top of file
TOTAL_CONTEXT = 128000
SEED_ALLOWANCE = TOTAL_CONTEXT // 2  # 64K
THRESHOLDS = {
    "LOW": SEED_ALLOWANCE // 4,      # 16K (25%)
    "MEDIUM": SEED_ALLOWANCE // 2,   # 32K (50%)
    "HIGH": SEED_ALLOWANCE * 3 // 4, # 48K (75%)
    "MAX": SEED_ALLOWANCE            # 64K (100%)
}

def check_seed_usage(frag_tokens: int) -> str:
    """Returns warning message based on seed usage percentage"""
    if frag_tokens >= THRESHOLDS["MAX"]:
        return "🛑 CRITICAL: Seed size reached 100% of allocation. Fragmentation required immediately!"
    elif frag_tokens >= THRESHOLDS["HIGH"]:
        return "⚠️ WARNING: Seed size at 75% of allocation. Consider fragmentation soon."
    elif frag_tokens >= THRESHOLDS["MEDIUM"]:
        return "⚠️ WARNING: Seed size at 50% of allocation."
    elif frag_tokens >= THRESHOLDS["LOW"]:
        return "⚠️ WARNING: Seed size at 25% of allocation."
    return ""

def safe_count_tokens(text: str) -> int:
    """Count tokens with fallback to word count"""
    try:
        import tiktoken
        encoder = tiktoken.get_encoding("cl100k_base")
        return len(encoder.encode(text))
    except ImportError:
        # Fallback: 1 token ≈ 4 characters
        return len(text) // 4

# Load API key from .env  
load_dotenv()  
API_KEY = os.getenv("API_KEY")  

def ask_librarian(query):
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are LIBRARIAN_AI..."},
                {"role": "user", "content": query}
            ]
        }
    )
    print("RAW API RESPONSE:", response.text)  # <-- ADD THIS LINE
    return response.json()["choices"][0]["message"]["content"]  

def ask_session_ai(fragments, prompt):  
    # Token counting
    frag_tokens = safe_count_tokens(fragments)
    prompt_tokens = safe_count_tokens(prompt)
    
    # --- NEW THRESHOLD CHECK SYSTEM ---
    # Get warning message based on seed size
    seed_warning = check_seed_usage(frag_tokens)
    if seed_warning:
        print(seed_warning)
    
    # Block execution if at maximum capacity
    if frag_tokens >= THRESHOLDS["MAX"]:
        return "SESSION BLOCKED: Seed exceeds maximum allocation. Please consult Librarian for fragmentation."
    # --- END OF NEW SYSTEM ---
    
    # Original API call remains unchanged
    response = requests.post(  
        "https://api.deepseek.com/v1/chat/completions",  
        headers={"Authorization": f"Bearer {API_KEY}"},  
        json={  
            "model": "deepseek-chat",  
            "messages": [  
                {"role": "system", "content": fragments},  
                {"role": "user", "content": prompt}  
            ]  
        }  
    )
    return response.json()["choices"][0]["message"]["content"]

# --- TEST DRIVE YOUR DUAL AI SYSTEM --- #  
if __name__ == "__main__":  
    # 1. Librarian suggests fragments  
    lore_query = "Need fragments for a scene about chaos energy cats"  
    fragments = ask_librarian(lore_query)  
    print(f"\n🔵 LIBRARIAN SUGGESTS:\n{fragments}\n")  

    # 2. Session AI writes using those fragments  
    creative_prompt = "Write a 3-sentence scene about 7 chaos cats manipulating reality bubbles"  
    story = ask_session_ai(fragments, creative_prompt)  
    print(f"🟢 SESSION AI WRITES:\n{story}")  

    # SAFER TOKEN COUNTER IMPLEMENTATION
import os
import requests
from dotenv import load_dotenv

try:
    import tiktoken
    TOKEN_COUNTING_ENABLED = True
except ImportError:
    TOKEN_COUNTING_ENABLED = False
    print("⚠️ tiktoken not installed - token counting disabled")

# ... [rest of your existing setup] ...

def ask_session_ai(fragments, prompt):
    # --- NEW TOKEN AWARENESS (SAFE) ---
    if TOKEN_COUNTING_ENABLED:
        try:
            encoder = tiktoken.get_encoding("cl100k_base")
            frag_tokens = len(encoder.encode(fragments))
            prompt_tokens = len(encoder.encode(prompt))
            print(f"🔍 Tokens: Frag={frag_tokens} + Prompt={prompt_tokens} = {frag_tokens+prompt_tokens}")
        except Exception as e:
            print(f"⚠️ Token counting error: {str(e)}")
    
    # ... [your original API call remains unchanged] ...