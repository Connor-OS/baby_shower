import sqlalchemy as sqla
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Gift(Base):
    """Stores Submission information."""

    __tablename__ = "gift"

    gift_id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(), nullable=False)
    description = sqla.Column(sqla.String(), nullable=False)
    price = sqla.Column(sqla.String(), nullable=False)
    link = sqla.Column(sqla.String(), nullable=False)
    image = sqla.Column(sqla.String(), nullable=False)
    bought = sqla.Column(sqla.Boolean(), nullable=False)

    guests = relationship("Guest", back_populates="gift")

class Guest(Base):
    """Stores Submission information."""

    __tablename__ = "guest"

    guest_id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(), nullable=False)
    message = sqla.Column(sqla.String(), nullable=True)
    gift_id = sqla.Column(sqla.Integer, sqla.ForeignKey("gift.gift_id"))

    gift = relationship("Gift", back_populates="guests")