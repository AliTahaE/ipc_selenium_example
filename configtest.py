# conftest.py
import sys
import os
import pytest

# Adding the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Your fixtures here...
@pytest.fixture(scope="session")
def browser_name():
    return "edge"

@pytest.fixture(scope="session")
def url():
    return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
