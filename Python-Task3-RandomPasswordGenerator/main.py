
import string
import secrets

print("==============================")
print("     PASSWORD GENERATOR")
print("==============================")

try:
    password_length = int(input("Enter the desired password length: "))

    if password_length < 8:
        print("Error: Password length must be at least 8.")

    else:
        print("\nPassword length accepted!")

        characters = ""
        required_characters = []

        lowercase = input("Include lowercase letters? (yes/no): ")

        if lowercase.lower() == "yes":
            characters += string.ascii_lowercase
            required_characters.append(secrets.choice(string.ascii_lowercase))

        uppercase = input("Include uppercase letters? (yes/no): ")

        if uppercase.lower() == "yes":
            characters += string.ascii_uppercase
            required_characters.append(secrets.choice(string.ascii_uppercase))

        numbers = input("Include numbers? (yes/no): ")

        if numbers.lower() == "yes":
            characters += string.digits
            required_characters.append(secrets.choice(string.digits))

        symbols = input("Include symbols? (yes/no): ")

        if symbols.lower() == "yes":
            characters += string.punctuation
            required_characters.append(secrets.choice(string.punctuation))

        if len(required_characters) < 2:
            print("\nError: Please select at least 2 character types!")

        else:
            print("\nCharacter selection accepted!")

            while True:

                password_characters = required_characters.copy()

                for i in range(password_length - len(password_characters)):
                    password_characters.append(secrets.choice(characters))

                secrets.SystemRandom().shuffle(password_characters)

                password = "".join(password_characters)

                print("\nGenerated Password:", password)

                again = input("\nGenerate another password? (yes/no): ")

                if again.lower() != "yes":
                    print("\nThank you for using Password Generator!")
                    break

except ValueError:
    print("\nPlease enter numbers only!")

