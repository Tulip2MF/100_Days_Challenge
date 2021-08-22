from add_country import add_new_country



travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

new_entry = add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

travel_log.append(new_entry)

print(travel_log)


