from google import genai
from google.genai import types
import base64

def generate(prompt):  # Take the prompt as an argument
    client = genai.Client(
        vertexai=True,
        project="aihktn25-shared",  # Replace with your project ID
        location="us-central1",
    )

    # Load video from local computer
    video_file_path = "/Users/ahmed.ehab/Desktop/adk-samples-main/record-app/output.mp4"  # Replace with the actual path to your video file
    mime_type = "video/mp4" #Change the mime_type according to the video type
    try:
        with open(video_file_path, "rb") as video_file:
            video_data = video_file.read()
            video1 = types.Part.from_bytes(data=video_data, mime_type=mime_type)
    except FileNotFoundError:
        print(f"Error: Video file not found at {video_file_path}")
        return  # Exit the function if the file is not found

    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(
            role="user",
            parts=[
                video1,
                types.Part.from_text(text=prompt),  # Use the dynamic prompt
            ],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        max_output_tokens=8192,
        response_modalities=["TEXT"],
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"
            ),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model, contents=contents, config=generate_content_config
    ):
        print(chunk.text, end="")


# Example of how to execute the function with a dynamic prompt
user_prompt = "Summarize the key events in this video in three sentences."
generate(user_prompt)