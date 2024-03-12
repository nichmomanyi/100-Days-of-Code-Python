from data_manager import DataManager

DM = DataManager()
sheet_data = DM.get_destination_data()
#print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    DM.destination_data = sheet_data
    DM.update_destination_code()
