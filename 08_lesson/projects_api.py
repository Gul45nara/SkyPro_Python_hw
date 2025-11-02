from api_client import YougileAPIClient


class ProjectsAPI:
    def __init__(self, base_url=None, mock_mode=True):
        self.client = YougileAPIClient(base_url, mock_mode)
        self.base_endpoint = "/api-v2/projects"

    def create_project(self, title, users=None):
        """Создать проект [POST] /api-v2/projects"""
        data = {"title": title}
        if users:
            data["users"] = users

        return self.client.post(self.base_endpoint, data)

    def update_project(self, project_id, title=None, users=None):
        """Обновить проект [PUT] /api-v2/projects/{id}"""
        data = {}
        if title is not None:
            data["title"] = title
        if users is not None:
            data["users"] = users

        endpoint = f"{self.base_endpoint}/{project_id}"
        return self.client.put(endpoint, data)

    def get_project(self, project_id):
        """Получить проект [GET] /api-v2/projects/{id}"""
        endpoint = f"{self.base_endpoint}/{project_id}"
        return self.client.get(endpoint)
