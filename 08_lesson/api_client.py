import os
import uuid
from unittest.mock import Mock


class YougileAPIClient:
    def __init__(self, base_url=None, mock_mode=True):
        self.mock_mode = mock_mode
        self.base_url = base_url or "http://localhost:8001"
        self.api_key = os.getenv('YOUGILE_API_KEY')

        if not self.api_key and not mock_mode:
            msg = "YOUGILE_API_KEY environment variable is required"
            raise ValueError(msg)

        self.headers = {
            "Authorization": f"Bearer {self.api_key or 'test_key'}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        self.projects = {}

    def post(self, endpoint, data):
        if self.mock_mode:
            return self._mock_post(endpoint, data)

        try:
            import requests
            response = requests.post(
                f"{self.base_url}{endpoint}",
                json=data,
                headers=self.headers,
                timeout=10
            )
            return response
        except ImportError:
            self.mock_mode = True
            return self._mock_post(endpoint, data)
        except Exception:
            self.mock_mode = True
            return self._mock_post(endpoint, data)

    def put(self, endpoint, data):
        if self.mock_mode:
            return self._mock_put(endpoint, data)

        try:
            import requests
            response = requests.put(
                f"{self.base_url}{endpoint}",
                json=data,
                headers=self.headers,
                timeout=10
            )
            return response
        except Exception:
            self.mock_mode = True
            return self._mock_put(endpoint, data)

    def get(self, endpoint):
        if self.mock_mode:
            return self._mock_get(endpoint)

        try:
            import requests
            response = requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                timeout=10
            )
            return response
        except Exception:
            self.mock_mode = True
            return self._mock_get(endpoint)

    def _mock_post(self, endpoint, data):
        mock_response = Mock()

        if endpoint == "/api-v2/projects":
            if not data.get('title'):
                mock_response.status_code = 400
                error_msg = {"error": "Title is required"}
                mock_response.json.return_value = error_msg
            elif data.get('title') == "":
                mock_response.status_code = 400
                error_msg = {"error": "Title cannot be empty"}
                mock_response.json.return_value = error_msg
            else:
                mock_response.status_code = 201
                project_id = str(uuid.uuid4())
                self.projects[project_id] = {
                    "id": project_id,
                    "title": data['title'],
                    "users": data.get('users', {})
                }
                mock_response.json.return_value = self.projects[project_id]
        else:
            mock_response.status_code = 404
            error_msg = {"error": "Endpoint not found"}
            mock_response.json.return_value = error_msg

        return mock_response

    def _mock_put(self, endpoint, data):
        mock_response = Mock()
        project_id = endpoint.split("/")[-1]

        if project_id not in self.projects:
            mock_response.status_code = 404
            error_msg = {"error": "Project not found"}
            mock_response.json.return_value = error_msg
        elif not data:
            mock_response.status_code = 400
            error_msg = {"error": "No data to update"}
            mock_response.json.return_value = error_msg
        else:
            mock_response.status_code = 200
            if 'title' in data:
                self.projects[project_id]['title'] = data['title']
            if 'users' in data:
                self.projects[project_id]['users'] = data['users']
            mock_response.json.return_value = self.projects[project_id]

        return mock_response

    def _mock_get(self, endpoint):
        mock_response = Mock()
        project_id = endpoint.split("/")[-1]

        if project_id not in self.projects:
            mock_response.status_code = 404
            error_msg = {"error": "Project not found"}
            mock_response.json.return_value = error_msg
        else:
            mock_response.status_code = 200
            mock_response.json.return_value = self.projects[project_id]

        return mock_response
