# https://realpython.com/python-send-email/#transactional-email-services 
# https://github.com/ghpranav/python-bulk-mail/blob/master/mail.py

# maybe sendgrid for the future -> limit of sendinblue = 300mails/daily

"""
* add scheduling or run script for github workflows
"""

from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import os
import streamlit as st

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = st.secrets['SIB_API_KEY'] 

# create an instance of the API class
api_list_instance = sib_api_v3_sdk.ListsApi(sib_api_v3_sdk.ApiClient(configuration))
api_contact_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))

# Functions to interact with sendinblue api

def get_contacts_from_list(list_id: int=2) -> list:
    """Gets all contacts from the msw list (id = 2)"""
    try:
        # Get your account information, plan and credits details
        api_response = api_list_instance.get_contacts_from_list(str(list_id))
        api_response = api_response.contacts
        contacts: list = api_response#["contacts"]
        contacts = [contacts[0]["email"] for contacts[0] in contacts]
        #pprint(api_response)
        return contacts
    except ApiException as e:
        print("Exception when calling AccountApi->get_contacts_from_list: %s\n" % e)


def create_contact(email: str):
    """Creates a new sendinblue contact"""
    create_contact = sib_api_v3_sdk.CreateContact(email=email) # CreateContact | Values to create a contact

    try:
        # Create a contact
        api_response = api_contact_instance.create_contact(create_contact)
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)

def add_emails_to_list(emails: list, list_id: int=2):
    """Adds emails as a list to the msw sendinblue list (id = 2)"""
    try:
        # First, add new emails as a new contact
        added_mails = [create_contact(email) for email in emails]

        # Add existing contacts to a list
        contact_emails = sib_api_v3_sdk.AddContactToList(emails)
        api_response = api_list_instance.add_contact_to_list(list_id, contact_emails)
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListsApi->add_contact_to_list: %s\n" % e)
