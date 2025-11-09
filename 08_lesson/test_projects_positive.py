class TestProjectsPositive:
    """Позитивные тесты для методов проектов."""

    def test_create_project_success(self, projects_api):
        """Позитивный тест создания проекта."""
        title = "Тестовый проект"
        users = {"80eed1bd-eda3-4991-ac17-09d28566749d": "admin"}

        response = projects_api.create_project(title, users)

        assert response.status_code == 201
        data = response.json()
        assert data['title'] == title
        assert data['users'] == users
        assert 'id' in data
        print(f"✅ Создан проект с ID: {data['id']}")

    def test_get_project_success(self, projects_api, created_project):
        """Позитивный тест получения проекта."""
        project_id = created_project['id']

        response = projects_api.get_project(project_id)

        assert response.status_code == 200
        data = response.json()
        assert data['id'] == project_id
        assert 'title' in data
        assert 'users' in data
        print(f"✅ Получен проект: {data['title']}")

    def test_update_project_success(self, projects_api, created_project):
        """Позитивный тест обновления проекта."""
        project_id = created_project['id']
        new_title = "Обновленный тестовый проект"
        new_users = {
            "80eed1bd-eda3-4991-ac17-09d28566749d": "admin",
            "new_user_id": "user"
        }

        response = projects_api.update_project(
            project_id, new_title, new_users
        )

        assert response.status_code == 200
        data = response.json()
        assert data['title'] == new_title
        assert data['users'] == new_users
        print(f"✅ Проект обновлен: {data['title']}")
