#Suma de elemento de una lista
def sum_elements(list:[int]=[]):
    sum_number = 0
    for i in list:
        sum_number += i

    return print(f"TOTAL IS {sum_number}")


#Eliminar duplicados de una lista
def delete_doubled_item(list_double:[int] = []):
    i=0
    list_two = []

    for i in list_double:
        if i in list_double:
            if i not in list_two:
                list_two.append(i)
    
    return print(f"FINAL LIST IS {list_two}")

#Invertir una lista (sin métodos built-in)
def reverse_list(list:[str] = []):
    
    list_two = []

    for i in range(len(list)-1,-1,-1):
        list_two.append(list[i])
    return print(list_two)

#Contador de palabras
def word_counter(list:[str] = []):

    diccionare = {}

    for i in list:
        if i in diccionare:
            diccionare[i] += 1
        else:
            diccionare[i] = 1

    return print(diccionare)

#Combinar dos listas ordenadas
def merge_lists(list_one=[], list_two=[]):

    merged_list=[]

    for i in list_one:
        

    return print(merged_list)


def main():
    sum_elements([35,41,29,15,41])
    delete_doubled_item([35,41,29,15,41])
    reverse_list([35,41,29,15])
    word_counter(["Hola","Camila","Cristian","Camila","Hello","Hola"])
    merge_lists([1,3,5], [2,4,6])
main()