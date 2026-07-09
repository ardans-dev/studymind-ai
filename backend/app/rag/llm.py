import ollama


class LLM:
    """
    Wrapper untuk berkomunikasi dengan Ollama.
    """

    MODEL = "gemma3:4b"

    @staticmethod
    def chat(prompt: str) -> str:

        response = ollama.chat(
            model=LLM.MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]
