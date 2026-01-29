def test_ini_values(pytestconfig):
    assert pytestconfig.getini("addopts") == ["-v"]

def test_environment(request):
    env = request.config.getoption("--env")
    assert env in ["dev", "qa", "prod"]