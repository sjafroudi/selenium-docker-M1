# read imports
try:
    exec(open("./scraper/imports.py").read())
except:
    exec(open("./imports.py").read())

# instantiate Firefox webdriver
def get_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    return driver