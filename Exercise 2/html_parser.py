import json
from bs4 import BeautifulSoup

html_file_path = "D:/Exercise 2/coding-exercise/index.html"

try:
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup)
        capitals = []
        for li in soup.find_all('li'):
            capital = li.find('strong', class_='capital').text.strip()
            state = li.find('span', class_='state').text.strip()
            capitals.append({"capital": capital, "state": state})
        summary = {"numberOfCapitals": len(capitals)}
        output_data = {"capitals": capitals, "summary": summary}
        with open("result.json", "w", encoding="utf-8") as json_file:
            json.dump(output_data, json_file, ensure_ascii=False, indent=2)
except FileNotFoundError:
    print(f"File not found: {html_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
