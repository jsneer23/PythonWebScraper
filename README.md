# PythonWebScraper
This is a python web scraper that collects match data from FIRST Robotics Competition events and saves it in a json file.

An example has been scraped for the 2024 San Francisco Regional Qualifier [event website](https://frc-events.firstinspires.org/2024/CASF/qualifications) and the results can be found in the json folder.

## Installation Instructions

1. Create python virtual envionment in VS Code using CMD+Shift+P Python: Create Environment
2. Activate the environment in the terminal using source .venv/bin/activate
3. Install crawl4ai in the terminal using

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Use Instructions

1. Set the year, event code, and match type of the desired matches in main.py
2. Run the code in main.py
3. Results will appear in the json folder