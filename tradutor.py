#Linguagem do risonho, sempre que há uma vogal, substitui-se por "k"

def translate (frase):
    translation = "" #criando string para receber a tradução
    
    for letter in frase: #for para passar por cada letra
        if letter.lower() in "aeiou": #vogais negativas
            if letter.isupper(): #vogais positivas 
                translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter 
    return translation
            
print(translate(input("Digite uma frase: ")))
