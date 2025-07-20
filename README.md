# Dual-AI Storytelling System

## For Developers
```mermaid
graph TD
    User -->|Query| Librarian
    Librarian -->|Fragments| Session
    Session -->|Output| User

Key Files
dual_ai_test.py: API handler

fragmentation.py: Splits lore into chunks

ecology.py: Chaos cat demo

Setup
pip install python-dotenv requests tiktoken
echo "API_KEY=your_key" > .env
python3 ecology.py

