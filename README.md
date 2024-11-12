# Automated Mosquito Larvae Production System

This repository contains code and instructions for building an automated mosquito larvae production system. The system is designed to produce larvae for fish feed while minimizing mosquito population growth.

## GPIO Connections

Set up the components by connecting them to the Raspberry Pi GPIO pins as follows:

- **Valve**: Connect to GPIO pin 17.
- **Pump**: Connect to GPIO pin 22.
- **Limit Switch**: Connect to GPIO pin 27 (used to sense the valve position).

## Usage

### Running the System

To initiate the system, execute the main control script. This will manage the valves, pump, and sensors to automate the larvae production process.

### Schedule and Cycle Intervals

The script automates the following sequence:

1. **Open the Valve** once a week to empty the primary tank.
2. **Filter Larvae** and refill the primary tank using the pump.
3. **Clean Up** GPIO settings at the end of each cycle.

The weekly timing interval is defined by the `secondi_settimana` variable in `main.py`. Adjust this variable to change the cycle frequency.

#### Cycle Summary

- **Valve Opens**: Water flows from the primary tank to the secondary tank.
- **Filter Larvae**: A fine-mesh filter traps larvae in the secondary tank.
- **Pump Activates**: Water is pumped back to the primary tank.
- **Weekly Repeat**: The system resets to start the cycle again the next week.

## Code Structure

- **main.py**: Core control script that:
  - Manages GPIO pins and cycle timing.
  - Logs activity and any errors to `data/RPI_SH.log`.
  - Contains functions to open/close the valve, activate/deactivate the pump, and check the limit switch.

- **start_mosq_trap.sh**: Shell script to launch the Python script. Make this file executable before running.

## Detailed File Explanations

### GPIO Setup

- **valvola_pin (Pin 17)**: Controls the valve.
- **finecorsa_pin (Pin 27)**: Reads the limit switch state to determine the valve position.
- **pompa_pin (Pin 22)**: Controls the pump for water refilling.

### Timing and Cycle Management

- **secondi_settimana**: Configurable interval for the weekly cycle.
- **secondi_svuotamento** and **secondi_pompaggio**: Control the timing for the valve and pump.

### Logging

The system logs temperature, cycle start times, and errors to `RPI_SH.log` for troubleshooting purposes.

## License

This project is open-source and available under the MIT License.

By following this guide, you should be able to create a functional, automated mosquito larvae production system for fish feed that minimizes the risk of mosquito population growth. Happy building!