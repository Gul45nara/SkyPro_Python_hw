import pytest
import uuid
from projects_api import ProjectsAPI


@pytest.fixture
def projects_api():
    return ProjectsAPI(mock_mode=True)


@pytest.fixture
def created_project(projects_api):
    """Фикстура создает временный проект для тестов"""
    unique_title = f"Test Project {uuid.uuid4().hex[:8]}"
    users = {"80eed1bd-eda3-4991-ac17-09d28566749d": "admin"}

    response = projects_api.create_project(unique_title, users)

    if response.status_code == 201:
        project_data = response.json()
        yield project_data
    else:
        pytest.fail(f"Failed to create test project: {response.text}")
