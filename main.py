'''
The following program could be used to write multiple cover letters, invitations letters or emails at one time.
Cover letters typically need to be adjusted to suit the requirements of positions and companies so
it might not be a great idea to use the same templates for every application.
'''

# Write the template for cover letter or email as a text file or a docx.
with open('template_letter.txt', mode='w') as letter_file:
    letter_file.write("[Your Name],\nAddress | Telephone | Email\n\n[Recipient Name]\nTitle\nCompany Name\n"
                      "Address\nCity, State Zipcode\n\nDear [Recipient Name],\n\n"
                      "Write the body of the text accordingly."
                      "\n-\n-\n-\n-\n-\n\nSincerely,\n[Your Name].")

# Write the names of recruiters or associated people as desire file types.
with open('recipient_names.txt', mode='w') as names_of_recipients:
    names_of_recipients.write('Joe\nJohn\nJesse\nDonna\nEmily\n')

# Create constants to easily change contents.
PLACEHOLDER = '[Recipient Name]'
YOUR_NAME = '[Your Name]'

# Get recipients' names as a list.
with open('recipient_names.txt') as names_file:
    # Readlines() returns a list. Don't use readline() which returns only one line.
    names = names_file.readlines()

with open('template_letter.txt') as letter_file:
    # Get contents of templates.
    contents = letter_file.read()
    # Change your name here or in template.
    change_your_name = contents.replace(YOUR_NAME, 'Thu')
    for name in names:
        # Remove new lines or blank spaces.
        new_name = name.strip()
        # If [Your Name] is change when writing template, use contents.replace(X, Y) to replace the line below.
        new_contents = change_your_name.replace(PLACEHOLDER, new_name)
        # Create new text files or word documents with names of recipients.
        with open(f'letter_for_{new_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_contents)


