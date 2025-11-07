import pytest
import sys
import os
from sqlalchemy import text

# Добавляем папку 09_lesson в путь Python для импортов
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from database import engine, SessionLocal
from models import Company, Base


class TestCompanyCRUD:

    @pytest.fixture(autouse=True)
    def setup(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()
        yield
        self.db.execute(
            text("DELETE FROM company WHERE name LIKE 'Test Company%'")
        )
        self.db.commit()
        self.db.close()

    def test_create_company(self):
        new_company = Company(name="Test Company Create")
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        assert new_company.id is not None
        assert new_company.name == "Test Company Create"

    def test_update_company(self):
        company = Company(name="Test Company Update")
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        company.name = "Updated Company Name"
        self.db.commit()
        self.db.refresh(company)
        assert company.name == "Updated Company Name"

    def test_soft_delete_company(self):
        company = Company(name="Test Company Delete")
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)
        company_id = company.id
        company.soft_delete()
        self.db.commit()
        deleted_company = self.db.query(Company).filter(
            Company.id == company_id
        ).first()
        assert deleted_company.is_deleted
