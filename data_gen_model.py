from faker import Faker
import pandas as pd
import random
import datetime
from sklearn.model_selection import train_test_split

fake = Faker()

def generate_weather_data(num_readings):
    readings = []
    for _ in range(num_readings):
        timestamp = fake.date_time_this_year()  # Generate a timestamp within the current year
        city = fake.city()
        
        # Generate weather parameters
        weather_params = {
            'temperature': random.uniform(-20.0, 50.0),  # Example range for temperature in Celsius
            'humidity': random.uniform(0.0, 100.0),  # Example range for humidity in percentage
            'pressure': random.uniform(900.0, 1100.0),  # Example range for pressure in hPa
            'wind_speed': random.uniform(0.0, 30.0),  # Example range for wind speed in m/s
            'precipitation': random.uniform(0.0, 50.0),  # Example range for precipitation in mm
            'cloud_cover': random.uniform(0.0, 100.0),  # Example range for cloud cover in percentage
            'visibility': random.uniform(0.0, 50.0),  # Example range for visibility in km
            'uv_index': random.randint(0, 10),  # Example range for UV index
            'air_quality_index': random.randint(0, 500),  # Example range for air quality index
            'pollen_count': random.randint(0, 1000)  # Example range for pollen count
            # add more parameters if needed
        }

        # Append weather readings to the list
        for param, value in weather_params.items():
            readings.append({'timestamp': timestamp, 'city': city, 'parameter': param, 'value': value})
    return readings

# Generate synthetic weather data
weather_data = generate_weather_data(200000)

# Convert to pandas DataFrame
df = pd.DataFrame(weather_data)

# Save the weather data to a CSV file
df.to_csv('weather_data.csv', index=False)

# Display the first few rows of the DataFrame
print(df.head())

# Split the data into training, validation, and test sets
train_ratio = 0.7  # 70% of the data for training
validation_ratio = 0.15  # 15% of the data for validation
test_ratio = 0.15  # 15% of the data for testing

# Split the data into training and the rest
train_data, rest_data = train_test_split(df, test_size=1 - train_ratio, random_state=42)

# Split the rest into validation and test sets
validation_data, test_data = train_test_split(rest_data, test_size=test_ratio / (validation_ratio + test_ratio), random_state=42)

# Display the sizes of the resulting datasets
print("Training data size:", len(train_data))
print("Validation data size:", len(validation_data))
print("Test data size:", len(test_data))

# Save the data splits to files
train_data.to_csv('train_weather_data.csv', index=False)
validation_data.to_csv('validation_weather_data.csv', index=False)
test_data.to_csv('test_weather_data.csv', index=False)

# Save the data splits to Excel files
#train_data.to_excel('train_weather_data.xlsx', index=False)
#validation_data.to_excel('validation_weather_data.xlsx', index=False)
#test_data.to_excel('test_weather_data.xlsx', index=False)
