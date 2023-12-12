from sqlalchemy.orm import declarative_base, mapped_column, Mapped

from sqlalchemy import (
    BIGINT,
    String,
    TIMESTAMP,
    func,
    text,
    Boolean
)

from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    registration_date: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    

    got_autosending_1: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    got_autosending_2: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    newsletter_sended: Mapped[bool] = mapped_column(Boolean, default=False)