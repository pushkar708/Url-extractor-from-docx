from selenium import webdriver
import threading
import time, os

# Function to scroll a tab
def scroll_tab(driver):
    for _ in range(10):  # Scroll down 10 times
        driver.execute_script("window.scrollBy(0, 100);")  # Scroll down by 100 pixels
        time.sleep(1)  # Wait for a second before the next scroll

# Initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument(os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data'))
driver = webdriver.Chrome(options=options)

# Open the first tab
driver.get("https://www.github.com")  # Replace with your desired URL
time.sleep(2)  # Wait for the page to load

# Open a new tab and navigate to another URL
driver.execute_script("window.open('', '_blank');")  # Replace with your desired URL
time.sleep(2)  # Wait for the new tab to load

# Get handles for both tabs
handles = driver.window_handles

# Create threads for scrolling each tab
threads = []
for handle in handles:
    driver.switch_to.window(handle)  # Switch to each tab
    thread = threading.Thread(target=scroll_tab, args=(driver,))
    threads.append(thread)
    thread.start()  # Start scrolling in each tab

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Close the driver after scrolling
driver.quit()