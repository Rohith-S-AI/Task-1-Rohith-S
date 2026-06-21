# ============================================================
# DecodeLabs - AI Industrial Training | Batch 2026
# Project 1: Rule-Based AI Chatbot
# Author: Rohi
# ============================================================

# ── KNOWLEDGE BASE (Dictionary - O(1) lookup) ──────────────
responses = {
    "hello":        "Hey there! I'm DecodeBot. How can I help you?",
    "hi":           "Hi! Great to see you. What's on your mind?",
    "hey":          "Hey! What can I do for you today?",
    "how are you":  "I'm running at 100% efficiency! Thanks for asking.",
    "what is ai":   "AI is the simulation of human intelligence by machines — enabling them to learn, reason, and solve problems.",
    "what is ml":   "Machine Learning is a subset of AI where systems learn patterns from data without being explicitly programmed.",
    "who made you": "I was built by Rohi as part of DecodeLabs AI Internship - Project 1.",
    "what can you do": "I can answer basic questions, greet you, and demonstrate rule-based logic. More skills coming in future projects!",
    "help":         "You can ask me: 'what is ai', 'what is ml', 'how are you', 'who made you', or just say hello!",
    "bye":          "Goodbye! Keep building. See you in Project 2!",
    "goodbye":      "Goodbye! Keep building. See you in Project 2!",
    "thanks":       "You're welcome! Always here to help.",
    "thank you":    "Happy to help! Keep up the great work.",
}

# ── PHASE 1: INPUT SANITIZATION ────────────────────────────
def sanitize(raw_input):
    """Normalize input: lowercase + strip whitespace."""
    return raw_input.lower().strip()

# ── PHASE 2: PROCESS (Intent Matching) ─────────────────────
def get_response(clean_input):
    """Look up response from knowledge base with O(1) dict lookup.
    Falls back to default if intent not found."""
    return responses.get(clean_input, "I don't understand that yet. Try asking 'help' to see what I can do!")

# ── PHASE 3: MAIN LOOP (The Heartbeat) ─────────────────────
def run_chatbot():
    print("=" * 55)
    print("   DecodeBot — Rule-Based AI Chatbot | DecodeLabs")
    print("=" * 55)
    print("   Type 'exit' or 'quit' to end the session.\n")

    while True:
        # Get raw input
        raw_input = input("You: ")

        # Sanitize
        clean_input = sanitize(raw_input)

        # EXIT STRATEGY — Kill command
        if clean_input in ("exit", "quit"):
            print("DecodeBot: Session terminated. Project 1 complete! 🚀")
            break

        # Get and print response
        reply = get_response(clean_input)
        print(f"DecodeBot: {reply}\n")

# ── ENTRY POINT ─────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
