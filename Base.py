from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import os

random_num = random.randint(1,5)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized");
chrome_options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("disable-infobars")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get('https://www.google.com/')

search_terms = [
    {
        "Subject": "Camping Tents",
        "Query": "camping tents allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8696']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7456']",
        "first_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a[1]",
        "second_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Hammocks",
        "Query": "camping hammocks allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8696']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7457']/a",
        "first_related_blog_items": "//*[@id='post-5281']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-5281']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Backpacks",
        "Query": "camping backpacks allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8692']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7459']/a",
        "first_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a",
        "second_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[4]/div/p/a"
    },
    {
        "Subject": "Camping Stoves",
        "Query": "camping stoves allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8697']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7461']/a",
        "first_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Tables",
        "Query": "camping tables allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8698']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7463']/a",
        "first_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Shower Tents",
        "Query": "camping shower tents allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8698']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7462']/a",
        "first_related_blog_items": "//*[@id='post-6312']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6312']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    }
]

search_box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_box.send_keys(f"{search_terms[random_num]['Query']}")
search_box.submit()

website_address = "allcamping-gears.com"

def scroll_up_down():
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))
            
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

all_results = driver.find_elements_by_class_name("iUh30")

for website in all_results:
    if website_address in website.text:
        website.click()

        scroll_up_down()

        navbar_dropdown = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown']}")

        hover = ActionChains(driver).move_to_element(navbar_dropdown)
        hover.perform()

        navbar_dropdown_items = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown_items']}")
        navbar_dropdown_items.click()

        vignette_url = "https://allcamping-gears.com/#google_vignette"

        if vignette_url in driver.current_url:
            driver.back()

            hover = ActionChains(driver).move_to_element(navbar_dropdown)
            hover.perform()

            navbar_dropdown_items = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown_items']}")
            navbar_dropdown_items.click()

            scroll_up_down()

            first_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['first_related_blog_items']}")

            first_related_blog_items.click();

            scroll_up_down()
            driver.back()

            second_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['second_related_blog_items']}")

            second_related_blog_items.click()

            scroll_up_down()
            driver.back()

            print("Python tasks completed successfully")