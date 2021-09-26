print("Bem vindo ao jogo, PALAVRA SECRETA!\n")

dicas = { # criação de um dictionarie de strings para strings
    #key -> correspondente
    "1" : "Pode ser um detetive", #Perry o ornintorrinco haha 
    "2" : "É um animal",
    "3" : "É um mamifero"
}
secret_word = "ornitorrinco" 
palpite = ""
cont_palpites = 0 #conta os palpites utilizados (int)
limite_palpites = 5 #estabelece um limite para os palpites (int)
end_game = False 
#bool para estabelecer o fim do jogo, naturalmente, antes do começo, o fim de jogo é falso 

while secret_word != palpite and not(end_game):
#a repetição ocorre, enquanto o palpite não bate com a palavra secreta e, enquanto end_game = false
    if limite_palpites > cont_palpites:
        palpite = input("Digite o seu palpite: ")
#Caso digite os valores key, chama os valores correspondentes no dicionário
        if palpite == "1":
            print(dicas.get("1"))
        elif palpite == "2":
            print(dicas.get("2"))
        elif palpite == "3":
            print(dicas.get("3"))
        cont_palpites += 1 #conta os palpites gastos
        print("Palpites restantes: " + str(limite_palpites - cont_palpites)) #Mostra os palpites restantes
    else: #Quando limite_palpites deixa de ser maior que cont_palpites, end_game = True e o while se encerra 
        end_game = True
    
if end_game:
    print("Você perdeu! Mas não desanime, entre 7 bilhões de pessoas sempre existe uma patinho feio :-)")
    print("\nLembre-se, caso queira dicas, basta digitar o valor 1, 2 ou 3!")
else:
    print("Parabéns, você venceu!")
