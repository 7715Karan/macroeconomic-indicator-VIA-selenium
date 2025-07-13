from flask import Flask, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8000"}})


def scrape_rbi_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    url = "https://rbi.org.in/"
    driver.get(url)

    data = {
        "policy_rates": [],
        "reserve_ratios": [],
        "exchange_rates": [],
        "deposit_rates": [],
        "market_trends": []
    }

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button2"))).click()


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/h3[1]/a'))).click()
        for i in range(1, 6):
            row = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="wrapper"]/div[1]/table/tbody/tr[{i}]'))
            )
            data["policy_rates"].append(row.text)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/h3[2]/a'))).click()
        for i in range(1, 3):
            row = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="wrapper"]/div[2]/table/tbody/tr[{i}]'))
            )
            data["reserve_ratios"].append(row.text)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/h3[3]/a'))).click()
        for i in range(1, 6):
            row = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="wrapper"]/div[3]/table/tbody/tr[{i}]'))
            )
            data["exchange_rates"].append(row.text)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/h3[4]/a'))).click()
        for i in range(1, 5):
            row = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="wrapper"]/div[4]/table/tbody/tr[{i}]'))
            )
            data["deposit_rates"].append(row.text)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/h3[5]/a'))).click()
        for i in range(1, 9):
            row = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="wrapper"]/div[5]/table[2]/tbody/tr[{i}]'))
            )
            data["market_trends"].append(row.text)

    except Exception as e:
        driver.quit()
        return {"error": str(e)}

    driver.quit()
    return data


@app.route('/rbi-data', methods=['GET'])
def get_rbi_data():
    rbi_data = scrape_rbi_data()
    return jsonify(rbi_data)


if __name__ == '__main__':
    app.run(port=5050, debug=True)

