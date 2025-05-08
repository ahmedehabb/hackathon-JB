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

# execution_agent.py
from google.adk.agents import Agent
from google.genai import types
from .prompts import return_instructions_execution_agent
from ...config import Config
from .tools import execute_code

configs = Config()


execution_agent = Agent(
    model=configs.execution_agent_settings.model,
    name=configs.execution_agent_settings.name,
    instruction=return_instructions_execution_agent(),
    global_instruction="You are a reliable code execution assistant.",
    tools=[execute_code],
    generate_content_config=types.GenerateContentConfig(temperature=0.0),  # Be precise
)