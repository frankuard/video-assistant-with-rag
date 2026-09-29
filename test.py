from dotenv import load_dotenv

# Load environment variables before importing core modules
load_dotenv()

from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summaries import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)



# INPUT


source = "https://youtu.be/0Ho79yq1_jw?si=psF55CPyfXcMUexo"



# 1. PROCESS AUDIO


print("\n" + "=" * 60)
print("🎵 PROCESSING AUDIO")
print("=" * 60)

chunks = process_input(source)



# 2. TRANSCRIBE AUDIO


print("\n" + "=" * 60)
print("🎙️ TRANSCRIBING AUDIO")
print("=" * 60)

transcript = transcribe_all(chunks)



# 3. SAVE TRANSCRIPT


with open("transcript.txt", "w", encoding="utf-8") as file:
    file.write(transcript)

print("\n✅ Transcript saved successfully!")


# 4. DISPLAY TRANSCRIPT

print("\n" + "=" * 60)
print("📝 TRANSCRIPT")
print("=" * 60)

if len(transcript) > 500:
    print(transcript[:500] + "...")
else:
    print(transcript)


# 5. GENERATE TITLE

print("\n" + "=" * 60)
print("📌 GENERATING TITLE")
print("=" * 60)

title = generate_title(transcript)

print(f"\nTitle: {title}")


 # 6. GENERATE SUMMARY


print("\n" + "=" * 60)
print("📋 GENERATING SUMMARY")
print("=" * 60)

summary = summarize(transcript)

print("\n" + summary)



# 7. EXTRACT ACTION ITEMS


print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)

action_items = extract_action_items(transcript)

print(action_items)



# 8. EXTRACT KEY DECISIONS


print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)

decisions = extract_key_decisions(transcript)

print(decisions)



# 9. EXTRACT OPEN QUESTIONS


print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)

questions = extract_questions(transcript)

print(questions)



# COMPLETE


print("\n" + "=" * 60)
print("🎉 AI VIDEO ASSISTANT COMPLETED")
print("=" * 60)

