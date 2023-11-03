# Analysis_by_Traveling-Waves

<img width="1189" alt="grap_abs" src="https://github.com/JavierRodriguezH/Analysis_by_Traveling-Waves/assets/142826929/69c1011d-865b-42f6-b112-5876df731f88">


Resources and extra documentation for the manuscript "Analysis by Traveling Waves for a Protection Scheme of Transmission Lines with a UPFC" published in IEEE Latin America Transactions. The code is organized by the type of programming language used in the project in the following order Matlab -> Python. The project hierarchy and folders description is as follows

MATLAB/Model: Simulink_models. The simulation file of the Simulink platform with .slx extension is attached. In this file you can modify the parameters of line length, inseption angles, fault resistance, fault type, UPFC compensation, to later run the simulation and save the values.
Python/code: The python codes are attached to carry out the process of reading the signals, fault detection, fault location and fault classification. The signals that are taken must be created before the model simulation.

# Instructions for running the code


1. Run the simulation file in Matlab called "analysis_TW_UPFC.slx", the parameters must be modified to the desired values to perform the experiment.
2. Saves in .csv files all the cases that must be considered for your fault detection analysis.
3. Running the python file "main.py" using the previously generated values will obtain the results corresponding to the failure. Data must be created and saved to create results data and statistical data.
