from selenium.webdriver.common.by import By
import time

def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30) #можете изменить, т.к в задании написано 30, но хватает даже 5ти:)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    #Я прекрасно понимаю, что сообщение после assert в целом бесполезное, т.к если элемента не будет,
    #то будет ошибка NoSuchElement, но в ходе задания это необходимо
    #В целом, я понимаю, как можно сделать хорошую и валидную проверку, но там необходима конструкция с expect condition
    #а судя по коммментариям, учителя на курсе это не жалуют, но в реальных проектах, я именно такую проверу и буду использовать
    assert button, "No button"

    


