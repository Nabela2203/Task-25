from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import chromedriver_autoinstaller

class Imdb:
    def search_all(self, search_query, from_date, to_date, bday):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(10)
        driver.get("https://www.imdb.com/search/name/")
        wait = WebDriverWait(driver,15)
        actions = ActionChains(driver)

        # sign-in pop-up
        signin = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Close']")))
        signin.click()

        # to perform a series of page down and to avoid auto scrolling after each entry
        for _ in range(15):
            actions.send_keys(Keys.DOWN).perform()

        # Input Boxes
        name_box = wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Name']")))
        name_box.click()
        enter_name_box = wait.until(EC.presence_of_element_located((By.NAME,"name-text-input")))
        enter_name_box.send_keys(search_query)

        for _ in range(5):
            actions.send_keys(Keys.DOWN).perform()

        # Select Boxes - Birth date
        birth_date = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Birth date']")))
        birth_date.click()
        enter_from_date = wait.until(EC.presence_of_element_located((By.NAME,"birth-date-start-input")))
        enter_from_date.send_keys(from_date)
        enter_to_date = wait.until(EC.presence_of_element_located((By.NAME, "birth-date-end-input")))
        enter_to_date.send_keys(to_date)

        for _ in range(5):
            actions.send_keys(Keys.DOWN).perform()

        # Birthday
        birth_day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Birthday']")))
        birth_day.click()
        day_text_box = wait.until(EC.presence_of_element_located((By.NAME, 'birthday-input')))
        day_text_box.send_keys(bday)

        # Click the Search button
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//button/span[text()="See results"]')))
        search_button.click()

        exp_url = "https://www.imdb.com/search/name/?name=Aysha&birth_date=1960-01-01,1965-12-31&birth_monthday=01-06"

        # Wait for the search results page to load
        if driver.current_url == exp_url:
           print(f"SUCCESS: Performed {search_query} Name Search")

        # Close the browser window
        driver.quit()

imdb_search = Imdb()
imdb_search.search_all("Aysha", "01-01-1960", "31-12-1970", "01-06")