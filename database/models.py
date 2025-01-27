# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 27, 2025 17:18:40
# Database: sqlite:////tmp/tmp.pVBHNG1wPC-01JJMCACTCA8NEJJHQ6ZR9SVNF/NFLClubDataManagement/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class FootballClub(Base):  # type: ignore
    """
    description: Represents an NFL football club.
    """
    __tablename__ = 'football_club'
    _s_collection_name = 'FootballClub'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    stadium_name = Column(String)
    foundation_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    MerchandiseList : Mapped[List["Merchandise"]] = relationship(back_populates="club")
    PlayerList : Mapped[List["Player"]] = relationship(back_populates="football_club")
    PracticeScheduleList : Mapped[List["PracticeSchedule"]] = relationship(back_populates="club")
    CharityAffiliationList : Mapped[List["CharityAffiliation"]] = relationship(back_populates="club")



class Position(Base):  # type: ignore
    """
    description: Different positions a player can have during a game.
    """
    __tablename__ = 'position'
    _s_collection_name = 'Position'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Stadium(Base):  # type: ignore
    """
    description: Details about stadiums for the clubs.
    """
    __tablename__ = 'stadium'
    _s_collection_name = 'Stadium'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    capacity = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)



class TvAnnouncer(Base):  # type: ignore
    """
    description: TV announcers providing commentary for games.
    """
    __tablename__ = 'tv_announcer'
    _s_collection_name = 'TvAnnouncer'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    network = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    BroadcastScheduleList : Mapped[List["BroadcastSchedule"]] = relationship(back_populates="tv_announcer")



class BroadcastSchedule(Base):  # type: ignore
    """
    description: Broadcast schedule for games, linking games and announcers.
    """
    __tablename__ = 'broadcast_schedule'
    _s_collection_name = 'BroadcastSchedule'  # type: ignore

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    tv_announcer_id = Column(ForeignKey('tv_announcer.id'))
    game_date = Column(Date, nullable=False)

    # parent relationships (access parent)
    tv_announcer : Mapped["TvAnnouncer"] = relationship(back_populates=("BroadcastScheduleList"))

    # child relationships (access children)



class Merchandise(Base):  # type: ignore
    """
    description: Represents merchandise associated with football clubs.
    """
    __tablename__ = 'merchandise'
    _s_collection_name = 'Merchandise'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer)
    club_id = Column(ForeignKey('football_club.id'))

    # parent relationships (access parent)
    club : Mapped["FootballClub"] = relationship(back_populates=("MerchandiseList"))

    # child relationships (access children)



class Player(Base):  # type: ignore
    """
    description: Represents a player who is part of a football club.
    """
    __tablename__ = 'player'
    _s_collection_name = 'Player'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    history = Column(String)
    football_club_id = Column(ForeignKey('football_club.id'))

    # parent relationships (access parent)
    football_club : Mapped["FootballClub"] = relationship(back_populates=("PlayerList"))

    # child relationships (access children)
    BenefitList : Mapped[List["Benefit"]] = relationship(back_populates="player")
    CharityAffiliationList : Mapped[List["CharityAffiliation"]] = relationship(back_populates="player")
    GameStatisticList : Mapped[List["GameStatistic"]] = relationship(back_populates="player")
    HealthcareList : Mapped[List["Healthcare"]] = relationship(back_populates="player")



class PracticeSchedule(Base):  # type: ignore
    """
    description: Schedule for club practice sessions.
    """
    __tablename__ = 'practice_schedule'
    _s_collection_name = 'PracticeSchedule'  # type: ignore

    id = Column(Integer, primary_key=True)
    club_id = Column(ForeignKey('football_club.id'))
    date = Column(Date, nullable=False)
    time = Column(String)

    # parent relationships (access parent)
    club : Mapped["FootballClub"] = relationship(back_populates=("PracticeScheduleList"))

    # child relationships (access children)



class Benefit(Base):  # type: ignore
    """
    description: Additional benefits offered to players.
    """
    __tablename__ = 'benefit'
    _s_collection_name = 'Benefit'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    description = Column(String)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("BenefitList"))

    # child relationships (access children)



class CharityAffiliation(Base):  # type: ignore
    """
    description: Charities affiliated with either clubs or players.
    """
    __tablename__ = 'charity_affiliation'
    _s_collection_name = 'CharityAffiliation'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    player_id = Column(ForeignKey('player.id'))
    club_id = Column(ForeignKey('football_club.id'))

    # parent relationships (access parent)
    club : Mapped["FootballClub"] = relationship(back_populates=("CharityAffiliationList"))
    player : Mapped["Player"] = relationship(back_populates=("CharityAffiliationList"))

    # child relationships (access children)



class GameStatistic(Base):  # type: ignore
    """
    description: Statistics for games played by players.
    """
    __tablename__ = 'game_statistics'
    _s_collection_name = 'GameStatistic'  # type: ignore

    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    game_date = Column(Date, nullable=False)
    goals = Column(Integer)
    assists = Column(Integer)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("GameStatisticList"))

    # child relationships (access children)



class Healthcare(Base):  # type: ignore
    """
    description: Healthcare information for each player.
    """
    __tablename__ = 'healthcare'
    _s_collection_name = 'Healthcare'  # type: ignore

    id = Column(Integer, primary_key=True)
    policy_number = Column(String, nullable=False)
    player_id = Column(ForeignKey('player.id'), nullable=False)
    provider = Column(String)

    # parent relationships (access parent)
    player : Mapped["Player"] = relationship(back_populates=("HealthcareList"))

    # child relationships (access children)
