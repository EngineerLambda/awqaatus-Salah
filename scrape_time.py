import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def load_data(url:str)->dict:
    resp = requests.get(url)
    cont = resp.content

    soup = BeautifulSoup(cont, "html.parser")


    oyinbo_date = soup.find("div", class_="pt-date font-dark font-sm").p.text
    hijra_date = soup.find("div", class_="pt-date font-dark font-sm").find("p", class_="font-weight-bold pt-date-right").text

    fajr_time = soup.find("div", class_="prayerTiles fajar-tile").p.find("span", class_="prayertime").text
    sunrise_time = soup.find("div", class_="prayerTiles sunrise-tile").p.find("span", class_="prayertime").text
    zuhr_time = soup.find("div", class_="prayerTiles dhuhar-tile").p.find("span", class_="prayertime").text
    asr_time = soup.find("div", class_="prayerTiles asr-tile").p.find("span", class_="prayertime").text
    maghrib_time = soup.find("div", class_="prayerTiles maghrib-tile").p.find("span", class_="prayertime").text
    isha_time = soup.find("div", class_="prayerTiles isha-tile").p.find("span", class_="prayertime").text


    final_dict = {
        "oyinbo_date" : oyinbo_date.replace("\xa0", " "),
        "hijra_date" : hijra_date.replace("\xa0", " "),
        "fajr_time" : fajr_time,
        "sunrise_time" : sunrise_time,
        "zhur_time" : zuhr_time,
        "asr time" : asr_time,
        "maghrib_time" : maghrib_time,
        "isha_time" : isha_time
    }
    return final_dict


def split_thirds(prayer_times: dict) -> dict:
    # Extract Maghrib and Fajr times
    maghrib_str = prayer_times["maghrib_time"]
    fajr_str = prayer_times["fajr_time"]

    # Parse them into datetime objects using 12-hour format with AM/PM
    maghrib_time = datetime.strptime(maghrib_str.strip(), "%I:%M %p")
    fajr_time = datetime.strptime(fajr_str.strip(), "%I:%M %p")

    # If Fajr is earlier than Maghrib, it's the next day
    if fajr_time <= maghrib_time:
        fajr_time += timedelta(days=1)

    # Compute thirds
    night_duration = fajr_time - maghrib_time
    one_third = night_duration / 3

    first_third_start = maghrib_time
    first_third_end = first_third_start + one_third

    second_third_start = first_third_end
    second_third_end = second_third_start + one_third

    last_third_start = second_third_end
    last_third_end = fajr_time

    # Format results
    thirds = {
        "first_third": (first_third_start.strftime("%I:%M %p"), first_third_end.strftime("%I:%M %p")),
        "second_third": (second_third_start.strftime("%I:%M %p"), second_third_end.strftime("%I:%M %p")),
        "last_third": (last_third_start.strftime("%I:%M %p"), last_third_end.strftime("%I:%M %p")),
    }
    return thirds

