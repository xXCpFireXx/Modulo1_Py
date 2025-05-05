def greetings(name:str = "World")->str:
    Hi:str = "Hello, " + name +"!"
    return Hi

def sum (number1:int = 0, number2:int = 0)->int:
    return number1 + number2

def circle_area(radio:float=0.0)->float:
    return 3.1416*(radio*radio)

def is_even (number:int)->bool:
    if number % 2 == 0:
        return True
    else:
        return False
    
def largest_number(number1:int=0, number2:int=0, number3:int=0)->int:

    if number1 > number2 and number1 > number3:
       return number1
    elif number2> number1 and number2 > number3:
        return number2
    elif number3> number1 and number3 > number2:
        return number3
    else:
        return 0

def count_vowels (text:str="")->int:
    
    count = 0
    for i in text:
        if i == "a" or i=="e"or i=="i"or i=="o"or i=="u":
            count +=1
        elif i == "A" or i=="E"or i=="I"or i=="O"or i=="U":
            count +=1
    return f"La cantidad de vocales son {count}"

def is_palindrome (text:str=("reconoceR")):
    
    

    return text == text[::-1]
    



def main():
    print(greetings("Roxana"))
    print(sum(5,8))
    print(circle_area(4.5))
    print(is_even(3))
    print(largest_number(1,5,38))
    print(is_palindrome())
   

main()
print(count_vowels("hola amiguitos, Alas, Perros, GAtos"))

