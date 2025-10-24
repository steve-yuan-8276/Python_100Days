class kitty:
    eyes = 2
    paws = 4
    body = "fluffy"

    def __init__(self, name_of_cat, hobby):
        self.name = name_of_cat
        self.hobby = hobby

    def walk(self):
        print("I can walk")

    def catch(self):
        print("I caught a mouse!")

    def talk(self):
        print(f"Hi, My name is {self.name}.")
        print(f" I am a kitty.I have {self.eyes} eyes and {self.paws} paws.")
        print(f"I like to {self.hobby}")


Millie = kitty("Millie", "read")
Piper = kitty("Piper")


Millie.talk()
