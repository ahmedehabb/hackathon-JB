# tools.py
from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool

from .sub_agents import code_agent
from .sub_agents import execution_agent
from .sub_agents import critique_agent

import json

async def call_code_agent(
    file_modifications: list[dict[str, str]],
    tool_context: ToolContext,
):
    """Tool to call the Code Agent for modifying existing code files.

    Args:
        file_modifications: A list of dictionaries, where each dictionary
            contains the file_path (str) and code (str) for a file to be modified.
    """
    print("calling code agent")
    agent_tool = AgentTool(agent=code_agent)

    code_agent_output = await agent_tool.run_async(
        args={"file_modifications": file_modifications},
        tool_context=tool_context,
    )
    # tool_context.state["code_agent_output"] = code_agent_output # Optional: Store output if needed
    return code_agent_output

async def call_critique_agent(
    tool_context: ToolContext,
):
    """Tool to call the Critique Agent for code review and suggestions."""
    print("calling critique agent")
    agent_tool = AgentTool(agent=critique_agent)

    critique_agent_output = await agent_tool.run_async(
        args={
            "request": "Run the critique tool now !",
        },
        tool_context=tool_context,
    )
    # tool_context.state["critique_agent_output"] = critique_agent_output # Optional: Store output if needed
    return critique_agent_output