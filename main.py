from selenium import webdriver
from selenium.webdriver.common.by import *

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

def main():
    driver.get("https://duckduckgo.com/?q=inurl%3A%22index.php%3Fid%3D%22&ia=web")
    elems = driver.find_elements(By.XPATH, "//a[@href]")

    try:
        with open("result.txt", "r") as f:
            existing_links = [line.strip() for line in f]
    except FileNotFoundError:
        existing_links = []
    with open("result.txt", "a") as f:
        for elem in elems:
            link = elem.get_attribute("href")
            if "index.php" in link and not link.startswith("https://duckduckgo.com"):
                if link not in existing_links:
                    f.write(link + "\n")
                    existing_links.append(link)
    driver.quit()

if __name__ == '__main__':
    main()
