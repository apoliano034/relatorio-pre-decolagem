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

### Requisitos
Para executar o projeto, é necessário ter:
- Python 3 instalado;
- VS Code, terminal ou outra IDE compatível.

### Executando o código
No terminal, execute:

```bash
python pre_decolagem.py
