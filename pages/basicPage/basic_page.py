from pages.general_elements.side_panel import SidePanel
from pages.general_elements.tool_bar import Toolbar


class BasicPage(Toolbar, SidePanel):
    def __init__(self, driver):
        super().__init__(driver)