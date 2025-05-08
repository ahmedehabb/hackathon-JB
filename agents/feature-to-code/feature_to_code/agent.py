# agent.py
import os
from datetime import date

from google.genai import types

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import load_artifacts  # Keep this if you still need it

from .sub_agents import code_agent 
from .sub_agents import execution_agent
#from .sub_agents import bqml_agent  # Removed:  No longer needed
#from .sub_agents.bigquery.tools import ( # Removed: No longer needed
#    get_database_settings as get_bq_database_settings,
#)
from .prompts import return_instructions_root
from .tools import call_code_agent 
# from .tools import call_execution_agent
from .tools import call_critique_agent
#from .tools import call_db_agent, call_ds_agent # Removed: No longer needed

from .config import Config
configs = Config()
date_today = date.today()


root_agent = Agent(
    model=configs.agent_settings.model,
    name=configs.agent_settings.name,
    instruction=return_instructions_root(),
    global_instruction=(
        f"""
        You are a Code Development Multi Agent System.  You help users implement software features.
        """
    ),
    # sub_agents=[code_agent, execution_agent], 
    tools=[
        call_code_agent,
        # call_execution_agent,
        call_critique_agent,
        load_artifacts, #Keep if still needed
    ],
    # before_agent_callback=setup_before_agent_call,
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)