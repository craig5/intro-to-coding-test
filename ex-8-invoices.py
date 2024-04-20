#!/usr/bin/env python3


def read_companies():
    data = dict()
    with open("2024-04-19-companies.csv") as fp:
        lines = fp.readlines()
    # Skip the first line since it is a "header line".
    for cur_line in lines[1:]:
        # When reading a file, there will be a "\n" at the end of the line.
        # This next line simply removes that "\n".
        # https://docs.python.org/3.11/library/stdtypes.html#str.rstrip
        cur_line = cur_line.rstrip("\n")
        # Parse the line and split it into a list using the comma as a seperator.
        parts = cur_line.split(",")
        # To be very explicit; assign each part to a variable.
        company_name = parts[0]
        # Add the data to the dictionary as ANOTHER dictionary.
        data[company_name] = {
            "contact-name": parts[1],
            "contact-phone": parts[2],
        }
    return data


def read_invoices():
    data = list()
    with open("2024-04-19-invoices.csv", "r") as fp:
        lines = fp.readlines()
    # Skip the first line since it is a "header line".
    for cur_line in lines[1:]:
        # When reading a file, there will be a "\n" at the end of the line.
        # This next line simply removes that "\n".
        # https://docs.python.org/3.11/library/stdtypes.html#str.rstrip
        cur_line = cur_line.rstrip("\n")
        # Break up the line using a comma as the seperator.
        parts = cur_line.split(",")
        cur_data = {
            "invoice-id": parts[0],
            "company-name": parts[1],
            "status": parts[2],
        }
        # In this case, just append the current dictionary to the LIST of all invoices.
        data.append(cur_data)
    return data


def find_unpaid_invoices(invoices):
    unpaid = list()
    # FIXME Loop through each invoice find the unpaid ones.
    #
    return unpaid


def unique_customers_from_invoices(invoices, companies):
    unique = dict()
    for cur_invoice in invoices:
        cur_company_name = cur_invoice["company-name"]
        if cur_company_name in unique:
            continue
        unique[cur_company_name] = companies[cur_company_name]
    return unique


def show_people_to_call():
    # Read in the data from the relevant files.
    companies = read_companies()
    invoices = read_invoices()
    # Find just the unpaid invoices.
    unpaid = find_unpaid_invoices(invoices)
    # Combine the unpaid invoices with the customer list to get a list of people to call.
    unique_unpaid = unique_customers_from_invoices(unpaid, companies)
    for cur_name, cur_data in unique_unpaid.items():
        # FIXME Print out each line from the unique list.
        #


# You should notice that we have only definied subroutines.
# So, let's just call the ONE subroutine we care about:
show_people_to_call()
