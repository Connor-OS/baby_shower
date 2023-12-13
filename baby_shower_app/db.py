import click

from flask import current_app, g
from sqlalchemy import create_engine
import pandas as pd

from baby_shower_app.entitites import Base


def get_db():
    if 'db' not in g:
        g.db = create_engine(f"sqlite:///{current_app.config['DATABASE']}", echo=True)

    return g.db


def init_db():
    engine = create_engine(f"sqlite:///{current_app.config['DATABASE']}", echo=True)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with engine.connect() as connection:
        gift_df = pd.read_csv("./baby_shower_app/static/test_db_seed.csv")
        gift_df.to_sql("Gift", con=connection, index=False, if_exists="append")


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)