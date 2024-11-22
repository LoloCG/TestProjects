# this code is ABANDONED. Does not work, and there are many things that require fixing...
# What it was supposed to do, and what it could manage to do:
#   I wanted to use it to get fluctuations on product prices over long periods
#   Managed to scrape the prices of products and the selected options.
#  
# The main problem and reason on why it was abandoned:
#   Aliexpress has a welcome deal discount that cannot be removed without login in.
#   As im no expert in datascrapping, at least knowing just the minimum, i couldnt pass
#       the aliexpress login dialog or load the cookies for the prices to be shown correctly.
#   The oficial solution would be to use the oficial APIs, registering as a dev, but i dont want to...
#  

import json
import datetime
from dotenv import load_dotenv 
import os
import pickle

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.aliexpress.com/item/1005006975464963.html" # Example page with multiple options


def main():
    driver = start_webdriver(headless=False)
    print(f"Opening URL: {URL}")
    driver.get(URL)
    # ==================== Non-Specific item data ====================
    
    item = {}
    item["URL"] = URL
    item["title"] = driver.title
    item_options = check_item_options(driver)
    item["all_options"] = item_options
    
    # ==================== Selected item data ====================
    
    selected_item_properties = get_selected_properties(driver)
    print(f"selected_item_properties: {selected_item_properties}")
    item_prices = get_prices(driver)
    print(f"selected_item_prices: {item_prices}")

    prices = {}
    key_as_string = "; ".join(selected_item_properties)
    prices[key_as_string] = item_prices

    item["prices"] = prices

    save_as_json(data=item)
    
    # ========================= Finalization ========================= 
    
    print("Closing driver.")
    driver.close()

class AliexProductScrapper:
    def __init__(self, product_url, headless=False):
        self.product_url = product_url
        self.driver = self.start_webdriver(headless)

        self.driver.get(URL)

        self.product_info = {}
        self.product_info["URL"] = URL
        self.product_info["title"] = self.driver.title

    def start_webdriver(self, headless=False):
        options = FirefoxOptions()

        print(f"Initiating Firefox WebDriver{ ' in headless mode.' if headless else '.' }")
        if headless == True:
            options.add_argument("-headless") 
        else:
            options.add_argument("--window-size=1024,768") # reduce window size

        options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
        options.set_preference("permissions.default.image", 2)  # Disable image loading
        options.set_preference("browser.startup.homepage", "about:blank")  # Skip homepage

        self.driver = webdriver.Firefox(options=options)
        
        return self

    def save_all_item_options(self):
        item_options_raw = []
        n = 1
        while True:
            try:
                css_selector = f"div.sku-item--property--HuasaIz:nth-child({n})"
                property_element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
                property_text = property_element.text
                item_options_raw.append(property_text)

            except NoSuchElementException:
                break

            except Exception as e:
                print(f"An error occurred: {e}")

            n += 1

        item_options = {}

        for options_raw in item_options_raw:
            key, values = options_raw.split(":", 1)
            values_list = list(dict.fromkeys(values.strip().split("\n")))
            item_options[key.strip()] = values_list

        self.product_info["all_options"] = item_options

        return self

    def select_options(self):
        pass

    def save_currently_selected_options(self):
        selected_item_options = []
        n = 1
        while True:
            try:
                css_selector = f"div.sku-item--property--HuasaIz:nth-child({n}) > div:nth-child(1)"
                option_element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
                option_text = property_option.text
                selected_item_options.append(option)

            except NoSuchElementException:
                break

            except Exception as e:
                print(f"An error occurred: {e}")

            n += 1

        return selected_item_options

    def save_prices(self):
        selectors = {
            "current_price": ".price--currentPriceText--V8_y_b5",
            "past_price": ".price--originalText--gxVO5_d",
            "discount": ".price--discount--Y9uG2LK"
        }
        
        prices = {}
        for key, selector in selectors.items():
            try:
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                prices[key] = element.text
            except NoSuchElementException:
                # If the element is not found, assign None to indicate it's missing
                prices[key] = None
        
        return prices

# ========================= UNUSED/UNFINISHED ========================= 

def ask_aliexpress_signup(driver): # UNUSED/UNFINISHED
    URL = "https://www.aliexpress.com"
    print(f"Opening URL: {URL}")
    driver.get(URL)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".my-account--menuItem--1GDZChA"))
    )
    print(f"Please register with your account to save session for future use.")
    input(f"Press Enter once registered.")
    
    driver.maximize_window()
    driver.switch_to.window(driver.current_window_handle)    
    
    save_cookies(driver)

def load_cookies(driver, URL, cookie_file="cookies.json"): # UNUSED/UNFINISHED
    print(f"Opening URL: {URL}")
    driver.get(URL)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".my-account--menuItem--1GDZChA"))
    )

    try:
        # Open and read the cookie file
        with open(cookie_file, "r") as file:
            cookies = json.load(file)
        
        # Add each cookie to the browser
        for cookie in cookies:
            driver.add_cookie(cookie)
        
        print("Cookies loaded successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{cookie_file}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file '{cookie_file}' contains invalid JSON.")
    except Exception as e:
        print(f"Error loading cookies: {e}")

    driver.refresh()

    return driver
        
def save_cookies(driver): # UNUSED/UNFINISHED
    print("Saving cookies of the session.")
    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))
    
    time.sleep(10)
    
    return

# ========================= helper functions ========================= 
def save_as_json(data, file_name="product_data.json"):
    try:
        print(f"Saving data into json as {file_name}.")
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"An error occurred while writing to JSON: {e}")
        return False

def open_config(key=None, default_value=""):
    try:
        if os.path.exists("config.json"):
            try:      
                with open("config.json", "r", encoding="utf-8") as config_file:
                    config = json.load(config_file)
                    
                if key == None: return config
                if key in config: return config[key]
            
            except json.JSONDecodeError:
                config = {}
        else:
            print(f"config.json not found.")
            config = {}        

        # If the key does not exist, add it with the default value
        print(f'Adding key "{key}" with default value "{default_value}" to config.json file.')
        config[key] = default_value
        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)

        return default_value

    except Exception as e:
        print(f"error obtaining config: {e}")
        return None

def save_config(data):
    if os.path.exists("config.json"):
        # Load existing content
        with open("config.json", "r", encoding="utf-8") as config_file:
            try:
                existing_data = json.load(config_file)
            except json.JSONDecodeError:
                existing_data = {}  # If the file is empty or invalid JSON
    else:
        existing_data = {}

    existing_data.update(data)

    with open("config.json", "w", encoding="utf-8") as config_file:
        json.dump(existing_data, config_file, indent=4)  

if __name__ == '__main__':
    main()
