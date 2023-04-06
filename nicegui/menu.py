from nicegui import ui

def menu() -> None:
    with ui.button(on_click=lambda: menu.open()).props('icon=menu'):
        with ui.menu() as menu:
            ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
            ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))