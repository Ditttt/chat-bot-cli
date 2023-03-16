import aiohttp
import asyncio
import subprocess
import time
import sys
import traceback


class ChatBot:
    @staticmethod
    async def chat_bot(sentence: str):
        async with aiohttp.ClientSession() as session:
            token_chatbot = "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"
            payload = {
                "model": "text-davinci-003",
                "prompt": sentence,
                "temperature": 0.5,
                "max_tokens": 50,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1,
            }
            headers = {"Authorization": f"Bearer {token_chatbot}"}
            async with session.post(
                "https://api.openai.com/v1/completions", json=payload, headers=headers
            ) as resp:
                response = await resp.json()
                return response["choices"][0]["text"].replace('\n\n', '')

    @staticmethod
    async def start_chat():
        index = 0
        exit_chatbot = True
        while exit_chatbot:
            index += 1
            if index > 1:
                exit = input(
                    "Ketik Quit/Q Jika Ingin Keluar/Berhenti, Ketik Yes/Y Jika Ingin Lanjut : "
                ).title()
                match exit:
                    case "Quit":
                        subprocess.call("clear", shell=True)
                        sys.exit()
                    case "Q":
                        subprocess.call("clear", shell=True)
                        sys.exit()
                    case "Y":
                        subprocess.call("clear", shell=True)
                    case "Yes":
                        subprocess.call("clear", shell=True)
                    case _:
                        teks = "Input tidak valid, silahkan coba lagi".title()
                        print(f"\033[1m\033[31m{teks}\033[0m\033[0m")
                        continue

            pertanyaan = input("Silahkan Masukkan Pertanyaan Anda : ")
            try:
                res = await ChatBot.chat_bot(pertanyaan)
            except Exception:
                traceback.print_exc()
            else:
                subprocess.call("clear", shell=True)
                print(
                    f"""
🇶 : {pertanyaan}
🇦 : {res}
"""
                )


if __name__ == "__main__":
    asyncio.run(ChatBot.start_chat())
