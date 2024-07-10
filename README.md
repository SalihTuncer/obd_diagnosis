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

| Protocol | Description                            |
|:---------|:---------------------------------------| 
| 0        | Automatic                              |
| 1        | SAE J1850 PWM (41.6 kbaud)             |
| 2        | SAE J1850 VPW (10.4 kbaud)             |
| 3        | ISO 9141-2 (5 baud init)               |
| 4        | ISO 14230-4 KWP (5 baud init)          |
| 5        | ISO 14230-4 KWP (fast init)            |
| 6        | ISO 15765-4 CAN (11 bit ID, 500 kbaud) |
| 7        | ISO 15765-4 CAN (29 bit ID, 500 kbaud) |
| 8        | ISO 15765-4 CAN (11 bit ID, 250 kbaud) |
| 9        | ISO 15765-4 CAN (29 bit ID, 250 kbaud) |
| 10       | SAE J1939 CAN (29 bit ID, 250* kbaud)  |
| 11       | USER1 CAN (11* bit ID, 125* kbaud)     |
| 12       | USER2 CAN (11* bit ID, 50* kbaud)      |

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

## Usage

1. Connect your OBD II adapter to your car's OBD II port
2. Open the URL http://localhost:8000/api/v1/docs in your browser for the Swagger UI
3. You can use the Swagger UI to interact with the API or you can make requests on your own way.