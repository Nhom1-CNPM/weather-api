import requests
from datetime import datetime

API_KEY = "38f26c4dd62728b1c2a02e6a5e488409"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "vi"
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        forecast_data = data["list"]
        city_name = data["city"]["name"]
        
        forecast_dict = {}
        
        for entry in forecast_data:
            date = datetime.utcfromtimestamp(entry["dt"]).strftime("%Y-%m-%d")
            time = datetime.utcfromtimestamp(entry["dt"]).strftime("%H:%M")
            temp = entry["main"]["temp"]
            desc = entry["weather"][0]["description"]
            
            if date not in forecast_dict:
                forecast_dict[date] = []
            forecast_dict[date].append(f"{time}: {desc.capitalize()}, {temp}°C")
        
        forecast_report = f"Dự báo thời tiết tại {city_name}:\n"
        for date, reports in forecast_dict.items():
            forecast_report += f"\n📅 {date}:\n" + "\n".join(reports) + "\n"
        
        return forecast_report
    else:
        return "Không tìm thấy thông tin dự báo thời tiết. Vui lòng thử lại!"

if __name__ == "__main__":
    city = input("Nhập tên thành phố: ")
    print(get_forecast(city))
    input("Nhấn bất kì phím gì để dừng chương trình")
    
    