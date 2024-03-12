from ._anvil_designer import ItemTemplate31Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import main_form_module 


class ItemTemplate31(ItemTemplate31Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user_id = main_form_module.userId
        user_data = app_tables.fin_user_profile.get(customer_id=self.user_id)
        if user_data:
            self.image_1.source = user_data['user_photo']

    def outlined_button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        loan_id_to_display = self.loan_id.text
        open_form('admin.dashboard.loan_management.approved_loans.view_profile', loan_id_to_display)
