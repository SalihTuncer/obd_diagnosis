# OBD II Diagnosis Tool

This tool is designed to help you diagnose your car's OBD II system. It is a simple tool that can be used to read and
clear diagnostic trouble codes (DTCs) from your car's OBD II system. It can also display live data from your car's
sensors and perform various tests on your car's systems. This tool is not designed to replace professional diagnostic
equipment, but it can be a useful tool for diagnosing simple problems with your car's OBD II system. It is also not my
purpose to make any money from this tool, so it is completely free to use. I hope you find it useful! If you have any
questions or feedback, please feel free to contact me.

## Features

- Read and clear diagnostic trouble codes (DTCs)
- Display live data from your car's sensors
- Perform various tests on your car's systems
- Completely free to use! No ads or in-app purchases
- No internet connection required
- No special permissions required
- No data tracking
- No registration or sign-up required
- No personal information required

## Requirements

- An OBD II adapter (Any ELM327 adapter should work)
- A car with an OBD II system

## Supported Protocols

- ISO 9141-2
- ISO 14230-4 (KWP2000)
- ISO 15765-4 (CAN)
- SAE J1850 VPW
- SAE J1850 PWM
- SAE J1939 (Heavy Duty Vehicles)

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SalihTuncer/obd_diagnosis.git
   ```
2. Create a virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate the virtual environment

   3.1 With Windows
   ```sh
   .\venv\Scripts\activate
   ```

   3.2 With Linux/Mac
   ```sh
    source venv/bin/activate
   ```

4. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```

5. Run the application via
   ```sh
   python3 main.py 
   ```

