from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()

# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.kayak.co.in/flights/MAA-DEL/2024-08-15?sort=bestflight_a'
driver.get(url)

driver.implicitly_wait(10)
try:
    button = driver.find_element(By.CLASS_NAME, 'Hv20-content')
    button.click()
    print("Cheapest clicked successfully.")
    time.sleep(3)
    print("Showed more results")
    clearall_btn = driver.find_element(By.CLASS_NAME,'yCz4')
    clearall_btn.click()
    time.sleep(3)
    indigo = driver.find_element(By.XPATH,'//*[@id="valueSetFilter-vertical-airlines-6E-label"]/div')
    indigo.click()
    show_more_btn = driver.find_element(By.CLASS_NAME, 'ULvh')
    show_more_btn.click()
    time.sleep(3)
    contents = driver.find_elements(By.CLASS_NAME, 'nrc6-main')
    cont_count = len(contents)
    print(cont_count)
    for content in contents:
        try:
            now_btn = content.find_element(By.CLASS_NAME, 'hJSA')
            now_btn.click()
        except Exception as e:
            print(f"Failed to click 'Now' button for flight: {e}")
        flight_details = driver.find_elements(By.CLASS_NAME, 'NxR6-plane-details')
        if 'IndiGo 562' in flight_details[0].text:
            print("Yes, this is the flight!")
            provider_details = driver.find_elements(By.CLASS_NAME, 'veIp-provider-name')
            price_details = driver.find_elements(By.CLASS_NAME, 'ehQI-provider-price')
            providers = []
            price = []
            for pro in provider_details:
                providers.append(pro.text)
            for pri in price_details:
                price.append(pri.text)
            print(str(dict(zip(providers, price))))

            time.sleep(2)
            break
        else:
            print("No, this is not the flight.")
            time.sleep(1)
            go_back_btn = driver.find_element(By.CLASS_NAME, 'jnTP-btn-wrapper')
            go_back_btn.click()

    time.sleep(3)

except Exception as e:
    print(f"Error occurred: {e}")

# Close the WebDriver
driver.quit()
