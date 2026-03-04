#Oddiy class
class Mashina:
    def __init__(self, model, rang, tezlik, yil):
        self.model = model
        self.rang = rang
        self.tezlik = tezlik
        self.yil = yil


gentra = Mashina("Gentra 1.6", "Oq", 200, 2025)

damas = Mashina("Damas 2", "Oq", 140, 2024)

bmw = Mashina("BMW M5", "Qora", 300, 2026)



print("="*30)
print(f"Model: {bmw.model}")
print(f"Rangi: {bmw.rang} rang!")
print(f"Tezligi: {bmw.tezlik} km/s")
print(f"Chiqarilgan yili: {bmw.yil}-yil!")
print("="*30)





#Zamonaviy Dataclass
from dataclasses import dataclass

@dataclass
class Mashina:
    model: str
    rang: str
    tezlik: int
    yil: int


bmw = Mashina("BMW M5", "Qora", 300, 2026)

print("="*30)
print(f"Model: {bmw.model}")
print(f"Rangi: {bmw.rang} rang!")
print(f"Tezligi: {bmw.tezlik} km/s")
print(f"Chiqarilgan yili: {bmw.yil}-yil!")
print("="*30)