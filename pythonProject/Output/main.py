# Create a letter using start_letter.txt
# for each name in invited_names.txt
# replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".



with open("../Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("../Input/letters/start_letter.txt") as file2:
    content = file2.read()
    for name in names:
            new_name = name.strip()
            new_content = content.replace("[name]", new_name)
            with open(f"ReadyToSend/{new_name}.txt", mode="w") as file3:
                file3.write(new_content)






