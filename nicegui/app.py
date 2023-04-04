"""Test NiceGUI in Azure Web App."""
from nicegui import app, ui

app.add_static_files('/images', 'images')
ui.label('NiceGUI example running on Azure Container Apps')
ui.label('Deployed via GitHub Actions')
with ui.row():
	ui.avatar('img:./images/github.png', size='md', font_size='32px', color='White')
	ui.link('Joey40/NiceGuiTest', 'https://github.com/Joey40/NiceGuiTest')

ui.run(
    title='NiceGUI ACA Test',
    favicon='./images/favicon.ico'
)
