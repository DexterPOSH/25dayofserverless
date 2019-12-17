# Posadas

This is the repository housing the JSON file containing the posadas information.
Each posadas entry should follow below format.

Create a json entry like below and append to the list in the [posadas.json](./posadas.json)

```json
{
    "day": 1,
    "host": "HostName here",
    "address": {
        "area": "area name here",
        "landmark": "nearest landmark",
        "city": "city name",
        "state": "state name",
        "codigopostal": "768792"
    }

}
```

- day field is for the day of the Posadas
- host field represents the host of the posadas
- address - enter the detailed address for hosting the posadas
    - area - area in which the posadas is being hosted
    - landmark - nearest landmark
    - city - city name
    - state - state name
    - codigopostal - zip code of the area