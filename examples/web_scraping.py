import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
system = platform.system()
if system == "Darwin":  # macOS
    driver = webdriver.Safari()
    print("System iOS wykryty - uruchamiamy Safari.")
else:  # Windows, Linux, Android (domyślnie uruchomimy Chrome)
    driver = webdriver.Chrome()
    print("System inny niż iOS - uruchamiamy Chrome.")

driver.get("https://www.onet.pl")
print("Otwieram Onet...")
time.sleep(4)

# Pobierz tytuły artykułów
naglowki = driver.find_elements(By.XPATH, '//h2 | //h3')
print("\n Nagłówki z Onet.pl:")
for naglowek in naglowki[:10]:
    print("-", naglowek.text)
driver.quit()
