#PORTUGUESE

# Relatório Operacional de Pré-Decolagem

## Descrição do projeto
Este projeto simula a análise operacional de uma nave antes da decolagem, utilizando dados de telemetria, verificações lógicas em Python e análise energética. O objetivo é determinar se a nave está apta para decolar ou se a missão deve ser abortada com base em condições de segurança previamente definidas.

## Objetivo
Desenvolver uma solução simples em Python capaz de:
- organizar os dados da telemetria;
- verificar se os parâmetros da missão estão dentro das faixas seguras;
- indicar o resultado final da missão;
- calcular a autonomia energética inicial;
- apresentar as falhas encontradas, se houver.

## Parâmetros analisados
Os dados verificados pelo sistema são:
- temperatura interna;
- temperatura externa;
- integridade estrutural;
- nível de energia;
- pressão dos tanques;
- status dos módulos críticos.

## Faixas seguras utilizadas
- Temperatura interna: de 18 °C a 27 °C
- Temperatura externa: de -50 °C a 50 °C
- Integridade estrutural: igual a 1
- Nível de energia: mínimo de 60%
- Pressão dos tanques: de 70 a 90 psi
- Módulos críticos: ativos

## Arquivos do projeto

### 1. `pre_decolagem`
Versão interativa em que o usuário digita os dados da missão pelo terminal.

#### Características:
- permite testar diferentes cenários;
- torna a simulação mais dinâmica;
- recebe os dados da telemetria e os dados energéticos em tempo real.

## Lógica do sistema
O programa compara cada dado informado com as faixas seguras da missão. Quando algum valor está fora do padrão, uma falha é adicionada à lista de problemas. Ao final:

- se não houver falhas, o resultado é `PRONTO PARA DECOLAR`;
- se houver uma ou mais falhas, o resultado é `DECOLAGEM ABORTADA`.

Além disso, o sistema realiza a análise energética com base em:
- capacidade total de energia;
- carga atual;
- consumo estimado na decolagem;
- perdas energéticas.

## Cálculos energéticos
O programa calcula:
1. **Energia disponível**
2. **Energia útil**
3. **Autonomia restante**

### Fórmulas utilizadas
- Energia disponível = capacidade total × (nível de energia / 100)
- Energia útil = energia disponível × (1 - perdas / 100)
- Autonomia restante = energia útil - consumo de decolagem

## Como executar

### Requisitos
- Python 3 instalado
- VS Code, terminal ou qualquer IDE compatível

### Executando a versão fixa
No terminal, use:

```bash
python pre_decolagem.py



#ENGLISH

# Pre-Launch Operational Report

## Project Description
This project simulates the operational analysis of a spacecraft before launch, using telemetry data, logical checks in Python, and energy analysis. The goal is to determine whether the spacecraft is ready for launch or whether the mission must be aborted based on previously defined safety conditions.

## Objective
Develop a simple Python solution capable of:
- organizing telemetry data;
- checking whether mission parameters are within safe ranges;
- indicating the final mission result;
- calculating the initial energy autonomy;
- presenting any detected failures, if applicable.

## Analyzed Parameters
The data checked by the system includes:
- internal temperature;
- external temperature;
- structural integrity;
- energy level;
- tank pressure;
- status of critical modules.

## Safe Ranges Used
- Internal temperature: from 18 °C to 27 °C
- External temperature: from -50 °C to 50 °C
- Structural integrity: equal to 1
- Energy level: minimum of 60%
- Tank pressure: from 70 to 90 psi
- Critical modules: active

## Project Files

### 1. `pre_decolagem`
Interactive version in which the user enters the mission data through the terminal.

#### Features:
- allows testing different scenarios;
- makes the simulation more dynamic;
- receives telemetry and energy data in real time.

## System Logic
The program compares each input value with the mission’s safe ranges. When any parameter is outside the expected standard, a failure is added to the problem list. At the end:

- if there are no failures, the result is `READY FOR LAUNCH`;
- if there is one or more failures, the result is `LAUNCH ABORTED`.

In addition, the system performs energy analysis based on:
- total energy capacity;
- current charge level;
- estimated launch consumption;
- energy losses.

## Energy Calculations
The program calculates:
1. **Available Energy**
2. **Useful Energy**
3. **Remaining Autonomy**

### Formulas Used
- Available Energy = total capacity × (energy level / 100)
- Useful Energy = available energy × (1 - losses / 100)
- Remaining Autonomy = useful energy - launch consumption

## How to Run

### Requirements
- Python 3 installed
- VS Code, terminal, or any compatible IDE

### Running the fixed version
In the terminal, use:

```bash
python pre_decolagem.py

