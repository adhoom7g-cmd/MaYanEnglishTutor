"""Database connection and models for user progress tracking"""

from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime, Float, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

# Global engine and session factory
_engine = None
_SessionLocal = None

class User(Base):
    """User model for storing learner profiles"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    job_role = Column(String)  # hotel_staff, tour_guide, website_manager
    created_at = Column(DateTime, default=datetime.now)
    last_active = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Progress(Base):
    """Progress model for tracking learning across all modules"""
    __tablename__ = 'progress'
    
    __table_args__ = (UniqueConstraint('user_name', name='uix_user_name'),)
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False, unique=True)
    
    # Vocabulary progress
    vocabulary_words_learned = Column(Integer, default=0)
    vocabulary_by_category = Column(JSON, default=dict)
    mastered_words = Column(JSON, default=list)
    
    # Conversation progress
    conversations_completed = Column(Integer, default=0)
    conversation_scenarios = Column(JSON, default=dict)
    
    # Grammar progress
    grammar_completed = Column(Integer, default=0)
    grammar_by_topic = Column(JSON, default=dict)
    
    # Reading progress
    reading_completed = Column(Integer, default=0)
    reading_by_type = Column(JSON, default=dict)
    reading_scores = Column(JSON, default=list)
    
    # Pronunciation progress
    pronunciation_practiced = Column(Integer, default=0)
    pronunciation_by_category = Column(JSON, default=dict)
    
    # Writing progress
    writing_completed = Column(Integer, default=0)
    writing_by_type = Column(JSON, default=dict)
    
    # Achievements and activity
    achievements = Column(JSON, default=list)
    activity_history = Column(JSON, default=list)
    
    last_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

def get_database_engine():
    """Create and return database engine"""
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")
    
    engine = create_engine(database_url)
    return engine

def init_database():
    """Initialize database tables"""
    engine = get_database_engine()
    Base.metadata.create_all(engine)
    return engine

def get_session():
    """Get database session"""
    engine = init_database()
    Session = sessionmaker(bind=engine)
    return Session()
