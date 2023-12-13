from flask import Blueprint, render_template, request, flash
from sqlalchemy.orm import Session
from sqlalchemy import select

from baby_shower_app.db import get_db
from baby_shower_app.entitites import Gift, Guest
from baby_shower_app.email import send_reserve_email

sender_email = "arai.and.connor@gmail.com"
receiver_email = "coshaughnessy1@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python.
"""


bp = Blueprint('gift_inspo', __name__)


def get_gift_list():

    session = Session(get_db())
    available_gifts = session.scalars(select(Gift)).all()

    return available_gifts

def reserve_gift(name, message, gift_id):

    session = Session(get_db())
    # add bought flag to gift
    gift = session.scalars(select(Gift).where(Gift.gift_id == gift_id)).one()
    gift.bought = True

    # add guest to db
    guest = Guest(
        name=name,
        message=message
    )
    session.add(guest)

    # send email containing gift message
    send_reserve_email(gift.name, name, message)

    session.commit()

@bp.route('/gift_inspo', methods=(['POST', 'GET']))
def gift_inspo():

    if request.method == "GET":

        return render_template('gift_inspo.html', gift_list=get_gift_list())

    if request.method == "POST":
        reserve_gift(**dict(request.form))
        return render_template('gift_inspo.html', gift_list=get_gift_list())


@bp.route('/gift', methods=('GET', 'POST'))
def gift():
    gift_id = request.args.get('gift_id')

    session = Session(get_db())
    gift = session.scalars(select(Gift).where(Gift.gift_id == gift_id)).one()

    error = None
    if not gift:
        error = "no such gift"
        flash(error)

    return render_template('gift.html', gift=gift)