import ollama


class LLM:

    MODEL = "gemma3:4b"

    @staticmethod
    def chat(prompt: str):

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