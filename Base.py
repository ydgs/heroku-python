from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

random_num = random.randint(1,5)

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_argument("--start-maximized");
chrome_options.add_argument("--headless")
chrome_options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')

search_terms = [
    {
        "Subject": "Camping Tents",
        "Query": "camping tents allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8696']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7456']",
        "page_link": "https://allcamping-gears.com/camping-tents/",
        "first_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a[1]",
        "second_related_blog_items": "//*[@id='post-4358']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Backpacks",
        "Query": "camping backpacks allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8692']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7459']/a",
        "page_link": "https://allcamping-gears.com/camping-backpacks/",
        "first_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a",
        "second_related_blog_items": "//*[@id='post-5954']/div/div/div/section/div/div/div/section/div/div[3]/div/div[4]/div/p/a"
    },
    {
        "Subject": "Camping Stoves",
        "Query": "camping stoves allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8697']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7461']/a",
        "page_link": "https://allcamping-gears.com/camping-stoves/",
        "first_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6179']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
    },
    {
        "Subject": "Camping Tables",
        "Query": "camping tables allcamping-gears.com",
        "navbar_dropdown": "//*[@id='menu-item-8698']/a",
        "navbar_dropdown_items": "//*[@id='menu-item-7463']/a",
        "page_link": "https://allcamping-gears.com/camping-tables-and-chairs/",
        "first_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[2]/div/p/a",
        "second_related_blog_items": "//*[@id='post-6310']/div/div/div/section/div/div/div/section/div/div[3]/div/div[3]/div/p/a"
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

CPG_website = ""

for website in all_results:
    if (website.text == "https://allcamping-gears.com"):
        CPG_website = website;
    # if website_address in website.text:
    #     website.click()

    #     scroll_up_down()

        # navbar_dropdown = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown']}")

        # print(navbar_dropdown)

        # hover = ActionChains(driver).move_to_element(navbar_dropdown)
        # hover.perform()

        #navbar_dropdown_items = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown_items']}")
        #navbar_dropdown_items.click()

        # s1 = driver.find_element_by_css_selector('li.menu-item-7456')
        # s1.click()

        # print(s1)

        # elems = driver.find_elements_by_xpath("//a[@href]")
        # for elem in elems:
        #     print(elem.get_attribute("href"))

        # vignette_url = "https://allcamping-gears.com/#google_vignette"

        # if vignette_url in driver.current_url:
        #     driver.back()

        #     # hover = ActionChains(driver).move_to_element(navbar_dropdown)
        #     # hover.perform()

        #     navbar_dropdown_items = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown_items']}")
        #     navbar_dropdown_items.click()

        #     scroll_up_down()

        #     # first_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['first_related_blog_items']}")

        #     # first_related_blog_items.click();

        #     # scroll_up_down()
        #     # driver.back()

        #     # second_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['second_related_blog_items']}")

        #     # second_related_blog_items.click()

        #     # scroll_up_down()
        #     # driver.back()

        #     print("Python tasks completed successfully")


print(CPG_website)
CPG_website.click()
scroll_up_down()

navbar_dropdown = driver.find_element_by_xpath(f"{search_terms[random_num]['navbar_dropdown']}")
print(navbar_dropdown)


elems = driver.find_elements_by_xpath("//a[@href]")

Dropdown_item = ""

for elem in elems:
    if (elem.get_attribute("href") == f"{search_terms[random_num]['page_link']}"):
        
        Dropdown_item = elem

print(Dropdown_item)
Dropdown_item.click()

print(driver.current_url)

vignette_url = "https://allcamping-gears.com/#google_vignette"

if vignette_url in driver.current_url:
    driver.back()

Dropdown_item.click()

print("----------------------------------------------------------------------------------")

first_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['first_related_blog_items']}")

first_related_blog_items.click();

scroll_up_down()

driver.back()

second_related_blog_items = driver.find_element_by_xpath(f"{search_terms[random_num]['second_related_blog_items']}")

second_related_blog_items.click()

scroll_up_down()
driver.back()

print("Python tasks completed successfully")
