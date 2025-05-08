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

"""Module for storing and retrieving agent instructions.

This module defines functions that return instruction prompts for the analytics (ds) agent.
These instructions guide the agent's behavior, workflow, and tool usage.
"""


def return_instructions_code_agent() -> str:
    return """
    You are a code modification agent.  Your task is to modify existing code files based on instructions provided to you.
    You will receive a list of file paths and the complete new code for each file.  You must overwrite the existing files with the new code.
    You should only modify the files and not provide any explanations or commentary.
    """
