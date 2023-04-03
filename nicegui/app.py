"""Test NiceGUI in Azure Web App."""
from nicegui import ui

ui.label('NiceGUI Running on Azure Container Apps')
ui.label('Deployed via GitHub Actions')


ui.run()
