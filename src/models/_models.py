from sqlalchemy.orm import declarative_base, mapped_column, Mapped


from sqlalchemy import (
    BIGINT,
    String,
    TIMESTAMP,
    func,
    text,
    Boolean,
    ClauseElement
)

from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    registration_date: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    newsletter_sended: Mapped[bool] = mapped_column(server_default=text("false"))

    state: Mapped[str] = mapped_column(String(64))
    state_updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    status: Mapped[str] = mapped_column(String(32), server_default=text("'alive'"))  # Alive | dead
    before_web: Mapped[int] = mapped_column(server_default="0")

    text_1600_february: Mapped[datetime] = mapped_column(TIMESTAMP)
    text_1730_february: Mapped[datetime] = mapped_column(TIMESTAMP)
    text_1830_february: Mapped[datetime] = mapped_column(TIMESTAMP)
    text_1910_february: Mapped[datetime] = mapped_column(TIMESTAMP)


class Sending(Base):
    __tablename__ = 'sendings'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    sent_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

# select(User.id).where(User.status == 'alive', User.state == 'wait_gift', User.id.notin_(select(Sending.user_id).where(Sending.id == 'wait_gift')))
