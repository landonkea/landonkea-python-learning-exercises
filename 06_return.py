def build_greeting(name):
    if name == "Landon":
        return "Hey, it's you!"
    else:
        return "Hello, " + name + "!"

message = build_greeting("Landon")
print(message)

message2 = build_greeting("notLandon")
print(message2)
