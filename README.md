# Pre-Launch Operational Report

## Project Description
This project simulates the operational analysis of a spacecraft before launch using telemetry data, logical verification in Python, and energy analysis. The main goal is to determine whether the spacecraft is ready for launch or whether the mission must be aborted based on predefined safety conditions.

## Objective
Develop a simple Python-based system capable of:
- organizing telemetry data;
- checking whether mission parameters are within safe ranges;
- displaying the final mission result;
- calculating the initial energy autonomy;
- presenting detected failures, if any.

## Analyzed Parameters
The system checks the following telemetry data:
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

### `pre_decolagem_fixo.py`
A simple version with fixed values already defined in the code.

**Features:**
- easy to understand for beginners;
- useful for initial testing;
- ideal for generating execution prints for the report.

### `pre_decolagem_interativo.py`
An interactive version in which the user enters the mission data through the terminal.

**Features:**
- allows testing different scenarios;
- makes the simulation more dynamic;
- receives telemetry and energy data in real time.

### `pre_decolagem.ipynb`
Notebook version of the project for demonstration and documentation purposes.

### `relatorio.pdf`
Final PDF report containing the complete project explanation, pseudocode, calculations, and conclusions.

## System Logic
The program compares each input value with the safe mission ranges. When any parameter is outside the expected standard, a failure is added to the problem list. At the end:

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

## Technologies Used
- Python 3
- Jupyter Notebook
- VS Code
- GitHub

## How to Run

### Requirements
- Python 3 installed
- VS Code, terminal, or any compatible IDE

### Run the fixed version
```bash
python pre_decolagem_fixo.py
