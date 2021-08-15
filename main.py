from selenium import webdriver
import time
import pandas
import datetime
chrome_driver = "C:/Users/91755/Downloads/chromedriver"
class Internet:
    def __init__(self):
        self.web = webdriver.Chrome(executable_path=chrome_driver)

    def speed_check(self):
        self.web.get("https://www.speedtest.net")
        time.sleep(3)
        start=self.web.find_element_by_class_name(name="start-text")
        start.click()
        time.sleep(50)
        try:
            file = pandas.read_csv("./data.csv")
        except FileNotFoundError:
            k = {
                "date":[],
                "down":[],
                "up":[]
            }
            data = pandas.DataFrame(k)
            data.to_csv("./data.csv",index=False)
        down = self.web.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        up = self.web.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        file = pandas.read_csv("./data.csv")
        val = file.to_dict(orient="list")
        today= datetime.datetime.now()
        today= str(today).split()[0]
        val['date'].append(today)
        val['down'].append(down)
        val['up'].append(up)
        df = pandas.DataFrame(val)
        df.to_csv("./data.csv",index=False)
        self.web.close()
internet = Internet()
internet.speed_check()