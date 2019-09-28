import os
from appium import webdriver
from time import sleep
from random import randint
print('Started')

################################################################################
################################################################################
############################# EDIT HERE ########################################
################################################################################
################################################################################
password = 'Testing@123'

shoe_size = '9' # Here the sizes are exact and you cant select any size that is bigger than 10
zip_code = '60066'

################################################################################
################################################################################
################################################################################
################################################################################

length_of_random_num = 10
dir_path = os.path.dirname(os.path.realpath(__file__))
formated_data_path = '{}/{}'.format(dir_path, 'data.txt')

data_to_enter = open(formated_data_path, 'r').read()
lines = data_to_enter.split('\n')
emails = []
First_name = []
Last_name = []

for line in lines:
    if len(line) > 1:
        emails_read, first_name, last_name = line.split(',')
        emails.append(str(emails_read))
        First_name.append(str(first_name))
        Last_name.append(str(last_name))

dir_path = os.path.dirname(os.path.realpath(__file__))
formated_app_path = '{}/{}'.format(dir_path, 'com.hibbett.android.apk')

desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.hibbett.android",
  "appWaitActivity": "com.hibbett.android.auth.AuthActivity_",
  "app": formated_app_path
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)


def start():
    sleep(1)
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
    except Exception as e:
        print("ERROR OCCURED", e)


def signup(email, firstname, lastname, phonenum):
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_accessibility_id("Account Tab").click()
    except Exception as e:
        print("ERROR OCCURED", e)

    driver.implicitly_wait(5)
    try:
        driver.find_element_by_id("com.hibbett.android:id/signin_button").click()
    except Exception as e:
        print("ERROR OCCURED", e)

    driver.implicitly_wait(5)

    first_name_entry = driver.find_element_by_accessibility_id("First Name")
    last_name_entry = driver.find_element_by_accessibility_id("Last Name")
    phone_num_entry = driver.find_element_by_id("com.hibbett.android:id/phone")
    email_entry = driver.find_element_by_accessibility_id("Email Address")
    password_entry = driver.find_element_by_accessibility_id("Password")

    first_name_entry.set_value(firstname)
    last_name_entry.set_value(lastname)
    phone_num_entry.set_value(phonenum)
    email_entry.set_value(email)
    password_entry.set_value(password)

    # click signup buttons
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.Button').click()


def enter_raffle():
    # NAVIGATE TO RAFFLE sms_entry
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_accessibility_id('Raffle and Launch Tab').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # tap list view changer
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("Grid View")').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # Scroll down to select shoe_size
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('''new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Jordan 1 Retro High OG "Obsidian/University Blue" Men's Shoe").instance(0))''').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # To click enter raffle
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('com.hibbett.android:id/raffle_cta_text').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # To select shoe size
    driver.implicitly_wait(10)
    try:
        formated_ui_str = 'new UiSelector().text("{}")'.format(shoe_size)
        print(formated_ui_str)
        driver.find_element_by_android_uiautomator(formated_ui_str).click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # To select stores
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("Select Stores")').click()
    except Exception as e:
        print("ERROR OCCURED", e)


    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("Search for City & State or Zip")').click()
        driver.implicitly_wait(5)
        enter_zipcode = driver.find_element_by_id('com.google.android.gms:id/edit_text')
        sleep(1)
        enter_zipcode.set_value(zip_code)
    except Exception as e:
        print("ERROR OCCURED", e)

    sleep(2)
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()
    except Exception as e:
        print("ERROR OCCURED", e)


    driver.implicitly_wait(10)
    try:
        # driver.find_element_by_android_uiautomator('new UiSelector().text("Select")').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # click save button
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("SAVE SELECTED")').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # delete number
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/TextInputLayout/android.widget.FrameLayout/android.widget.EditText').set_value('')
    except Exception as e:
        print("ERROR OCCURED", e)

    # Confirm entry
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("CONFIRM ENTRY")').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # I UNDERSTAND popup close
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("I UNDERSTAND")').click()
        sleep(1)
        driver.back()
    except Exception as e:
        print("ERROR OCCURED", e)


def sign_out():
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_accessibility_id('Account Tab').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # tap account settings
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("Account Settings")').click()
    except Exception as e:
        print("ERROR OCCURED", e)

    # tap logout
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_android_uiautomator('new UiSelector().text("Log Out")').click()
    except Exception as e:
        print("ERROR OCCURED", e)


if __name__ == '__main__':
    for (emails_get, first_name_get, last_name_get) in zip(emails, First_name, Last_name):
        random_phone_num = ''.join(["%s" % randint(2, 9) for num in range(0, length_of_random_num)])
        start()
        signup(emails_get, first_name_get, last_name_get, random_phone_num)
        enter_raffle()
        sign_out()
        print('PASS')
