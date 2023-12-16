from openai import OpenAI

client = OpenAI(api_key='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')

with open("English.m4a", "rb") as audio_file:
    transcript = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file
    )
print(transcript)