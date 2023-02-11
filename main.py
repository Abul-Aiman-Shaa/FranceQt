import time
import pywhatkit
import datetime as dt
import customtkinter

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    # Login
    time.sleep(20)
    name_input = browser.find_element(by=By.ID, value="mat-input-0")
    name_input.send_keys(Keys.ENTER)
    time.sleep(1)
    name_input.send_keys("xxxxxxxxxxx@gmail.com")

    password_input = browser.find_element(by=By.ID, value="mat-input-1")
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)
    password_input.send_keys("#############")

    cookie = browser.find_element(by=By.ID, value="onetrust-accept-btn-handler")
    cookie.click() # (419, 500)

    signup_btn = browser.find_element(by=By.CLASS_NAME, value="mat-button-wrapper")
    signup_btn.click()

    # Booking
    time.sleep(10)
    booking = browser.find_element(by=By.CLASS_NAME, value="mat-button-wrapper")
    booking.click()

    time.sleep(10)


def bangalore():
    time.sleep(10)
    select_element1 = browser.find_element(by=By.ID, value="mat-select-0")
    select_element1.send_keys(Keys.ENTER)
    option_element1 = browser.find_element(by=By.ID, value="mat-option-3")
    option_element1.send_keys(Keys.ENTER)
    time.sleep(10)
    select_element2 = browser.find_element(by=By.ID, value="mat-select-value-5")
    select_element2.click()
    option_element2 = browser.find_element(by=By.ID, value="mat-option-58")
    option_element2.send_keys(Keys.ENTER)
    time.sleep(5)


def chennai():
    select_element1 = browser.find_element(by=By.ID, value="mat-select-0")
    select_element1.send_keys(Keys.ENTER)
    option_element1 = browser.find_element(by=By.ID, value="mat-option-5")
    option_element1.send_keys(Keys.ENTER)
    time.sleep(10)
    select_element2 = browser.find_element(by=By.ID, value="mat-select-value-5")
    select_element2.click()
    option_element2 = browser.find_element(by=By.ID, value="mat-option-84")
    option_element2.send_keys(Keys.ENTER)
    time.sleep(5)


def cochin():
    time.sleep(10)
    select_element1 = browser.find_element(by=By.ID, value="mat-select-0")
    select_element1.send_keys(Keys.ENTER)
    option_element1 = browser.find_element(by=By.ID, value="mat-option-6")
    option_element1.send_keys(Keys.ENTER)
    time.sleep(10)
    select_element2 = browser.find_element(by=By.ID, value="mat-select-value-5")
    select_element2.click()
    option_element2 = browser.find_element(by=By.ID, value="mat-option-123")
    option_element2.send_keys(Keys.ENTER)
    time.sleep(5)


def hyderabad():
    time.sleep(10)
    select_element1 = browser.find_element(by=By.ID, value="mat-select-0")
    select_element1.send_keys(Keys.ENTER)
    option_element1 = browser.find_element(by=By.ID, value="mat-option-7")
    option_element1.send_keys(Keys.ENTER)
    time.sleep(10)
    select_element2 = browser.find_element(by=By.ID, value="mat-select-value-5")
    select_element2.click()
    option_element2 = browser.find_element(by=By.ID, value="mat-option-150")
    option_element2.send_keys(Keys.ENTER)
    time.sleep(5)


def puducherry():
    select_element1 = browser.find_element(by=By.ID, value="mat-select-0")
    select_element1.send_keys(Keys.ENTER)
    option_element1 = browser.find_element(by=By.ID, value="mat-option-14")
    option_element1.send_keys(Keys.ENTER)
    time.sleep(10)
    select_element2 = browser.find_element(by=By.ID, value="mat-select-value-5")
    select_element2.click()
    option_element2 = browser.find_element(by=By.ID, value="mat-option-169")
    option_element2.send_keys(Keys.ENTER)
    time.sleep(5)


