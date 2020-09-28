# make sure that the chrome driver and your chrome browser is of the same version
from tkinter import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

win = Tk()
win.resizable(width = False, height = False)
win.title("Insta_messaging_bot")
win.iconbitmap("myicon.ico")

User_label = Label(win, text = "Username:")
User_label.grid(row = 0, column = 0, padx = 5, pady = 5)

Pass_label = Label(win, text = "Password:")
Pass_label.grid(row = 1, column = 0, padx = 5, pady = 5)

User_entry = Entry(win, width = 80)
User_entry.grid(row = 0, column = 1, padx = (0,5))

Pass_entry = Entry(win, width = 80)
Pass_entry.grid(row = 1, column = 1, padx = (0,5))

target_label = Label(win, text = "TargetIDs:")
target_label.grid(row = 2, column = 0, padx = 5, pady = 5)

target_entry = Entry(win , width = 80)
target_entry.grid(row = 2, column = 1, padx = (0,5))

msg_label = Label(win, text = "Msg:")
msg_label.grid(row = 3, column = 0, padx = 5, pady = 5)

msg_entry = Entry(win , width = 80)
msg_entry.grid(row = 3, column = 1, padx = (0,5))

def clicked():

    driver = webdriver.Chrome("chromedriver.exe")

    driver.maximize_window()

    driver.get("https://www.instagram.com")

    try:
        clickuser = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        clickuser.send_keys(User_entry.get())

        clickpass = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        clickpass.send_keys(Pass_entry.get())
        clickpass.send_keys(Keys.RETURN)

        notnow1 = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cmbtv"))
        )
        notnow1.click()
        
        notnow2 = WebDriverWait(driver, 1000).until(
            lambda x: x.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        )
        notnow2.click()

        # I'm storing the target names in a list so that I can use them as I want..

        lists = target_entry.get().split(",")

        # I used the count variable to control the while loop..

        count = 0
 
        # I am using while loop to control the number of times, it repeats the steps...
        # And I am using the for loop for controling the target names

        while count < len(lists):
            for names in lists:

                searchid = WebDriverWait(driver, 1000).until(
                    lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
                )
                searchid.send_keys(names)

                clickid = WebDriverWait(driver, 1000).until(
                    lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
                )
                clickid.click()

                clickmsg = WebDriverWait(driver, 1000).until(
                    lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
                )
                clickmsg.click()

                msg = WebDriverWait(driver, 1000).until(
                    lambda x: x.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                )
                msg.send_keys(msg_entry.get())
                msg.send_keys(Keys.RETURN)

                driver.back()   # I'm using driver.back() to go backwards....
                driver.back()

                count += 1 # incrementing the value of count..

    finally:
        driver.quit()

    msg_entry.delete(0, END)
    User_entry.delete(0, END)
    Pass_entry.delete(0, END)
    target_entry.delete(0, END)

b1 = Button(win , text = "Activate", command = clicked)
b1.grid(row = 4, column = 0 , columnspan = 2, pady = 5)

win.mainloop()