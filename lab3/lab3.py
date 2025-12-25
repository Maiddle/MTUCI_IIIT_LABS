import os
def edit_add_file(file_path, content):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content + "\n")
    print(f"content added to {file_path}")
def choose_file_in_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            print("\nno files found in the directory.")
            return None
        print("\navailable files:")
        for i, file_name in enumerate(files, start=1):
            print(f"{i}. {file_name}")
        try:
            choice = int(input(f"\nenter file number(1 - {len(files)}): "))
            if 1 <= choice <= len(files):
                chosen_file = os.path.join(directory, files[choice - 1])
                print(f"\nyou choose file: {files[choice - 1]}")
                return chosen_file
            else:
                print("error: number out of range.")
                return None
        except ValueError:
            print("error: invalid input, please enter a number.")
            return None
    except FileNotFoundError:
        
        print("error: directory not found.")
        return None
def user_read_type(read_type,file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        if read_type == 'all':
            content = file.read()
            return content  
        elif read_type == 'line':
            lines = file.readlines()
            try:
                line_number = int(input(f"enter line number (1-{len(lines)}): "))
                if 1 <= line_number <= len(lines):
                    print(lines[line_number - 1].strip())
                else:
                    print("line number out of range")
            except ValueError:
                print("invalid input, please enter a number")
            return 
        else:
            return "invalid choice"

user_choice_directory = input("enter directory path: ").strip()
file_path = choose_file_in_directory(user_choice_directory)
if file_path:
    action = input("do you want to (r)ead or (a)dd content to the file? (r/a): ").strip().lower()
    if action == 'a':
        content_to_add = input("enter content to add: \n").strip()
        edit_add_file(file_path, content_to_add)
    elif action == 'r':
        read_type = input("do you want to read the (a)ll content or a specific (l)ine? (a/l): ").strip().lower()
        if read_type == 'a':
            file_content = user_read_type('all', file_path)
            print("\nfile content:\n")
            print(file_content)
        elif read_type == 'l':
            user_read_type('line', file_path)
        else:
            print("invalid choice")
    else:
        print("invalid choice")

