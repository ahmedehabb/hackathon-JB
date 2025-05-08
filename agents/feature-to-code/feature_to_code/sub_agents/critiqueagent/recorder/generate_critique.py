from google import genai
from google.genai import types
import base64

def generate(reference_video_path: str, current_state_video_path: str) -> str:
    client = genai.Client(
        vertexai=True,
        project="aihktn25-shared",  # Replace with your project ID
        location="us-central1",
    )

    # Load video 1
    mime_type = "video/mp4" #Change the mime_type according to the video type
    try:
        with open(reference_video_path, "rb") as video_file:
            video_data1 = video_file.read()
            video1 = types.Part.from_bytes(data=video_data1, mime_type=mime_type)
    except FileNotFoundError:
        print(f"Error: Video file not found at {reference_video_path}")
        return  # Exit the function if the file is not found
    
    # Load video 2
    try:
        with open(current_state_video_path, "rb") as video_file:
            video_data2 = video_file.read()
            video2 = types.Part.from_bytes(data=video_data2, mime_type=mime_type)
    except FileNotFoundError:
        print(f"Error: Video file not found at {current_state_video_path}")
        return  # Exit the function if the file is not found


    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=instruction_prompt),  # Use the dynamic prompt
            ],
        ),
        types.Content(
            role="user",
            parts=[
                video1,
                types.Part.from_text(text=prompt1),  # Use the dynamic prompt
            ],
        ),
        types.Content(
            role="user",
            parts=[
                video2,
                types.Part.from_text(text=prompt2),  # Use the dynamic prompt
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

    # return the text by streaming the response
    response = ""
    for chunk in client.models.generate_content_stream(
        model=model, contents=contents, config=generate_content_config
    ):
        print(chunk.text, end="")
        response += chunk.text
    return response


instruction_prompt = """
I am providing two inputs:

A video of the original feature (Source - the desired behavior).
A video of the implemented feature (Target - the current implementation).

Your primary task is to meticulously compare the Target implementation to the Source and identify **all observable discrepancies**, encompassing both User Interface (UI) accuracy and functional behavior. Your goal is to provide a comprehensive list of issues to guide the Target towards being indistinguishable from the Source.

**Scan Priority and Initial Focus:**
While you should aim to identify all types of discrepancies, begin your scan by **prioritizing a thorough examination of UI elements for visual accuracy.** Think of yourself as a highly detailed UI/UX quality assurance specialist initially, but be prepared to note functional issues as you see them.

**Identifying Discrepancies (UI & Functional):**

Look for any differences, including but not limited to:

*   **UI Discrepancies (Visuals, Layout, Styling - Scan these thoroughly first):**
    *   Incorrect colors, fonts, text content, sizes, or styles. (e.g., "Button color is green, Source is blue.")
    *   Misplaced elements, incorrect dimensions, improper spacing/alignment. (e.g., "Logo is 10px too far left.")
    *   Incorrect or missing visual styles like borders, shadows, opacity, rounded corners. (e.g., "Input field is missing the 1px gray border shown in Source.")
*   **Functional Discrepancies (Interactions, Animations, Behavior - Note these as observed):**
    *   Actions not working as expected or at all. (e.g., "'Delete' button does not remove the item.")
    *   Animations or transitions missing, incorrect in timing, or having the wrong visual effect. (e.g., "Menu appears instantly, Source shows a 0.2s slide-in.")
    *   User interactions leading to an incorrect state or data display. (e.g., "Search results do not filter according to the input text.")

**Reporting Format for Each Identified Discrepancy:**

For *each* discrepancy you find, provide the following:

1.  **Type:** Clearly state if it's a "UI Discrepancy" or a "Functional Discrepancy".
2.  **Description:** Clearly and specifically describe the issue.
    *   *For UI:* Reference exact visual attributes and how the Target differs from the Source (e.g., "UI Discrepancy: The main heading text 'Welcome User' in Target uses 'Arial' font, while Source uses 'Roboto' font.").
    *   *For Functional:* Explain exactly how the Target's behavior differs from the Source's behavior (e.g., "Functional Discrepancy: Clicking the 'Sort' button in Target does not reorder the list, whereas in Source it sorts the list alphabetically.").
3.  **Suggested Fix:** Suggest a direct and actionable step to fix the issue.
    *   *For UI:* Suggest a CSS/style change (e.g., "Change font-family of heading to 'Roboto'.").
    *   *For Functional:* Suggest a code logic or implementation change (e.g., "Implement the sorting logic for the 'Sort' button's click event.").

**Goal for Output:**
Your output should be a **comprehensive list of all identified discrepancies**, each formatted as described above. Aim to be thorough. If multiple similar UI issues exist (e.g., several buttons have the wrong color), list each one if they are distinct elements or require distinct fixes.

**Special Conditions:**

*   **No Discrepancies Found:** If, after a thorough examination, you find that the Target is visually and behaviorally identical to the Source, respond with the following *exact* message: "The Target implementation is identical to the Source. No changes are required."
*   **Overwhelming Differences:** If the Target is so significantly different from the Source that listing individual discrepancies becomes impractical (e.g., completely different layout and functionality), you may state this and recommend a complete reimplementation, but only as a last resort if a detailed list is not feasible.

Your objective is to act as a constructive and exhaustive critique, providing all necessary feedback in one go to guide the implementation towards a state that is *indistinguishable* from the Source video. Start by rigorously identifying UI issues, then incorporate functional ones.
"""

video_path1 = "/Users/ahmed.ehab/Desktop/adk-samples-main/agents/feature-to-code/feature_to_code/sub_agents/critiqueagent/recorder/reference.mp4" #Path to first video
prompt1 = "Here is the first video, A video of the original feature (Source - the desired behavior)." #prompt for first video
video_path2 = "/Users/ahmed.ehab/Desktop/adk-samples-main/agents/feature-to-code/feature_to_code/sub_agents/critiqueagent/recorder/output.mp4" #Path to second video
prompt2 = "Here is the second video, A video of the implemented feature (Target - the current implementation)." #prompt for second video
# generate(reference_video_path=video_path1, current_state_video_path=video_path2)