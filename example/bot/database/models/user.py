from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from bot.database.models.base import Base, TimestampMixin, big_int_pk, str_32, str_64, str_255


class UserModel(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[big_int_pk]
    username: Mapped[str_32 | None]
    first_name: Mapped[str_255 | None]
    last_name: Mapped[str_255 | None]
    deep_link: Mapped[str_64 | None]
    has_blocked_bot: Mapped[bool] = mapped_column(server_default=expression.false())
    locale: Mapped[str | None] = mapped_column(String(2))

    repr_cols = ("id", "username")
    repr_cols_num = 2
