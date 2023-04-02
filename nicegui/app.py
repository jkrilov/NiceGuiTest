"""Test NiceGUI in Azure Web App."""
from nicegui import ui

ui.label('NiceGUI Running on Azure Web App')
ui.label('Deployed via GitHub Actions')

ui.run(
  port='8000' #default port used by Azure Web Apps
)
