"""Test NiceGUI in Azure Web App."""
from nicegui import app, ui

app.add_static_files('/images', 'images')

@ui.page('/')
def home_page():
    ui.label('NiceGUI example running on Azure Container Apps')
    ui.label('Deployed via GitHub Actions')
    with ui.row():
        ui.avatar('img:./images/github.png', size='md', font_size='24px', color='White')
        ui.link('Joey40/NiceGuiTest', 'https://github.com/Joey40/NiceGuiTest')
    with ui.row():
        with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
            badge = ui.badge('0', color='red').props('floating')
        ui.button('Reset', on_click=lambda: badge.set_text('0'))

@ui.page('/egg')
def egg():
    ui.label('You found an Easter Egg!')

ui.run(
    title='NiceGUI ACA Test',
    favicon='./images/favicon.ico'
)
