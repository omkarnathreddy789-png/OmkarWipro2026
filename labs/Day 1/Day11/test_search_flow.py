def test_search_flow():
    # Simulated end-to-end search
    search_term = "pytest"
    results = ["pytest tutorial", "pytest framework"]

    assert search_term in results[0]
    assert len(results) > 0