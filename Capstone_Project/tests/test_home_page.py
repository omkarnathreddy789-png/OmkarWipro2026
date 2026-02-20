def test_open_homepage(setup):

    driver = setup

    assert "Automation Practice Site" in driver.title
