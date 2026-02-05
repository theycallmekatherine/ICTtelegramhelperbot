import requests
from bs4 import BeautifulSoup
import pymysql
import time

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ege",
    charset ="utf8mb4"
)
cursor = conn.cursor()

HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
session = requests.Session()
session.headers.update(HEADERS)
url = "https://inf-ege.sdamgia.ru/test?id=19706454&nt=True&pub=False"
resp = session.get(url, headers=HEADERS, timeout=30)
time.sleep(4)
#print(resp.text)
soup = BeautifulSoup(resp.text, "html.parser")

problems =soup.find_all("div", class_="pbody")
for problem in problems:
    print(problem.text.replace("­",""))
#data = resp.json()
links =soup.find_all("a")
for link in links:
    href = link.get("href")
    if not href or "/problem?id=" not in href:
        continue
    problem_url = "https://inf-ege.sdamgia.ru" + href
    resp_problem = session.get(problem_url, headers=HEADERS, timeout=30)
    time.sleep(4)
    soup_problem = BeautifulSoup(resp_problem.text, "html.parser")

    problem_div = soup_problem.find("div", class_="pbody")
    if not problem_div:
        continue
    problem_text = problem_div.get_text(strip=True)

    answer_div = soup_problem.find("div", class_="answer")
    if not answer_div:
        continue

    answer_text = answer_div.get_text(strip=True)
    answer_value = answer_text.replace("Ответ:", "").strip()

    print("ОТВЕТ:")
    print(answer_value)

    sql = """
    INSERT INTO ege_tasks (problem_url, condition_text, solution_text)
    VALUES (%s, %s, %s)
        """
    cursor.execute(sql, (problem_url, problem_text.replace("­",""), answer_value))
    conn.commit()
cursor.close()
conn.close()