def test_get_context():
    from agent_core.memory_manager import get_context
    assert isinstance(get_context("query"), str)