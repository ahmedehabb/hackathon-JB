import subprocess
import os
from google.adk.agents import Agent
from google.genai import types
from .prompts import return_instructions_critique_agent
from ...config import Config
configs = Config()
# PROJECT_DIR = "/Users/ahmed.ehab/Desktop/new_project"
from .recorder import app, generate_critique  # Assuming recorder.py is in the same directory

REFERENCE_VIDEO_PATH = os.path.join(os.path.dirname(__file__), "recorder", "reference.mp4") # Set this!
GENERATED_VIDEO_PATH = os.path.join(os.path.dirname(__file__), "recorder", "output.mp4") # Set this!



def analyze_videos(reference_video_path: str, generated_video_path: str) -> str:
    """Analyzes two videos and generates a critique.

    Args:
        reference_video_path: The path to the reference video.
        generated_video_path: The path to the generated video.

    Returns:
        A critique of the differences between the two videos.
    """
    try:
        return generate_critique.generate(reference_video_path, generated_video_path)
    except Exception as e:
        return f"Error analyzing videos: {e}"

def run_critique_tool(request: str) -> str:
    # I want to run a command line tool to run ./recorder/record.sh 
    print("Running critique agent...")
    app.run_record_sh()
    critique = analyze_videos(REFERENCE_VIDEO_PATH, GENERATED_VIDEO_PATH)
    return critique

critique_agent = Agent(
    model=configs.critique_agent_settings.model,
    name=configs.critique_agent_settings.name,
    instruction=return_instructions_critique_agent(),
    tools=[run_critique_tool],
    global_instruction="You are a Critique Agent. You help users implement software features.",
    generate_content_config=types.GenerateContentConfig(temperature=0.2),  # Adjust temperature as needed
)