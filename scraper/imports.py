import os, sys, time, math, random, re, google, nest_asyncio
nest_asyncio.apply()
from firefox_clear_cache import clear_cache
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException, InvalidSessionIdException, TimeoutException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from urllib3.exceptions import HTTPError