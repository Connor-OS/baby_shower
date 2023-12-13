import sqlalchemy as sqla
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Gift(Base):
    """Stores Submission information."""

    __tablename__ = "gift"

    gift_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(), nullable=False)
    description = sqla.Column(sqla.String(), nullable=False)
    price = sqla.Column(sqla.String(), nullable=False)
    link = sqla.Column(sqla.String(), nullable=False)
    image = sqla.Column(sqla.String(), nullable=False)
    bought = sqla.Column(sqla.Boolean(), nullable=False)


class Guest(Base):
    """Stores Submission information."""

    __tablename__ = "guest"

    guest_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(), nullable=False)
    # email = sqla.Column(sqla.String(), nullable=True)
    message = sqla.Column(sqla.String(), nullable=True)
    # gift_bought: Mapped[List["Gift"]] = sqla.orm.relationship(back_populates="gift_id")
