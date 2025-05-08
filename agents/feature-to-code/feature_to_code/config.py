# config.py
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
"""Configuration module for the code development agent."""

import os
import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AgentModel(BaseModel):
    """Agent model settings."""

    name: str = Field(default="code_development_agent")
    model: str = Field(default="gemini-2.0-flash-001")


class CodeAgentModel(BaseModel):
    """Code Agent model settings."""

    name: str = Field(default="code_agent")
    model: str = Field(default="gemini-2.0-flash-001")


class ExecutionAgentModel(BaseModel):
    """Execution Agent model settings."""

    name: str = Field(default="execution_agent")
    model: str = Field(default="gemini-2.0-flash-001")

class CritiqueAgentModel(BaseModel):
    """Critique Agent model settings."""

    name: str = Field(default="critique_agent")
    model: str = Field(default="gemini-2.0-flash-001")


class Config(BaseSettings):
    """Configuration settings for the code development agent."""

    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../.env"
        ),
        env_prefix="GOOGLE_",
        case_sensitive=True,
    )
    agent_settings: AgentModel = Field(default=AgentModel())
    code_agent_settings: CodeAgentModel = Field(default=CodeAgentModel())
    execution_agent_settings: ExecutionAgentModel = Field(default=ExecutionAgentModel())
    critique_agent_settings: CritiqueAgentModel = Field(default=CritiqueAgentModel())
    app_name: str = "code_development_app"  # Changed app name
    CLOUD_PROJECT: str = Field(default="aihktn25-shared")
    CLOUD_LOCATION: str = Field(default="us-central1")
    GENAI_USE_VERTEXAI: str = Field(default="1")  # Consider if you're using Vertex AI
    API_KEY: str | None = Field(default="")  # Keep this if you need an API key for the models
    TARGET_LANGUAGE: str = Field(default="Python") #Add Target language for future agent


