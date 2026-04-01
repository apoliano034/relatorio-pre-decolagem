# Relatório Operacional de Pré-Decolagem

## Explicação do projeto
Este projeto simula a análise operacional de uma nave antes da decolagem, utilizando dados de telemetria, verificações lógicas em Python e análise energética. O objetivo principal é verificar se a nave está em condições seguras para decolar ou se a missão deve ser abortada.

O sistema analisa os seguintes parâmetros:
- temperatura interna;
- temperatura externa;
- integridade estrutural;
- nível de energia;
- pressão dos tanques;
- status dos módulos críticos.

Com base nesses dados, o programa compara os valores informados com faixas seguras previamente definidas. Caso todos os parâmetros estejam adequados, o resultado final será **PRONTO PARA DECOLAR**. Caso algum parâmetro esteja fora da faixa segura, o sistema informará **DECOLAGEM ABORTADA** e apresentará as falhas encontradas.

Além disso, o projeto também realiza uma análise energética, calculando:
- energia disponível;
- energia útil;
- autonomia restante.

A versão presente neste repositório é interativa, ou seja, o usuário digita os dados da missão no terminal, tornando a simulação mais dinâmica e permitindo testar diferentes cenários.

---

## Instruções de execução do código
Ao executar o programa, o sistema solicitará ao usuário os dados da missão, como:

temperatura interna;
temperatura externa;
integridade estrutural;
nível de energia;
pressão dos tanques;
módulos críticos;
capacidade total de energia;
consumo estimado na decolagem;
perdas energéticas.

Após o preenchimento, o programa exibirá:

os dados informados;
o resultado final da missão;
a análise energética;
as falhas identificadas, se houver.

Prints da execução:
Exemplo de entrada de dados:

===== SISTEMA DE PRÉ-DECOLAGEM =====
Digite os dados da missão:

Temperatura interna (°C): 22
Temperatura externa (°C): -35
Integridade estrutural (1 = íntegra / 0 = falha): 1
Nível de energia (%): 85
Pressão dos tanques (psi): 74
Módulos críticos (ativos ou inativos): ativos
Capacidade total de energia (kWh): 1200
Consumo estimado na decolagem (kWh): 700
Perdas energéticas (%): 8

Exemplo de saída do programa:

===== RELATÓRIO OPERACIONAL DE PRÉ-DECOLAGEM =====

DADOS DA TELEMETRIA:
Temperatura interna: 22 °C
Temperatura externa: -35 °C
Integridade estrutural: 1
Nível de energia: 85 %
Pressão dos tanques: 74 psi
Módulos críticos: ativos

RESULTADO DA MISSÃO:
PRONTO PARA DECOLAR

ANÁLISE ENERGÉTICA:
Capacidade total: 1200.0 kWh
Energia disponível: 1020.0 kWh
Energia útil: 938.4 kWh
Autonomia restante: 238.4 kWh

Situação energética: ENERGIA SUFICIENTE

FALHAS IDENTIFICADAS:
Nenhuma falha detectada.

### Requisitos
Para executar o projeto, é necessário ter:
- Python 3 instalado;
- VS Code, terminal ou outra IDE compatível.

### Executando o código
No terminal, execute:

```bash
python pre_decolagem.py
