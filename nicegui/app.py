"""Test NiceGUI in Azure Web App."""
from nicegui import ui

ui.label('NiceGUI Running on Azure Container Apps')
ui.label('Deployed via GitHub Actions')
with ui.row():
	ui.icon('link').classes('text-2xl')
	ui.link('Joey40/NiceGuiTest', 'https://github.com/Joey40/NiceGuiTest')

ui.run()
