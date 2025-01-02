from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a URL
driver.get("http://localhost:4200/")

# Login credentials 
username = "poco@gmail.com"
password = "projectigl"

# Login part
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_form"))
)

username_input = driver.find_element(By.ID, "selenium_username_login")
password_input = driver.find_element(By.ID, "selenium_password_login")
remember_me_input = driver.find_element(By.ID, "selenium_remeber_me_box")

username_input.send_keys(username)
password_input.send_keys(password)
remember_me_input.click()

# Wait to observe the inputs
sleep(1)

# Submit the form
login_button = driver.find_element(By.ID, "selenium_login_button")
login_button.click()

# Adding a new patient part
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "selenium_add_patient_button"))
)

# Wait to observe the dashboard
sleep(1)

add_patient_button = driver.find_element(By.ID, "selenium_add_patient_button")
add_patient_button.click()

# Wait for the patient form to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "first_name"))
)

# Patient info
first_name = "Mostefai"
last_name = "Mounir"
gender = "Male"
date_of_birth = "1990-01-01"
place_of_birth = "Bordj Bou Arreridj"
address = "Setif, Setif, Algeria"
social_number = "123456789"
phone_number = "+213555555555"
email = "mm_mostefai@esi.dz"
emergency_contact_name = "Ahmed Mohsin"
emergency_contact_phone = "+213666666666"
medical_condition = "None"

# Fill "First Name"
driver.find_element(By.NAME, "first_name").send_keys(first_name)

# Fill "Last Name"
driver.find_element(By.NAME, "last_name").send_keys(last_name)

# Select "Gender"
gender_dropdown = Select(driver.find_element(By.NAME, "gender"))
gender_dropdown.select_by_visible_text(gender)

# Fill "Date of Birth"
driver.find_element(By.NAME, "date_of_birth").send_keys(date_of_birth)

# Fill "Place of Birth"
driver.find_element(By.NAME, "place_of_birth").send_keys(place_of_birth)

# Fill "Address"
driver.find_element(By.NAME, "address").send_keys(address)

# Fill "Social Number"
driver.find_element(By.NAME, "nss").send_keys(social_number)

# Fill "Phone Number"
driver.find_element(By.NAME, "phone_number").send_keys(phone_number)

# Fill "Email"
driver.find_element(By.NAME, "email").send_keys(email)

# Fill "Emergency Contact Name"
driver.find_element(By.NAME, "emergency_contact_name").send_keys(emergency_contact_name)

# Fill "Emergency Contact Phone"
driver.find_element(By.NAME, "emergency_contact_phone").send_keys(emergency_contact_phone)

# Fill "Medical Condition"
driver.find_element(By.NAME, "medical_condition").send_keys(medical_condition)

# Optionally, click the "Save" button
sleep(4)  # Wait to observe the changes
driver.find_element(By.ID, "selenium_save_patient_button").click()

# Wait to observe the submission
sleep(2)

# Close the browser
driver.quit()
