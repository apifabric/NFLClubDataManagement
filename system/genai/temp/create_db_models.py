# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class FootballClub(Base):
    """description: Represents an NFL football club."""
    __tablename__ = 'football_club'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    stadium_name = Column(String)
    foundation_date = Column(Date)

class Player(Base):
    """description: Represents a player who is part of a football club."""
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String)
    history = Column(String)
    football_club_id = Column(Integer, ForeignKey('football_club.id'))

class GameStatistics(Base):
    """description: Statistics for games played by players."""
    __tablename__ = 'game_statistics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    game_date = Column(Date, nullable=False)
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)

class Merchandise(Base):
    """description: Represents merchandise associated with football clubs."""
    __tablename__ = 'merchandise'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    club_id = Column(Integer, ForeignKey('football_club.id'))

class Position(Base):
    """description: Different positions a player can have during a game."""
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Healthcare(Base):
    """description: Healthcare information for each player."""
    __tablename__ = 'healthcare'
    id = Column(Integer, primary_key=True, autoincrement=True)
    policy_number = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    provider = Column(String)

class Benefit(Base):
    """description: Additional benefits offered to players."""
    __tablename__ = 'benefit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    description = Column(String)

class CharityAffiliation(Base):
    """description: Charities affiliated with either clubs or players."""
    __tablename__ = 'charity_affiliation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=True)
    club_id = Column(Integer, ForeignKey('football_club.id'), nullable=True)

class TVAnnouncer(Base):
    """description: TV announcers providing commentary for games."""
    __tablename__ = 'tv_announcer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    network = Column(String)

class Stadium(Base):
    """description: Details about stadiums for the clubs."""
    __tablename__ = 'stadium'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)
    capacity = Column(Integer)

class PracticeSchedule(Base):
    """description: Schedule for club practice sessions."""
    __tablename__ = 'practice_schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    club_id = Column(Integer, ForeignKey('football_club.id'))
    date = Column(Date, nullable=False)
    time = Column(String)

class BroadcastSchedule(Base):
    """description: Broadcast schedule for games, linking games and announcers."""
    __tablename__ = 'broadcast_schedule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer)
    tv_announcer_id = Column(Integer, ForeignKey('tv_announcer.id'))
    game_date = Column(Date, nullable=False)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    club1 = FootballClub(id=1, name="Miami Dolphins", stadium_name="Hard Rock Stadium", foundation_date=date(1966, 8, 16))
    club2 = FootballClub(id=2, name="New England Patriots", stadium_name="Gillette Stadium", foundation_date=date(1960, 9, 16))
    club3 = FootballClub(id=3, name="Dallas Cowboys", stadium_name="AT&T Stadium", foundation_date=date(1960, 1, 22))
    club4 = FootballClub(id=4, name="San Francisco 49ers", stadium_name="Levi's Stadium", foundation_date=date(1946, 8, 9))
    player1 = Player(id=1, name="Tom Brady", position="QB", history="20 seasons", football_club_id=2)
    player2 = Player(id=2, name="Troy Aikman", position="QB", history="12 seasons", football_club_id=3)
    player3 = Player(id=3, name="Patrick Willis", position="LB", history="8 seasons", football_club_id=4)
    player4 = Player(id=4, name="Dan Marino", position="QB", history="17 seasons", football_club_id=1)
    stat1 = GameStatistics(id=1, player_id=1, game_date=date(2023, 10, 10), goals=2, assists=3)
    stat2 = GameStatistics(id=2, player_id=2, game_date=date(2023, 10, 11), goals=1, assists=1)
    stat3 = GameStatistics(id=3, player_id=3, game_date=date(2023, 10, 12), goals=0, assists=0)
    stat4 = GameStatistics(id=4, player_id=4, game_date=date(2023, 10, 13), goals=3, assists=2)
    
    
    
    session.add_all([club1, club2, club3, club4, player1, player2, player3, player4, stat1, stat2, stat3, stat4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
