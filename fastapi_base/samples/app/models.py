"""
Database models of {app_name} app
"""

# you need to import Base from [project_name].database 
from src.database import Base


class YourModel(Base):
    __tablename__ = 'YOUR_TABLE_NAME'