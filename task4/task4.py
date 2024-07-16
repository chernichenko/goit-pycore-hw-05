# Decorator to handle input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Arguments are missing or too many arguments."
    
    return inner

# Example command functions
@input_error
def add(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def all(args, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Main interaction loop
def main():
    contacts = {}
    
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command.startswith("add"):
            args = input("Enter the argument for the command: ").strip().split()
            print(add(args, contacts))
        
        elif command.startswith("phone"):
            args = input("Enter the argument for the command: ").strip().split()
            print(phone(args, contacts))
        
        elif command.startswith("all"):
            args = input("Enter the argument for the command: ").strip().split()
            print(all(args, contacts))
        
        elif command == "exit":
            break
        
        else:
            print("Invalid command. Available commands: add, phone, all, exit")

if __name__ == "__main__":
    main()
