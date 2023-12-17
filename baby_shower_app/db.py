import click

from flask import current_app, g
from sqlalchemy import create_engine
import pandas as pd

from baby_shower_app.entitites import Base


def get_db():
    if 'db' not in g:
        g.db = create_engine(current_app.config['DATABASE'], echo=True)

    return g.db


def init_db():
    engine = get_db()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with engine.connect() as connection:
        gift_df = pd.read_csv("./baby_shower_app/static/db_seed.csv")
        gift_df.to_sql("gift", con=connection, index=False, if_exists="append")


def add_db():
    engine = get_db()

    with engine.connect() as connection:
        gift_df = pd.read_csv("./baby_shower_app/static/db_add.csv")
        gift_df.to_sql("gift", con=connection, index=False, if_exists="append")


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('add-db')
def add_db_command():
    """Clear the existing data and create new tables."""
    add_db()
    click.echo('Added extra database entries.')


def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_db_command)
