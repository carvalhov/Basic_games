#Linguagem do risonho, sempre que há uma vogal, substitui-se por "k"

def translate (frase):
    translation = "" #criando string para receber a tradução
    
    for letter in frase: #for para passar por cada letra
        if letter.lower() in "aeiou": #vogais
            if letter.isupper(): #se vogais maiusculas - > K 
                translation = translation + "K"
            else: #caso não maiusculas - > k
                translation = translation + "k"
        else:
            translation = translation + letter 
    return translation
            
print(translate(input("Digite uma frase: ")))
