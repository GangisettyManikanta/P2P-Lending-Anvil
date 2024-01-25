from ._anvil_designer import all_transactionTemplate
from anvil import *
import anvil.facebook.auth
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class all_transaction(all_transactionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_2.items = app_tables.fin_wallet_transactions.search()
    # Any code you write here will run before the form opens.

  

  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("wallet.wallet")
