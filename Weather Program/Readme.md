# **Weather Program**

The Weather Program is a simple Python application that fetches real-time weather information for any city using the OpenWeather API. It provides details such as temperature, weather condition, humidity, wind speed, and atmospheric pressure in a user-friendly format.

---

## **Overview**

This program is designed to give users quick and accurate weather updates from the command line. By entering the name of a city, users can retrieve its current weather conditions, presented in a clear and concise manner. The program is powered by the OpenWeather API and serves as a practical example of integrating APIs in Python.

---

## **Features**

1. **Real-Time Weather Information**:
   - Fetches up-to-date weather details directly from OpenWeather API.

2. **Key Weather Metrics**:
   - **Temperature**: Displays in Celsius by default.
   - **Condition**: A short description of the current weather (e.g., "clear sky").
   - **Humidity**: Provides the percentage of atmospheric moisture.
   - **Pressure**: Shows atmospheric pressure in hPa.
   - **Wind Speed**: Displays wind speed in meters per second.

3. **Error Handling**:
   - Handles invalid city names and network errors gracefully.
   - Provides descriptive messages for common issues like unauthorized API keys or connectivity problems.

4. **Environment Variable Integration**:
   - API keys are securely stored in a `.env` file, ensuring privacy and security.

---

## **How to Use**

### **Prerequisites**

1. **Python**:
   - Ensure Python 3.6 or later is installed on your system.

2. **Required Python Packages**:
   - `requests`: For making HTTP requests to the OpenWeather API.
   - `python-dotenv`: For loading environment variables from the `.env` file.

   Install the packages using pip:
   ```bash
   pip install requests python-dotenv
   ```

3. **OpenWeather API Key**:
   - Sign up for a free account at [OpenWeather](https://openweathermap.org/) to obtain an API key.

4. **Create a `.env` File**:
   - In the project directory, create a file named `.env` and add your API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

---

### **Steps to Run**

1. Open a terminal or command prompt and navigate to the project directory:
   ```bash
   cd Weather_Program
   ```

2. Run the script:
   ```bash
   python weather_program.py
   ```

3. Enter the name of the city when prompted:
   ```plaintext
   Enter the name of the city: London
   ```

4. View the weather details for the specified city.

---

## **Example Usage**

### **Input**:
```plaintext
Welcome to the Weather Program!
Enter the name of the city: New York
```

### **Output**:
```plaintext
Weather in New York:

Temperature: 22°C
Condition: partly cloudy
Humidity: 65%
Pressure: 1018 hPa
Wind Speed: 3.5 m/s
```

### **Error Handling**:
- **Invalid City**:
  ```plaintext
  Error: city not found
  ```
- **Missing or Invalid API Key**:
  ```plaintext
  Error: 401 Unauthorized - Invalid API key. Please check your .env file.
  ```

---

## **Code Walkthrough**

### **1. API Integration**
- The script uses the `requests` library to send a GET request to the OpenWeather API.
- The URL is dynamically constructed using the base API URL, city name, API key, and additional query parameters (`units=metric`).

```python
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
```

### **2. Environment Variable Management**
- The `dotenv` library securely loads the API key from the `.env` file, keeping it hidden from the source code.

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
```

### **3. Error Handling**
- The program checks for HTTP errors using `response.raise_for_status()` and handles specific error codes like `401 Unauthorized` or `404 Not Found`.

### **4. User-Friendly Output**
- The retrieved data is formatted into a clean, human-readable format with labeled metrics for easy interpretation.

---

## **Customization**

1. **Units of Measurement**:
   - By default, the temperature is displayed in Celsius. To switch to Fahrenheit, modify the `units` parameter in the API URL:
     ```python
     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
     ```

2. **Additional Weather Details**:
   - The OpenWeather API provides extensive weather data. To include more metrics, update the parsing logic:
     ```python
     uv_index = data["uvi"]  # Example: UV Index
     ```

3. **Enhanced UI**:
   - Add colors to the output using libraries like `colorama` for better readability.

---

## **Challenges You Can Try**

1. **Hourly Forecast**:
   - Extend the program to fetch hourly forecasts using OpenWeather's "One Call API."

2. **City Suggestions**:
   - Implement fuzzy matching to suggest city names for incorrect inputs.

3. **Graphical Interface**:
   - Build a GUI for the program using libraries like `Tkinter` or `PyQt`.

---

## **Learning Outcomes**

This project demonstrates how to:
- Use APIs in Python for real-world applications.
- Handle HTTP requests and errors.
- Securely manage sensitive data using environment variables.
- Format and display structured data to end users.

---

## **Future Enhancements**

- Add support for multiple cities in a single run.
- Integrate a search history to store previously queried cities.
- Include icons or visual indicators for weather conditions.

---

Enjoy exploring the weather of any city at your fingertips! 😊



## How to Contribute:
Feel free to fork this repository, add new features, or fix bugs. Submit a pull request to share your improvements!

---

## License:
This project is licensed under the MIT License.
