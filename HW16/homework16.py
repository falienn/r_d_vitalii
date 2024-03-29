import threading
import requests
import time

# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
# Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
#
# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
#
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.

kyiv_ = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&hourly=temperature_2m"
uzhhorod_ = "https://api.open-meteo.com/v1/forecast?latitude=48.62&longitude=22.29&hourly=temperature_2m"
venezia_ = "https://api.open-meteo.com/v1/forecast?latitude=44.42&longitude=11.17&hourly=temperature_2m"
rome_ = "https://api.open-meteo.com/v1/forecast?latitude=41.89&longitude=12.51&hourly=temperature_2m"
sharm_el_sheikh_ = "https://api.open-meteo.com/v1/forecast?latitude=27.92&longitude=34.33&hourly=temperature_2m"

city_list = [kyiv_, uzhhorod_, venezia_, rome_, sharm_el_sheikh_]


def multi_thread():
    result = []

    def request(tread_number, city):
        print(f"Start to {tread_number}")
        resp = requests.get(city)
        result.append(resp)
        print(f"End to {tread_number}")
        temperatures = resp.json()["hourly"]["temperature_2m"]
        print(temperatures)

    start = time.time()
    threads = []

    for i, city in enumerate(city_list):
        threads.append(threading.Thread(target=request, args=(i, city)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for elem in result:
        print(elem)

    end = time.time()
    print(f"Time is {end - start}")


if __name__ == "__main__":
    multi_thread()
