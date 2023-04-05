from nicegui import ui


def menu() -> None:
    with ui.button(on_click=lambda: menu.open()).props('icon=menu'):
        with ui.menu() as menu:
            ui.link('Home', '/').classes(replace='text-white')