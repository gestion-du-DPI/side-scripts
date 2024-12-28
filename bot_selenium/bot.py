
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
username = "admin"
password = "123"

# Login part
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_form"))
)

username_input = driver.find_element(By.ID, "selenium_username_login")
password_input = driver.find_element(By.ID, "selenium_password_login")
remeber_me_input = driver.find_element(By.ID, "selenium_remeber_me_box")

username_input.send_keys(username)
password_input.send_keys(password)
remeber_me_input.click()

# waiting just to see the inputs filled
sleep(1)

# Submit the form
login_button = driver.find_element(By.ID, "selenium_login_button")
login_button.click()


# Adding a new patient part
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "selenium_add_patient_button"))
)

# waiting just to see the dashboard
sleep(1)

add_patient_button = driver.find_element(By.ID, "selenium_add_patient_button")
add_patient_button.click()

# Patient info
full_name = "Mostefai Mounir"
gender = "Male"
place_of_birth = "Bordj Bou Arreridj"
address = "Setif, Setif, Algeria"
social_number = "123456789"
phone_number = "0555555555"
email = "mm_mostefai@esi.dz"
emergency_contact_name = "Ahmed Mohsin"
emergency_contact = "0666666666"
number_of_consultation = "0"

# Fill "Full Name"
driver.find_element(By.NAME, "name").send_keys(full_name)

# Select "Gender"
gender_dropdown = Select(driver.find_element(By.NAME, "gender"))
gender_dropdown.select_by_visible_text(gender)

# Fill "Place of Birth"
driver.find_element(By.NAME, "placeOfBirth").send_keys(place_of_birth)

# Fill "Address"
driver.find_element(By.NAME, "address").send_keys(address)

# Fill "Social Number"
driver.find_element(By.NAME, "socialNumber").send_keys(social_number)

# Fill "Phone Number"
driver.find_element(By.NAME, "phone").send_keys(phone_number)

# Fill "Email"
driver.find_element(By.NAME, "email").send_keys(email)

# Fill "Emergency Contact Name"
driver.find_element(By.NAME, "emergencyContact").send_keys(emergency_contact_name)

# Fill "Emergency Contact Phone"
driver.find_element(By.NAME, "emergencyPhone").send_keys(emergency_contact)

# Fill "Number of Consultations"
# consultation = driver.find_element(By.ID, "selenium_consultations_input").clear() 
# consultation.send_keys(number_of_consultation)

# Optionally, click the "Save" button
sleep(4)  # Wait to observe the changes
driver.find_element(By.ID, "selenium_save_patient_button").click()

sleep(2)

# Close the browser
driver.quit()