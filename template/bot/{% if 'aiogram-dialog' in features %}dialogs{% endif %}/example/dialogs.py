from __future__ import annotations

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const
from bot.states import ExampleSG

example_dialog = Dialog(
    Window(
        Const("Example dialog"),
        Cancel(Const("Cancel")),
        state=ExampleSG.example,
    ),
)
