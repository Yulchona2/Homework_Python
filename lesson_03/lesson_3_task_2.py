from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16", "+79150236547"),
    Smartphone("Samsung", "Galaxy S22 Ultra", "+79165289631"),
    Smartphone("Xiaomi", "Redmi 14C", "+79031214589"),
    Smartphone("Realme", "Note 60X", "+79269742365"),
    Smartphone("Huawei", "Mate 50 Pro", "+79254378923")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")
