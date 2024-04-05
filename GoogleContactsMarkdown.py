import csv
import os

def create_markdown_file(contact_data, filename):
    """Creates a Markdown file for a given contact."""

    with open(filename, "w") as f:
        f.write("**Contact Information**\n\n")
        f.write(f"* **Name:** {contact_data.get('Name', '')}\n")
        f.write(f"* **Phone:** {contact_data.get('Phone 1 - Value', '')}\n")
        f.write(f"* **Email:** {contact_data.get('E-mail 1 - Value', '')}\n")
        f.write(f"* **Address:** {contact_data.get('Address 1 - Formatted', '')}\n\n")

        f.write("**Additional Information**\n\n")
        f.write(f"* **Birthday:** {contact_data.get('Birthday', '')}\n")
        f.write(f"* **Important Dates:** {contact_data.get('Event', '')}\n")  # Modify if needed
        f.write(f"* **Relationship:** {contact_data.get('Relation', '')}\n\n")  # Modify if needed

        f.write("**Notes**\n\n")
        f.write(f"{contact_data.get('Notes', '')}\n\n") 

        f.write("**Prayer Requests**\n\n")  
        # Placeholder (if you want to include this section)

        f.write("**Other**\n\n") 
        # Placeholder for customizable section

def process_contacts_csv(csv_filename):
    """Reads 'contacts.csv' and creates Markdown files."""

    with open(csv_filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            firstname = row.get("Name", "").split(" ")[0]  # Extract first name
            lastname = row.get("Name", "").split(" ")[-1]  # Extract last name
            filename = f"{firstname} {lastname}.md"

            create_markdown_file(row, filename)

if __name__ == "__main__":
    process_contacts_csv("contacts.csv")  # Replace 'contacts.csv' with your filename
