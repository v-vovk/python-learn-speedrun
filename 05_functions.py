from datetime import datetime

def show_date() -> None:
    print("This is the current date and time:")
    print(datetime.now())

show_date()

def greet(name: str, age: int) -> None:
    print(f"Hello, {name}! You are {age} years old.")

greet("Vlad", 29)

def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)
print(result)