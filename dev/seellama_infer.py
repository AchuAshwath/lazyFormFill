from transformers import pipeline
import time
import re

# Initialize the model using Hugging Face pipeline
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")

# Sample clinical text
sample_text = """
The patient is a 4-year-old male named Rohan Kumar, born at 38 weeks via normal vaginal delivery. He cried immediately at birth and had no postnatal complications. He was exclusively breastfed for the first 6 months. Rohan lives in Bangalore with his parents. His father, Mr. Rajesh Kumar, can be reached at 9876543210, and his mother, Mrs. Meena Kumar, at 9876543211. There is no known consanguinity, and the antenatal and perinatal periods were uneventful. The child was conceived naturally. Parents report concerns about delayed speech and poor social interaction. On examination, he maintains minimal eye contact, exhibits repetitive hand-flapping, and does not respond consistently to name. No gross motor delay noted. Diagnosis is suspected Autism Spectrum Disorder. Plan includes referral to developmental pediatrician, initiation of speech therapy, and audiological evaluation.
"""

# Define prompt
prompt = f"""
You are a JSON medical extractor. Return only the JSON output.

From this clinical note:

\"\"\"{sample_text}\"\"\"

Extract and return a JSON object with the following keys. Leave empty if not mentioned:
{{
  "first_name": "",
  "last_name": "",
  "sex": "",
  "chronological_age": "",
  "gestational_age": "",
  "father_name": "",
  "father_contact": "",
  "mother_name": "",
  "mother_contact": "",
  "residence": "",
  "chief_complaint": "",
  "clinical_observation": "",
  "diagnosis": "",
  "plan": ""
}}
"""

# Run inference
start_time = time.time()
output = pipe(prompt, max_new_tokens=2048, do_sample=True, temperature=0.7)
end_time = time.time()

# Output text from model
generated_text = output[0]['generated_text']
print(generated_text)
print(f"\nTime taken: {end_time - start_time:.2f} seconds")

# Extract JSON from generated text
json_pattern = r'\{.*?\}'
json_match = re.search(json_pattern, generated_text, re.DOTALL)
print("\nExtracted JSON:\n", json_match.group(0) if json_match else "No JSON found")
