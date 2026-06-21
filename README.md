# Task-1-Rohith-S
Repository for task 1
🤖 Rule-Based AI Chatbot | DecodeLabs Project 1


AI Industrial Training — Batch 2026 | Powered by DecodeLabs




📌 About the Project

A rule-based AI chatbot built using pure Python — no machine learning, no external libraries.

This project demonstrates how intelligent systems are built from the ground up using control flow, decision-making logic, and dictionary-based intent matching.


🧠 Concept

Before building systems that learn, an AI engineer must master systems that think in rules.

This chatbot simulates basic human interaction through:


Deterministic logic — same input always gives the same output
O(1) dictionary lookup — faster than if-elif chains (O(n))
Input sanitization — handles uppercase, lowercase, extra spaces
Continuous loop — stays alive until exit command



⚙️ How It Works (IPO Model)

INPUT → Sanitize (.lower().strip()) → PROCESS → Dictionary Lookup → OUTPUT → Response


🚀 Features


✅ Continuous while True loop (the heartbeat)
✅ Input sanitization (case & whitespace handling)
✅ 13+ intent knowledge base using Python dictionary
✅ Fallback response for unknown inputs
✅ Clean exit via exit or quit command



🛠️ Tech Stack

ToolPurposePython 3.xCore languageDictionary (HashMap)O(1) intent matchingWhile LoopContinuous interaction


▶️ Run Locally

bash# Clone the repo
git clone https://github.com/Rohith-S-AI/Task-1-Rohith S.git

# Navigate into folder
chatbot.py

# Run the chatbot
python chatbot.py


💬 Sample Interaction

=======================================================
   DecodeBot — Rule-Based AI Chatbot | DecodeLabs
=======================================================
   Type 'exit' or 'quit' to end the session.

You: hello
DecodeBot: Hey there! I'm DecodeBot. How can I help you?

You: what is ai
DecodeBot: AI is the simulation of human intelligence by machines.

You: exit
DecodeBot: Session terminated. Project 1 complete! 🚀


📚 Key Learnings


Rule-based systems are the guardrail layer in modern AI (used in NVIDIA NeMo, Llama Guard)
Dictionary lookup is O(1) vs if-elif ladder which is O(n)
Input sanitization is critical for reliable intent matching
Every LLM in production has rule-based logic wrapped around it



🗂️ Project Structure

decodelabs-ai-project1/
│
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation


👤 Author

Rohith S

ECE Final Year | Jeppiaar Engineering College, Chennai

Aspiring AI Engineer | DecodeLabs Intern — Batch 2026


🏢 About DecodeLabs

Industrial AI Training Program focused on building real-world AI projects from foundations to deployment.

🌐 www.decodelabs.tech
