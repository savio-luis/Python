print("Calculadora de redução do tempo de vida de um fumante")
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

cigarros_fumados = cigarros_por_dia * 365 * anos_fumando
tempo_perdido_em_minutos = cigarros_fumados * 10
tempo_perdido_em_dias = tempo_perdido_em_minutos / (24 * 60)

print(f"Um fumante que fuma {cigarros_por_dia} cigarros por dia e fuma há {anos_fumando} anos, perderá aproximadamente {tempo_perdido_em_dias:.1f} dias de vida.")
