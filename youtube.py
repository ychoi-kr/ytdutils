from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class YouTube:

    def __init__(self):
        options = Options()
        #options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)


    def playlist(self, playlist_id):
        url = "https://www.youtube.com/playlist?list=" + playlist_id
        driver = self.driver
        driver.get(url)
        
        pl = driver.find_elements(By.CSS_SELECTOR, "ytd-playlist-video-renderer")
        
        ret = []
        for i in range(len(pl)):
            driver.execute_script(f"window.scrollTo(0, {100 * i});")
            duration = pl[i].find_element(By.XPATH, './/span[contains(@class, "time-status")]').text
            if len(duration.split(':')) == 2:
                duration = '0:' + duration
            videotitle = pl[i].find_element(By.CSS_SELECTOR, "#video-title")
            title = videotitle.text
            video_url = videotitle.get_attribute('href').split('&')[0]
            ret.append((title, video_url, duration))
        
        return ret


    def script(self, video_id):
        video_url = "https://youtube.com/watch?v=" + video_id
        driver = self.driver
        driver.get(video_url)
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = '추가 작업']"))
        )
        driver.find_element(By.XPATH, "//button[@aria-label = '추가 작업']").click()
        
        try:
            driver.find_element_by_xpath("//*[@id='items']/ytd-menu-service-item-renderer/tp-yt-paper-item").click()
        except NoSuchElementException:
            return "(No transcript)"
        
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='body']/ytd-transcript-body-renderer"))
        )
        transcript = driver.find_element_by_xpath("//*[@id='body']/ytd-transcript-body-renderer")
        
        return transcript.text


    def playlist_script(self, playlist_id):
        for row in self.playlist(playlist_id):
            dquo = "\""
            title = f'{row[0]}({row[1]})'
            print(title)
            print('-' * len(title))
            video_id = row[1].split('=')[1]
            print(self.script(video_id))
            print()


    def close(self):
        self.driver.close()


    def quit(self):
        self.driver.quit()

