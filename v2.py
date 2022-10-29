from time import sleep
from os import mkdir
import urllib


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleWebCrawler():
    def __init__(self,phrase):
        self.driver=webdriver.Chrome()
        self.phrase=phrase


    def download(self,pcount):
        self.driver.get(f'https://duckduckgo.com/?q={self.phrase}&iax=images&ia=images')
        sleep(3)


        for i in range(1, pcount+1):
            while 1:
                try:
                    self.driver.find_element(By.XPATH,f'//*[@id="zci-images"]/div[1]/div[2]/div/div[{i}]').click()
                except:
                    pass
                else:
                    break

            sleep(1)
            try:
                mkdir('C:/Users/IT/Pictures/imagedownloader')
            except:
                pass
            try:
                self.driver.find_element(By.XPATH,f'//*[@id="zci-images"]/div[2]/div/div[1]/div[{1 if i==1 else 2}]/div/div[1]/div/a/img[2]').click() # .get_attribute('href')
                src = self.driver.find_element(By.XPATH,'/html/body/img').get_attribute('src')
                urllib.urlretrieve(src,f'C:/Users/IT/Pictures/imagedownloader/{self.phrase} {i}.png')
            except:
                pass
        self.driver.quit()
def run():
    while 1:
        try:
            n = int(input('count: '))
        except TypeError:
            print('please enter a number!')
        p = input('Phrase: ')
        imagetaker= GoogleWebCrawler(p)
        imagetaker.download(n)
if __name__ == '__main__':
    run()