def qt5_exit_win32api():
    browser.quit()


def qt5_tk_win32api():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")

    def button_function():
        qt5_exit_win32api()
        app.quit()

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()


# Start Info
try:
    pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                             f'FranceQt --Started --Time " {dt.datetime.now()} "')
    time.sleep(20)

except:
    pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                             f'FranceQt --Started --Time " {dt.datetime.now()} "')
    time.sleep(20)
while True:
    # Getting Browser Ready
    # Initializing The Browser
    browser = webdriver.Edge(
        r'C:\Users\user\edgedriver\edgedriver_win32\msedgedriver.exe')

    # Minimizing The Browser
    # browser.minimize_window()

    # Getting Vfs Web
    browser.get('https://visa.vfsglobal.com/ind/en/fra/application-detail/')
    try:
        # Getting The Main Function
        main()
        edit = True

        # Having Gui Exit Button
        # qt5_tk_win32api()
    
        if edit:
            # Getting The B Function
            try:
                bangalore()
                button_b = browser.find_element(by=By.CSS_SELECTOR,
                                                value=".mat-raised-button.mat-button-disabled:not(["
                                                      "class*=mat-elevation-z])").get_attribute(
                    "disabled")
                if button_b:
                    print("Not found B")
                # ______
            except NoSuchElementException:
                text_1 = browser.find_element(by=By.CSS_SELECTOR, value=".alert-info").text
                pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                                         text_1)
                print("Email sent")
    
            except:
                browser.close()
                continue
    
            # Getting The C Function
            try:
                chennai()
                button_c = browser.find_element(by=By.CSS_SELECTOR, value=".mat-raised-button.mat-button-disabled:not(["
                                                                          "class*=mat-elevation-z])").get_attribute(
                    "disabled")
    
                if button_c:
                    print("Not found C")
                # ______
            except NoSuchElementException:
                text_2 = browser.find_element(by=By.CSS_SELECTOR, value=".alert-info").text
                pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                                         text_2)           
                print("Email sent")
    
            except:
                browser.close()
                continue
    
            # Getting The CC Function
            try:
                cochin()
                button_cc = browser.find_element(by=By.CSS_SELECTOR, value=".mat-raised-button.mat-button-disabled:not(["
                                                                           "class*=mat-elevation-z])").get_attribute(
                    "disabled")
    
                if button_cc:
                    print("Not found CC")
                # ______
            except NoSuchElementException:
                text_3 = browser.find_element(by=By.CSS_SELECTOR, value=".alert-info").text
                pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                                         text_3)           
                print("Email sent")
    
            except:
                browser.close()
                continue
    
            # Getting The H Function
            try:
                hyderabad()
                button_h = browser.find_element(by=By.CSS_SELECTOR, value=".mat-raised-button.mat-button-disabled:not(["
                                                                          "class*=mat-elevation-z])").get_attribute(
                    "disabled")
    
                if button_h:
                    print("Not found H")
                # ______
            except NoSuchElementException:
                text_4 = browser.find_element(by=By.CSS_SELECTOR, value=".alert-info").text
                pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                                         text_4)
                print("Email sent")
    
            except:
                browser.close()
                continue
    
            # Getting The P Function
            try:
                puducherry()
                button_p = browser.find_element(by=By.CSS_SELECTOR, value=".mat-raised-button.mat-button-disabled:not(["
                                                                          "class*=mat-elevation-z])").get_attribute(
                    "disabled")
    
                if button_p:
                    print("Not found P")
                # ______
            except NoSuchElementException:
                text_5 = browser.find_element(by=By.CSS_SELECTOR, value=".alert-info").text
                pywhatkit.sendwhatmsg_to_group_instantly("H2b7vp6tzZ87cGX8vZH2Lm",
                                                         text_5)
                print("Email sent")
    
            except:
                browser.close()
                continue
    
            print("--------------------")
    except:
        browser.close()
        continue
