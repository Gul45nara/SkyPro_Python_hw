class TestProjectsNegative:
    """Негативные тесты для методов проектов."""

    def test_create_project_without_title(self, projects_api):
        """Создание проекта без title."""
        response = projects_api.create_project(title=None)
        assert response.status_code == 400
        msg = "✅ Создание без title - 400"
        print(msg)

    def test_get_nonexistent_project(self, projects_api):
        """Получение несуществующего проекта."""
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(nonexistent_id)
        assert response.status_code == 404
        msg = "✅ Получение несуществующего - 404"
        print(msg)

    def test_update_nonexistent_project(self, projects_api):
        """Обновление несуществующего проекта."""
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.update_project(nonexistent_id, "New Title")
        assert response.status_code == 404
        msg = "✅ Обновление несуществующего - 404"
        print(msg)

    def test_create_project_with_empty_title(self, projects_api):
        """Создание проекта с пустым title."""
        response = projects_api.create_project(title="")
        assert response.status_code == 400
        msg = "✅ Создание с пустым title - 400"
        print(msg)

    def test_update_project_with_empty_data(
        self, projects_api, created_project
    ):
        """Обновление проекта без данных."""
        project_id = created_project['id']
        response = projects_api.update_project(project_id)
        assert response.status_code == 400
        msg = "✅ Обновление без данных - 400"
        print(msg)
