from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DM = DataManager()
sheet_data = DM.get_destination_data()
flight_search = FlightSearch()
notification=NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    DM.destination_data = sheet_data
    DM.update_destination_code()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
