from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
from db.models import Base

fdb = SQLAlchemy(model_class=Base)
migrate = Migrate(directory='alembic')

# pylint: disable=wrong-import-position, ungrouped-imports
from api.factory import create_app
from db.seed import main as seed

app = create_app(config=Config)


@app.cli.command('seed')
def command_seed():
    seed()
    print("Corpus data added to database.")
