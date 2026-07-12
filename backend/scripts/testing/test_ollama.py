import time

import ollama

MODEL = "qwen2.5:3b"

messages = [
    {
        "role": "system",
        "content": "Kamu adalah asisten AI.",
    },
    {
        "role": "user",
        "content": "Apa itu distribusi data? Jawab singkat.",
    },
]

print("=" * 50)
print("Mulai request...")
print("=" * 50)

start = time.perf_counter()

response = ollama.chat(
    model=MODEL,
    messages=messages,
)

elapsed = time.perf_counter() - start

print("\n===== HASIL =====\n")
print(response["message"]["content"])

print("\n=========================")
print(f"Waktu: {elapsed:.2f} detik")
print("=========================")