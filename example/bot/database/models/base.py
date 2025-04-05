import datetime
from decimal import Decimal
from typing import Annotated

from sqlalchemy import BigInteger, Numeric, String, text
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True)]
big_int_pk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
str_255 = Annotated[str, mapped_column(String(255))]
str_32 = Annotated[str, mapped_column(String(32))]
decimal = Annotated[Decimal, mapped_column(Numeric(10, 2))]


class Base(AsyncAttrs, DeclarativeBase):
    repr_cols_num: int = 3  # print first columns
    repr_cols: tuple = ()  # extra printed columns

    def __repr__(self) -> str:
        cols = [
            f"{col}={getattr(self, col)}"
            for idx, col in enumerate(self.__table__.columns.keys())
            if col in self.repr_cols or idx < self.repr_cols_num
        ]
        return f"<{self.__class__.__name__} {', '.join(cols)}>"


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
    )
