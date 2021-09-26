print("Bem vindo ao jogo, PALAVRA SECRETA!\n")

dicas = { # criação de uma 
    "1" : "Pode ser um detetive", #Perry o ornintorrinco haha 
    "2" : "É um animal",
    "3" : "É um mamifero"
}

secret_word = "ornitorrinco"
palpite = ""
cont_palpites = 0
limite_palpites = 5
end_game = False

while secret_word != palpite and not(end_game):
    if limite_palpites > cont_palpites:
        palpite = input("Digite o seu palpite: ")
        if palpite == "1":
            print(dicas.get("1"))
        elif palpite == "2":
            print(dicas.get("2"))
        elif palpite == "3":
            print(dicas.get("3"))
        cont_palpites += 1
        print("Palpites restantes: " + str(limite_palpites - cont_palpites))
    else:
        end_game = True
    
if end_game:
    print("Você perdeu! Mas não desanime, entre 7 bilhões de pessoas sempre existe uma patinho feio :-)")
    print("\nLembre-se, caso queira dicas, basta digitar o valor 1, 2 ou 3!")
else:
    print("Parabéns, você venceu!")
