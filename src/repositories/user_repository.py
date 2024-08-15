from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    auth_id = Column(String(50), unique=True, nullable=False)
    user_name = Column(String(45), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_deleted = Column(Boolean, nullable=False, default=True)

    requested_books = relationship("RequestedBook", back_populates="user")
    admin = relationship("Admin", uselist=False, back_populates="user")
    book_reviews = relationship("BookReview", back_populates="user")
    reservations = relationship("Reservation", back_populates="user")
    loans = relationship("Loan", back_populates="user")
