import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 781888702575371411 in succeeded_hashes:  # avoid duplicate inserts
            instance = club1 = FootballClub(id=1, name="Miami Dolphins", stadium_name="Hard Rock Stadium", foundation_date=date(1966, 8, 16))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(781888702575371411)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -108235777182951877 in succeeded_hashes:  # avoid duplicate inserts
            instance = club2 = FootballClub(id=2, name="New England Patriots", stadium_name="Gillette Stadium", foundation_date=date(1960, 9, 16))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-108235777182951877)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4514881211674422742 in succeeded_hashes:  # avoid duplicate inserts
            instance = club3 = FootballClub(id=3, name="Dallas Cowboys", stadium_name="AT&T Stadium", foundation_date=date(1960, 1, 22))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4514881211674422742)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2867522153646966104 in succeeded_hashes:  # avoid duplicate inserts
            instance = club4 = FootballClub(id=4, name="San Francisco 49ers", stadium_name="Levi's Stadium", foundation_date=date(1946, 8, 9))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2867522153646966104)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4102319262043734891 in succeeded_hashes:  # avoid duplicate inserts
            instance = player1 = Player(id=1, name="Tom Brady", position="QB", history="20 seasons", football_club_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4102319262043734891)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8560507192890712888 in succeeded_hashes:  # avoid duplicate inserts
            instance = player2 = Player(id=2, name="Troy Aikman", position="QB", history="12 seasons", football_club_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8560507192890712888)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5072596692604579671 in succeeded_hashes:  # avoid duplicate inserts
            instance = player3 = Player(id=3, name="Patrick Willis", position="LB", history="8 seasons", football_club_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5072596692604579671)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7387162973501881608 in succeeded_hashes:  # avoid duplicate inserts
            instance = player4 = Player(id=4, name="Dan Marino", position="QB", history="17 seasons", football_club_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7387162973501881608)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6002024114307443076 in succeeded_hashes:  # avoid duplicate inserts
            instance = stat1 = GameStatistics(id=1, player_id=1, game_date=date(2023, 10, 10), goals=2, assists=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6002024114307443076)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4562528669513421521 in succeeded_hashes:  # avoid duplicate inserts
            instance = stat2 = GameStatistics(id=2, player_id=2, game_date=date(2023, 10, 11), goals=1, assists=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4562528669513421521)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7066695200975414082 in succeeded_hashes:  # avoid duplicate inserts
            instance = stat3 = GameStatistics(id=3, player_id=3, game_date=date(2023, 10, 12), goals=0, assists=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7066695200975414082)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7165437424856864119 in succeeded_hashes:  # avoid duplicate inserts
            instance = stat4 = GameStatistics(id=4, player_id=4, game_date=date(2023, 10, 13), goals=3, assists=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7165437424856864119)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
