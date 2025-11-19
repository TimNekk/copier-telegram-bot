from __future__ import annotations

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel

from bot.dialogs.common.widgets import I18NFormat
from bot.states.example import ExampleSG

example_dialog = Dialog(
    Window(
        I18NFormat("example-dialog"),
        Cancel(I18NFormat("cancel")),
        state=ExampleSG.example,
    ),
)
