import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
@anvil.server.callable
def calculate_next_month_due():
  app_tables.fin_loan_details.search()
  app_tables.fin_emi_table.search()
    # Assuming scheduled_payment is a string in the format 'YYYY-MM-DD'
  try:
      scheduled_date = datetime.datetime.strptime(scheduled_payment, '%Y-%m-%d').date()
      next_due_date = scheduled_date + relativedelta(months=1)
      return next_due_date.strftime('%Y-%m-%d')
  except ValueError:
      return None

@anvil.server.callable
def today_dues():
  app_tables.fin_loan_details.search()
  if emi_payment_type == 'One Time':
    if tenure:
      next_payment = loan_disbursed_timestamp.date() + timedelta(days=30 * tenure)
    elif emi_payment_type == 'Monthly':
      # For monthly payment, set next_payment to a month after first_payment_due_date
      next_payment = loan_disbursed_timestamp.date() + timedelta(days=30)
    elif emi_payment_type == 'Three Month':
      # For three-month payment, set next_payment to three months after first_payment_due_date
      next_payment = loan_disbursed_timestamp.date() + timedelta(days=90)
    elif emi_payment_type == 'Six Month':
      # For six-month payment, set next_payment to six months after first_payment_due_date
      next_payment = loan_disbursed_timestamp.date() + timedelta(days=180)
    else:
      # Default to monthly calculation if emi_payment_type is not recognized
      next_payment = loan_disbursed_timestamp.date() + timedelta(days=30)
              