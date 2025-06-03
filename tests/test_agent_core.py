def test_run_agent():
    from agent_core.agent_runner import run_agent
    assert "Recommended model" in run_agent("Suggest model for classification")