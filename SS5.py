#fri, jan 16, 2026
print("script by Cactus Airlines")
from pathlib import Path
import random
import base64
import json
import time
import pyperclip
import os

def crash():
    time.sleep(3)
    int("y")

def main_menu():
    while True: 
        print("\nchoose an option")
        print("100. Experiments")
        print("1. Impossible number game python edition")
        print("2. Base64")
        print("3. Basic password")
        print("4. JSON encoder")
        print("0. Exit")
        
        try:
            selected_item = int(input("choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if selected_item == 67:
            print("we do not allow the forbidden number.")
            crash()
        if selected_item > 100 or selected_item < 0:
            print("you can't do that")
            crash()

        if selected_item == 1:
            print("ING python edition")
            varmin = 1
            varmax = 2
            while True:
                random_number = random.randint(varmin, varmax)
                guess = int(input(f"put a number between {varmin} and {varmax} (0 to go back): "))
                if guess == random_number:
                    print("correct")
                    varmin *= 2
                    varmax *= 4
                elif guess == 0:
                    print("going back")
                    break
                else:
                    if varmin == 1:
                        print(f"incorrect, it was {random_number}.")
                    else:
                        varmin //= 2
                        varmax //= 4
                        print(f"incorrect, it was {random_number}.")

        elif selected_item == 2:
            print("1. Base64 Encode")
            print("2. Base64 Decode")
            print("3. Base64 but files are supported")
            print("0. Back to main menu")
            userinput = int(input("choose an option: "))
            text = ""
            
            if userinput == 1:
                print("base64 encoder")
                user_input = input("enter text: ")
                word = user_input.encode("utf-8")
                base = base64.b64encode(word)
                text = base.decode("utf-8")
            elif userinput == 2:
                print("base64 decoder")
                user_input = input("enter base64: ")
                word = user_input.encode("utf-8")
                base = base64.b64decode(word)
                text = base.decode("utf-8")
            elif userinput == 3:
                print("1. Encode")
                print("2. Decode")
                file_sub_choice = int(input("which one? "))
                folder = "extras"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                
                if file_sub_choice == 1:
                    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
                    if not files:
                        print("there is nothing there")
                    else:
                        print("\n--- Files ---")
                        for i, filename in enumerate(files):
                            print(f"{i + 1}. {filename}")
                        file_num = int(input("\nSelect the file number to encode: "))
                        selected_file = files[file_num - 1]
                        full_path = os.path.join(folder, selected_file)
                        with open(full_path, "rb") as f:
                            encoded_data = base64.b64encode(f.read()).decode("utf-8")
                            out_name = selected_file + ".b64.txt"
                            with open(os.path.join(folder, out_name), "w") as f:
                                f.write(encoded_data)
                        print(f"Saved as {out_name}")
                elif file_sub_choice == 2:
                    files = [f for f in os.listdir(folder) if f.endswith(".b64.txt")]
                    if not files:
                        print("There is nothing in the folder")
                    else:
                        for i, filename in enumerate(files):
                            print(f"{i + 1}. {filename}")
                        file_num = int(input("\nSelect the file to decode: "))
                        selected_file = files[file_num - 1]
                        with open(os.path.join(folder, selected_file), "r") as f:
                            decoded_data = base64.b64decode(f.read())
                        original_name = "RESTORED_" + selected_file.replace(".b64.txt", "")
                        with open(os.path.join(folder, original_name), "wb") as f:
                            f.write(decoded_data)
                        print(f"Restored as {original_name}")

            if userinput in [1, 2] and text:
                print("1. view")
                print("2. copy")
                print("3. save")
                save_choice = int(input("how save? "))
                if save_choice == 1:
                    print(text)
                elif save_choice == 2:
                    pyperclip.copy(text)
                    print("it should be copied")
                elif save_choice == 3:
                    folder_name = "extras"
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                    file_name = input("what to name the file? (add .txt) ")
                    save_path = os.path.join(folder_name, file_name)
                    with open(save_path, "w") as f:
                        f.write(text)

        elif selected_item == 3:
            password = 1234
            attempt = 0
            while attempt < 10:
                user_in = int(input("enter your password to continue: "))
                if user_in == password:
                    print("correct. There was nothing actually here so I guess I should just send you back to the main menu.")
                    break
                else:
                    attempt += 1
                    print(f"incorrect. You have {10 - attempt} attempts left.")
                    if attempt == 10:
                        print("out of attempts. Goodbye!")
                        crash()

        elif selected_item == 4:
            while True:
                print("\n1. AZ swap")
                print("2. Complex")
                print("3. AL, QZ swap")
                print("0. EXIT")
                chosen_pattern = int(input("which pattern: "))
                if chosen_pattern == 0:
                    break
                
                if chosen_pattern == 1:
                    json_thing = '{"A":"Z","a":"z","B":"Y","b":"y","C":"X","c":"x","D":"W","d":"w","E":"V","e":"v","F":"U","f":"u","G":"T","g":"t","H":"S","h":"s","I":"R","i":"r","J":"Q","j":"q","K":"P","k":"p","L":"O","l":"o","M":"N","m":"n","N":"M","n":"m","O":"L","o":"l","P":"K","p":"k","Q":"J","q":"j","R":"I","r":"i","S":"H","s":"h","T":"G","t":"g","U":"F","u":"f","V":"E","v":"e","W":"D","w":"d","X":"C","x":"c","Y":"B","y":"b","Z":"A","z":"a","0":"9","1":"8","2":"7","3":"6","4":"5","5":"4","6":"3","7":"2","8":"1","9":"0"," ":" ",".":"."}'
                elif chosen_pattern == 2:
                    json_thing = '{"Q":"A","A":"Q","a":"Z","Z":"a","q":"z","z":"q","W":"S","S":"W","s":"X","X":"s","x":"w","w":"x","E":"D","D":"E","d":"C","C":"d","e":"c","c":"e","R":"F","F":"R","f":"V","V":"f","r":"v","v":"r","T":"G","G":"T","g":"B","B":"g","t":"b","b":"t","Y":"H","H":"Y","h":"N","N":"h","y":"n","n":"y","U":"J","J":"U","j":"M","M":"j","u":"m","m":"u","I":"K","K":"I","k":"L","L":"k","i":"l","l":"i","O":"O","o":"P","P":"o","p":"p"," ":" ",".":".","7":"5","3":"1","8":"6","4":"2","0":"9","9":"0","5":"7","1":"3","6":"8","2":"4"}'
                elif chosen_pattern == 3:
                    json_thing = '{"A":"L","L":"A","a":"l","l":"a","S":"K","K":"S","s":"k","k":"s","D":"J","J":"D","d":"j","j":"d","F":"H","H":"F","f":"h","h":"f","G":"T","T":"G","g":"t","t":"g","Q":"Z","Z":"Q","q":"z","z":"q","P":"M","M":"P","p":"m","m":"p","W":"X","X":"W","w":"x","x":"w","O":"N","N":"O","o":"n","n":"o","E":"C","C":"E","e":"c","c":"e","B":"I","I":"B","b":"i","i":"b","R":"V","V":"R","r":"v","v":"r","Y":"U","U":"Y","y":"u","u":"y","1":"3","3":"1","2":"4","4":"2","5":"7","7":"5","6":"8","8":"6","9":"0","0":"9"}'
                
                json_otherthing = json.loads(json_thing)
                table = str.maketrans({ord(k): v for k, v in json_otherthing.items()})
                user_input = input("enter text to encode: ")
                message = user_input.translate(table)
                
                print("1. view")
                print("2. copy (EXP)")
                print("3. save (EXP)")
                save_choice = int(input("which one? "))
                if save_choice == 1:
                    print(f"\n{message}\n")
                elif save_choice == 2:
                    pyperclip.copy(message)
                    print("should be copied")
                elif save_choice == 3:
                    folder_name = "extras"
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)
                    file_name = input("name the file (ADD .txt): ")
                    save_path = os.path.join(folder_name, file_name)
                    with open(save_path, "w") as f:
                        f.write(message)

        elif selected_item == 0:
            print("0. exit")
            print("1. experiments")
            print("2. test")
            choice = int(input("which one? "))
            if choice == 0:
                confirm = input("are you sure? (y/n) ")
                if confirm == "y":
                    print("leaving")
                    crash()
            elif choice == 1:
                confirm = input("these might not be stable. Continue? (y/n) ")
                if confirm == "y":
                    print("1. read and write files")
                    print("2. images")
                    test_choice = int(input("which test? "))
                    if test_choice == 1:
                        p = Path('test_file.txt')
                        p.write_text('TEST')
                        print(p.read_text())
                    elif test_choice == 2:
                        print("planned but not started")

if __name__ == "__main__":
    main_menu()