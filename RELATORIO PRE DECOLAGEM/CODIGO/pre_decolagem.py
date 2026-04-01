# ==========================================
# TRABALHO FIAP FASE 1 - SISTEMA DE PRÉ-DECOLAGEM
# Aluno: APOLIANO OLIVEIRA DO NASCIMENTO NETO
# Turma: 1CCOA 
# ==========================================

print("===== SISTEMA DE PRÉ-DECOLAGEM =====")
print("Digite os dados da missão:")
print()

# ENTRADA DE DADOS
temperatura_interna = float(input("Temperatura interna (°C): "))
temperatura_externa = float(input("Temperatura externa (°C): "))
integridade_estrutural = int(input("Integridade estrutural (1 = íntegra / 0 = falha): "))
nivel_energia = float(input("Nível de energia (%): "))
pressao_tanques = float(input("Pressão dos tanques (psi): "))
modulos_criticos = input("Módulos críticos (ativos ou inativos): ")

# DADOS ENERGÉTICOS
capacidade_total = float(input("Capacidade total de energia (kWh): "))
consumo_decolagem = float(input("Consumo estimado na decolagem (kWh): "))
perdas = float(input("Perdas energéticas (%): "))

# FAIXAS SEGURAS
temp_interna_min = 18
temp_interna_max = 27
temp_externa_min = -50
temp_externa_max = 50
energia_minima = 60
pressao_min = 70
pressao_max = 90

# LISTA DE PROBLEMAS
problemas = []

# VERIFICAÇÕES
if temperatura_interna < temp_interna_min or temperatura_interna > temp_interna_max:
    problemas.append("Temperatura interna fora da faixa segura.")

if temperatura_externa < temp_externa_min or temperatura_externa > temp_externa_max:
    problemas.append("Temperatura externa fora da faixa segura.")

if integridade_estrutural != 1:
    problemas.append("Falha na integridade estrutural.")

if nivel_energia < energia_minima:
    problemas.append("Nível de energia insuficiente.")

if pressao_tanques < pressao_min or pressao_tanques > pressao_max:
    problemas.append("Pressão dos tanques fora da faixa segura.")

if modulos_criticos.lower() != "ativos":
    problemas.append("Módulos críticos inativos.")

# RESULTADO FINAL
if len(problemas) == 0:
    resultado = "PRONTO PARA DECOLAR"
else:
    resultado = "DECOLAGEM ABORTADA"

# ANÁLISE ENERGÉTICA
energia_disponivel = capacidade_total * (nivel_energia / 100)
energia_util = energia_disponivel * (1 - perdas / 100)
autonomia_restante = energia_util - consumo_decolagem

# SAÍDA
print()
print("===== RELATÓRIO OPERACIONAL DE PRÉ-DECOLAGEM =====")
print()

print("DADOS DA TELEMETRIA:")
print("Temperatura interna:", temperatura_interna, "°C")
print("Temperatura externa:", temperatura_externa, "°C")
print("Integridade estrutural:", integridade_estrutural)
print("Nível de energia:", nivel_energia, "%")
print("Pressão dos tanques:", pressao_tanques, "psi")
print("Módulos críticos:", modulos_criticos)
print()

print("RESULTADO DA MISSÃO:")
print(resultado)
print()

print("ANÁLISE ENERGÉTICA:")
print("Capacidade total:", capacidade_total, "kWh")
print("Energia disponível:", round(energia_disponivel, 2), "kWh")
print("Energia útil:", round(energia_util, 2), "kWh")
print("Autonomia restante:", round(autonomia_restante, 2), "kWh")
print()

if autonomia_restante > 0:
    print("Situação energética: ENERGIA SUFICIENTE")
else:
    print("Situação energética: ENERGIA INSUFICIENTE")

print()

print("FALHAS IDENTIFICADAS:")
if len(problemas) == 0:
    print("Nenhuma falha detectada.")
else:
    for problema in problemas:
        print("-", problema)