def me(name: str, number: int, age: int = 18)-> str:
    x = 2 + 3

    me("joy", 2000,  21)
    me(number=2323, age=21, name='joy')
    me(2323, name='joy')
    
    name = "joe"
    if name:
        x = 2 + 3