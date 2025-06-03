from .tool_dispatcher import dispatch_tool
from .memory_manager import get_context
from .prompts import get_prompt

def run_agent(user_input):
    context = get_context(user_input)
    prompt = get_prompt(context, user_input)
    response = dispatch_tool(prompt)
    return response