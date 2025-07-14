# Salah Time

## Overview
Salah Time is a web application built using Streamlit that displays Islamic prayer times and dates. The application retrieves data from a specified source URL and presents the current Gregorian and Hijri dates, along with the prayer times for the day, including Fajr, Zuhr, Maghrib, Sunrise, Asr, and Isha. Additionally, it calculates and displays the thirds of the night.

## Files
- **app.py**: The main application file that creates the web interface and displays the prayer times and dates.
- **scrape_time.py**: Contains functions for loading and processing prayer time data, including fetching data from the source and calculating the thirds of the night.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd awqaatus-Salah
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Set the environment variable for the source URL:
   ```
   export SOURCE_URL=<your-source-url>
   ```

## Usage
To run the application, execute the following command:
```
streamlit run app.py
```
Open your web browser and go to `http://localhost:8501` to view the application.

## License
This project is licensed under the MIT License.