# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from google.adk.agents import Agent
from google.genai import types
from .prompts import return_instructions_code_agent
# from .tools import modify_files
from ...config import Config
from pydantic import BaseModel, Field
configs = Config()
PROJECT_DIR = "/Users/ahmed.ehab/Desktop/adk-samples-main/agents/feature-to-code/feature_to_code/sub_agents/critiqueagent/recorder/new_project"


class Modification(BaseModel):
    """A single modification to be made to a file."""
    file_path: str = Field(description="Name of the file to be modified")
    code: str = Field(description="Code to be added to the file")

class ModificationList(BaseModel):
    """A list of modifications to be made to files."""
    file_modifications: list[Modification]


def modify_files(file_modifications: ModificationList) -> str:
    """Modifies the specified files with the provided code."""
    print("Modifying files...")
    try:
        modifications = file_modifications['file_modifications']
        for modification in modifications:
            file_path = modification['file_path']  # Access attributes directly
            code = modification['code']  # Access attributes directly
            # Here you would implement the logic to modify the file
            # For example, you could open the file and write the code to it
            with open(os.path.join(PROJECT_DIR, file_path), 'w') as f: # Overwrite (change 'a' to 'w')
                f.write(code)
            print(f"Modified {file_path} with the provided code.")
        return f"Modified {len(file_modifications['file_modifications'])} files successfully."
    except Exception as e:
        print(f"Error modifying files: {str(e)}")
        return f"Error modifying files: {str(e)}"

code_agent = Agent(
    model=configs.code_agent_settings.model,
    name=configs.code_agent_settings.name,
    instruction=return_instructions_code_agent(),
    tools=[modify_files],
    input_schema=ModificationList,
    global_instruction="You are a reliable code modification assistant.",
    generate_content_config=types.GenerateContentConfig(temperature=0.2),  # Adjust temperature as needed
)
