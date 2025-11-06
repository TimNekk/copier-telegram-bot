from __future__ import annotations

from aiogram.fsm.state import State, StatesGroup


class ExampleSG(StatesGroup):
    example = State()
