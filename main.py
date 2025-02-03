import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.ui import Select
from termcolor import colored  

# Fungsi untuk membuat akun
def create_account(email, username, account_number, result_file):

    options = uc.ChromeOptions()
    options.headless=False
    options.add_argument('--disable-gpu') 
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-extensions') 
    options.add_argument('--incognito')
    driver = uc.Chrome(options=options)
    try:
        driver.get("https://www.spotify.com/id-id/signup")

        driver.find_element(By.ID, 'username').send_keys(email)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']").click()

        # Tunggu hingga elemen error muncul atau sampai password field muncul
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'This address is already linked to an existing account')]"))
            )
            print(colored(f"Email sudah terdaftar: {email}. Melanjutkan ke email berikutnya.", 'yellow'))
            return  # Keluar dari fungsi jika email sudah terdaftar
        except:
            # Jika tidak ada error, lanjutkan ke proses pembuatan akun
            driver.find_element(By.ID, 'new-password').send_keys("yalldammit000")
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "button[data-encore-id='buttonPrimary']").click()

            driver.find_element(By.ID, 'displayName').send_keys(username)
            driver.find_element(By.ID, 'day').send_keys("4")

            # Pilih bulan secara acak
            select_element = driver.find_element(By.ID, "month")
            select = Select(select_element)
            options = select.options
            random_index = random.randint(1, len(options) - 1)  # Abaikan opsi pertama jika placeholder
            select.select_by_index(random_index)

            driver.find_element(By.ID, 'year').send_keys("1999")
            driver.find_element(By.XPATH, "//label[span[text()='Prefer not to say']]").click()
            driver.find_element(By.CSS_SELECTOR, "button[data-encore-id='buttonPrimary']").click()
            driver.find_element(By.XPATH, "//span[text()='I would prefer not to receive marketing messages from Spotify']").click()
            driver.find_element(By.CSS_SELECTOR, "button[data-encore-id='buttonPrimary']").click()
            
            time.sleep(7)

            current_url = driver.current_url
            if current_url == "https://www.spotify.com/id-id/download/windows/":
                success_message = f"{account_number}. Berhasil Membuat Akun Spotify : {email} "
                print(colored(success_message, 'green'))
             
            # Simpan akun yang berhasil dibuat ke dalam file result.txt
            result_file.write(f"{email}\n")

    except Exception as e:
        print(f"Error occurred while creating account for {email}: {str(e)}")
    finally:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error during driver quit: {str(e)}")

# Fungsi untuk membaca akun dari file dan membuat akun
def create_accounts_from_file():
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    account_number = 1  # Inisialisasi nomor akun

    # Membuka file result.txt untuk menulis semua akun yang berhasil
    with open("result.txt", 'a') as result_file:
        for account in accounts:
            account = account.strip()  # Hapus whitespace atau newline
            
            if account:  # Proses hanya baris yang tidak kosong
                try:
                    email, username = account.split('|')
                    create_account(email, username, account_number, result_file)
                    account_number += 1  # Increment nomor akun untuk setiap akun baru

                except ValueError:
                    print(f"Skipping invalid line (could not split correctly): {account}")

    input("Proses Selesai, tekan enter untuk keluar...")

if __name__ == "__main__":
    create_accounts_from_file()