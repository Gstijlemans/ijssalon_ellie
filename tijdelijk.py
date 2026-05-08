prijzen = {  
    "aardbei" : 3, 
    "vanille" : 4, 
    "chocolade" : 5,  
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
print(reclame_tekst)
# wegwerken nullen
reclame_tekst2 = reclame_tekst[:63]
print(reclame_tekst2)