from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/") # http://chetanbhogade.pythonanywhere.com/    http://127.0.0.1:8000/

# search_box = driver.find_element_by_xpath('//*[@id="search"]')
# search_box.send_keys('Hitesh Choudhary')

# search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# search_button.click()

time.sleep(2)

# selecting login nav link
login_link = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[4]/a')
login_link.click()

time.sleep(2)

# entering login details 
username_input = driver.find_element_by_xpath('//*[@id="id_username"]')
username_input.send_keys('subhash')

password_input = driver.find_element_by_xpath('//*[@id="id_password"]')
password_input.send_keys('subhash')

login_btn = driver.find_element_by_xpath('/html/body/div/form/div[2]/button')
login_btn.click()

time.sleep(2)

# selecting products nav link
products_link = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/li[3]/a')
products_link.click()

time.sleep(2)

# getting list of all products
products_list = driver.find_elements_by_xpath('//h5[@class="text-uppercase"]/a') 

# clicking on random product
index = random.randint(1, len(products_list)-1)
products_list[index].click()

time.sleep(5)

# clicking on add to cart button
add_to_cart_btn = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/form/button')
add_to_cart_btn.click()

time.sleep(2)


# clicking on checkout button 
checkout_btn = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/a')
checkout_btn.click()

time.sleep(2)


# Filling up the Billing address form 
addr_line1 = driver.find_element_by_xpath('//*[@id="id_address_line1"]')
addr_line1.send_keys('A/304')

addr_line2 = driver.find_element_by_xpath('//*[@id="id_address_line2"]')
addr_line2.send_keys('M.Baria House')

city = driver.find_element_by_xpath('//*[@id="id_city"]')
city.send_keys('Virar')

state = driver.find_element_by_xpath('//*[@id="id_state"]')
state.send_keys('Maharastra')

country = driver.find_element_by_xpath('//*[@id="id_country"]')
country.send_keys('India')

pincode = driver.find_element_by_xpath('//*[@id="id_pincode"]')
pincode.send_keys('401305')

payment_method = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label')
payment_method.click()

time.sleep(2)


# Submiting address form
submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/button')
submit_btn.click()

final_submit_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/table/tbody/tr[6]/td/form/button')
final_submit_btn.click()

time.sleep(2)


# fillimg debit card details
card_holder_name = driver.find_element_by_xpath('//*[@id="card-holder"]')
card_holder_name.send_keys('Chetan Bhogade')

exp_month = driver.find_element_by_xpath('/html/body/section/div/form/div/div/div[2]/div/input[1]')
exp_month.send_keys('08')

exp_year = driver.find_element_by_xpath('/html/body/section/div/form/div/div/div[2]/div/input[2]')
exp_year.send_keys('2025')

card_no = driver.find_element_by_xpath('//*[@id="card-number"]')
card_no.send_keys('4586729435612548')

cvc_no = driver.find_element_by_xpath('//*[@id="cvc"]')
cvc_no.send_keys('655')

proceed_card = driver.find_element_by_xpath('/html/body/section/div/form/div/div/div[5]/button')
proceed_card.click()

time.sleep(2)

# Finally click on account home link
acc_home_link = driver.find_element_by_xpath('/html/body/div/div/div[3]/h6/a')
acc_home_link.click()
time.sleep(2)
