nome = input("Nome do Herói: ")
xp = int(input("Ponto de XP do Herói:"))

while xp < 0:
    print("Os pontos de XP não podem ser negativos! Tente novamente.")
    
    xp = int(input("Ponto de XP do herói:"))

else:
    if xp < 1000:
        nivel = "Ferro"
    elif xp > 1000 and xp <=2000:
        nivel = "Bronze"
    elif xp > 2000 and xp <=5000:
        nivel = "Prata"
    elif xp > 5000 and xp <=7000:
        nivel = "Ouro"
    elif xp > 7000 and xp <=8000:
        nivel = "Platina"
    elif xp > 8000 and xp <=9000:
        nivel = "Ascendente"
    elif xp > 9000 and xp <=10000:
        nivel = "Imortal"
    elif xp > 10000:
        nivel = "Radiante"

print(f"O Herói de nome {nome} está no nivel de {nivel}! Com {xp} pontos de XP.")