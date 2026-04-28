# 1)
def Mystere(n):
    """n :int -> int
    Rôle: à découvrir !"""
    tmp1 = n * 345
    tmp2 = n * 5 +200
    tmp1 = (tmp1 -9 * tmp2)//100
    tmp2 = tmp1 +18
    return (tmp2 / 3 )% 100

print(Mystere(153688999))

# 2) le type du paramètre de la fonciton mystère est int

# 3) elle prend les 2 dernière valeurs