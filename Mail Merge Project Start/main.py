from docx import Document # type: ignore

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    doc = Document()
    doc.add_paragraph(new_letter)
    doc.save(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx")
    # with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as complete_letter:
    #     complete_letter.write(new_letter)