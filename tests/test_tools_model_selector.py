def test_model_recommendation():
    from tools.model_selector import recommend_model
    assert "RandomForestClassifier" in recommend_model("classification task")