from faster_whisper import WhisperModel
from llama_cpp import Llama
import re
import time

# Function to extract JSON from model output
def extract_json_from_text(text):
    json_pattern = r'\{.*?\}'
    json_match = re.search(json_pattern, text, re.DOTALL)
    return json_match.group(0) if json_match else text

def process_audio_file(audio_file):
    # Load Whisper model for STT
    model_size = "small"
    whisper_model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # Load TinyLlama model
    llm = Llama.from_pretrained(
        repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
        filename="tinyllama-1.1b-chat-v1.0.Q2_K.gguf",
        n_ctx=2048,
        verbose=False,
    )

    print(f"\n🔊 Transcribing: {audio_file}")
    
    stt_start = time.time()
    segments, info = whisper_model.transcribe(audio_file, beam_size=5)
    stt_end = time.time()

    # Combine all transcribed segments into one string
    transcription = " ".join([segment.text for segment in segments])

    print(f"Language: {info.language} (probability: {info.language_probability:.2f})")
    print(f"🕒 STT Time: {stt_end - stt_start:.2f} seconds")
    print("📝 Transcript:")
    print(transcription)
    print("-" * 60)

    # Structured prompt for LLM
    messages = [
        {
            "role": "system",
            "content": """You are a JSON medical extractor. 
From the given clinical note, extract the relevant fields and return a **strict JSON object** with the following keys. 
Leave values as empty strings if the information is not mentioned. Return nothing else, only valid JSON.

Required format:
{
  "age": "",
  "sex": "",
  "presenting_complaint": "",
  "duration_of_symptoms": "",
  "associated_symptoms": "",
  "clinical_findings": "",
  "investigations": "",
  "diagnosis": "",
  "differential_diagnosis": "",
  "plan": "",
  "follow_up_advice": ""
}
"""
        },
        {
            "role": "user",
            "content": transcription
        }
    ]

    print("🧠 Extracting structured JSON...")
    json_start = time.time()
    response = llm.create_chat_completion(messages=messages)
    json_end = time.time()

    # Extract JSON portion
    json_output = response['choices'][0]['message']['content']
    json_extracted = extract_json_from_text(json_output)

    print(json_extracted)
    print(f"🧾 JSON Extraction Time: {json_end - json_start:.2f} seconds")
    print("=" * 60)

    return json_extracted

# Example usage
if __name__ == "__main__":
    audio_file = "ADHD.m4a"
    result_json = process_audio_file(audio_file)
    print("Final JSON Output:")
    print(result_json)
