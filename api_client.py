import requests

url = "https://your-app.onrender.com/student"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Student ID:", data["student_id"])
    print("Name:", data["name"])
    print("Program:", data["program"])
    print("Year:", data["year"])
    print("Section:", data["section"])
else:
    print("Request failed.")