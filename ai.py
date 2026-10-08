from google import genai

client = genai.Client()

notice = client.files.upload(file="notice.jpg")

prompt = """
You are CampusLens AI, an assistant for college students.

Read the college notice carefully and extract the important information.

Return the answer in this format:

EVENT:
DATE:
TIME:
VENUE:
DEADLINE:
REQUIREMENTS:

SUMMARY:

IMPORTANT DETAILS:

If something is not mentioned in the notice, write "Not mentioned".
Do not guess or invent information.
"""

response = client.models.generate_content(
    model="gemma-4-31b-it",
    contents=[notice, prompt]
)

print(response.text)