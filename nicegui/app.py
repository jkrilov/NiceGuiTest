"""Test NiceGUI in Azure Web App."""
from nicegui import ui

ui.label('NiceGUI Running on Azure Web App')
ui.label('Deployed via GitHub Actions')


ui.run()
