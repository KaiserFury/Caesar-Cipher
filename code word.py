import Art 
print(Art.logo_caesar_cipher)
import os

# def system():
#     os.system('cls' if os.name == 'nt' else 'system')



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
number=['0','1','2','3','4','5','6','7','8','9',
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', 
        ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ' , ]


def caesar(message, shift,direction):
    code_store = ""
    if direction=="decode":
        shift*= -1
    for i in message:
        if i in number :
            # code_store += i
            message_index = number.index(i)
            new_index = (message_index + shift) % len(number)  
            code_store += number[new_index]

        else:
            message_index = alphabet.index(i)
            new_index = (message_index + shift) % len(alphabet)  
            code_store += alphabet[new_index]

    print(f"Your {user} message is :",code_store)


ask_to_continue="yes"
while ask_to_continue=="yes":
    user=input("Type encode to 'encrypt,Type decode to 'decrypt'\n").lower()
    if user not in ["decode", "encode"]:
        os.system("cls")
        print("You enter wrong command please try again !!!")
        continue
    text=str(input("Enter the your message (in lower case):\n"))
    shift_amount=int(input("Enter the shift number:\n"))
    
    caesar(direction=user,message=text,shift=shift_amount)
    ask_to_continue=input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    
    if ask_to_continue=="no":
        print("Goodbye")
    else:
        os.system("cls")

