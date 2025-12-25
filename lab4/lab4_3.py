from modulepack import mytext
from modulepack import mymodule
user_input = input("Enter name: ")
shouted_text = mytext.shout(user_input)
boo = mymodule.scary(user_input)
print("Shouted text:", shouted_text)
print("Boo text:", boo)
