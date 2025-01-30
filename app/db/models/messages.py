from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.session import Base

class UsersMessages(Base):
    __tablename__ = 'users_messages'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False)
    user_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)