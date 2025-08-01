# CLI Weather App
This project is to learn api calls and how requests works..

A clean and simple command-line application to get the current weather for any city in the world, by using the [OpenWeatherMap API](https://openweathermap.org/api).

This project demonstrates how to interact with external APIs and manage secret keys securely using a `.env` file.

---

## ✨ Features

- Fetches real-time weather data
- Displays temperature in Celsius
- Shows weather conditions and humidity
- Securely manages API keys, keeping them out of the main codebase

---

## 🧰 Prerequisites

- Python 3.8+
- [`uv`](https://github.com/astral-sh/uv) installed on your system
- An API key from [OpenWeatherMap](https://openweathermap.org/)

---

## ⚙️ Setup & Installation

1. **Clone the repository:**

```
git clone [<your-repository-url>](https://github.com/HackSmith010/CLI-Weather-App.git)
cd CLI-Weather-App
```

2. **Install dependencies:**

This command reads the pyproject.toml file and installs the necessary packages (requests, python-dotenv):
```
uv pip sync
```

3. **Create the environment file:**

Create a .env file in the root directory and add your API key:
```
OPENWEATHER_API_KEY='YOUR_ACTUAL_API_KEY_HERE'
```
The main.py script is configured to automatically load this key.

## 🚀 Usage
```
uv run main.py
```
The application will prompt you to enter a city name.

## 💡 Example Interaction

```
Welcome to the Weather App
----------------------------------------------

Enter the city name: London

Weather in London:
  Condition: Clouds (overcast clouds)
  Temperature: 14.5°C
  Humidity: 82%
```

## 📁 Project Structure
```
.
├── main.py          # The main application script
├── pyproject.toml   # Project configuration and dependencies
├── README.md        # This file
├── uv.lock          # Lockfile for reproducible installs
└── .env             # (You create this) For storing secret keys
```

