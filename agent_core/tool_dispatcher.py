def dispatch_tool(prompt):
    if "model" in prompt:
        from tools.model_selector import recommend_model
        return recommend_model(prompt)
    elif "diagram" in prompt:
        from tools.architecture_designer import generate_architecture
        return generate_architecture(prompt)
    return "No suitable tool found."