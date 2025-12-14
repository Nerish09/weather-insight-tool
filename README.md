# Weather Insight Tool

## Overview
Weather Insight Tool is a full-stack web application built using Python and Flask that allows users to search for real-time weather information by city. The application fetches live data from a third-party weather API and displays current conditions such as temperature, humidity, wind speed, and weather status in a clean, user-friendly interface.

This project started as a command-line application and was later refactored into a web application, allowing me to practice code reuse, clean architecture, and backend–frontend communication.

---

## Technologies Used
- Python
- Flask
- HTML
- CSS
- WeatherAPI (Third-party API)
- Git & GitHub

---

## Features
- Search weather by city name
- Real-time weather data using an external API
- Error handling for invalid city names and API failures
- Clean and responsive user interface
- Separation of backend logic and frontend presentation
- Both CLI and web-based versions supported

---

## How to Run the Project Locally

## 1. Clone the repository

git clone https://github.com/your-username/weather-insight-tool.git
cd weather-insight-tool

## 2. pip install -r requirements.txt

## 3. Add your API key
Open weather.py and add your WeatherAPI key:
API_KEY = "your_api_key_here"

## 4. Run the Flask app
python3 app.py

## 5. Open in browser
Go to:
http://127.0.0.1:5000

## 6. What I Learned

How to integrate and consume third-party APIs

How to  work with JSON data

Building backend logic using Flask

Separating business logic from UI for cleaner code

Handling API and user input errors gracefully

Refactoring a project from a CLI tool into a web application

Using Git and GitHub to manage and publish a project

## 7. Future Improvements

Add multi-day weather forecasts

Improve UI with icons and animations

Deploy the application online

Add automated tests for backend logic
