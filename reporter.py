from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime


class Reporter:
    def __init__(self, url, webdriver_path, x_arg):

        # Replace below path with the absolute path
        # to chromedriver in your computer
        self.driver = webdriver.Chrome(webdriver_path)

        self.driver.get(url)
        wait = WebDriverWait(self.driver, 600)

        wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

    def find_energies(self):

        surf_guru = self.driver.page_source
        soup = BeautifulSoup(surf_guru, features='html.parser')
        html_energies = soup.findAll("label", {"class": "resumo_energia_en"})
        week_energies = [html_energie.text for html_energie in html_energies]
        return week_energies

    def process_energies(self, raw_energies):

        p_energies = {}
        day = 0
        for energy in raw_energies:
            if 'J' in energy:

                date = datetime.datetime.today()
                date += datetime.timedelta(days=day)
                report_date = date

                energy = energy.replace('J', "")
                energy = energy.replace('▼', "")
                energy = energy.replace('▲', "")
                energy = int(energy)

                p_energies[report_date.strftime('%A, %d %b %Y')] = energy
                print(p_energies)
                day += 1

        return p_energies

    def __del__(self):
        self.driver.quit()
