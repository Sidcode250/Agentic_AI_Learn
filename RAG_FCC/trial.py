from dotenv import load_dotenv
load_dotenv()

import os

print("OpenAI key loaded:", bool(os.getenv("OPENAI_API_KEY")))
print("Anthropic key loaded:", bool(os.getenv("ANTHROPIC_API_KEY")))
print("Google key loaded:", bool(os.getenv("GOOGLE_API_KEY")))