import random

class Karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self.max_hälsa = hälsa
        self.hälsa = hälsa
        self.attackkraft = attackkraft
    
    def attack(self, motståndare):
        skada = self.attackkraft
        motståndare.hälsa -= skada
        print(f"{self.namn} attackerar {motståndare.namn} för {skada} skada!")
        return skada
    
    def är_vid_liv(self):
        return self.hälsa > 0
    
    def __str__(self):
        return f"{self.namn} ({self.hälsa}/{self.max_hälsa} HP)"

class Mage(Karaktär):
    def __init__(self, namn):
        super().__init__(namn, 80, 15)
        self.max_mana = 100
        self.mana = 100
    
    def attack(self, motståndare):
        # Vanlig attack - använder ingen mana
        skada = self.attackkraft
        motståndare.hälsa -= skada
        print(f"{self.namn} kastar en magisk puls på {motståndare.namn} för {skada} skada!")
        return skada
    
    def specialattack(self, motståndare):
        if self.mana >= 30:
            skada = self.attackkraft + 10
            self.mana -= 30
            motståndare.hälsa -= skada
            print(f"{self.namn} kastar ELDBOLL på {motståndare.namn} för {skada} skada! (30 mana)")
            return skada
        else:
            print(f"{self.namn} har inte tillräckligt med mana för eldboll!")
            return 0

class Warrior(Karaktär):
    def __init__(self, namn):
        super().__init__(namn, 120, 12)
        self.styrka = 100
    
    def attack(self, motståndare):
        # Vanlig attack
        skada = self.attackkraft
        motståndare.hälsa -= skada
        print(f"{self.namn} slår {motståndare.namn} med svärdet för {skada} skada!")
        return skada
    
    def specialattack(self, motståndare):
        if self.styrka >= 25:
            skada = self.attackkraft + 15
            self.styrka -= 25
            motståndare.hälsa -= skada
            print(f"{self.namn} utför YXHUGG på {motståndare.namn} för {skada} skada! (25 styrka)")
            return skada
        else:
            print(f"{self.namn} är för trött för yxhugg!")
            return 0

class Ranger(Karaktär):
    def __init__(self, namn):
        super().__init__(namn, 90, 14)
        self.energy = 100
    
    def attack(self, motståndare):
        # Vanlig attack
        skada = self.attackkraft
        motståndare.hälsa -= skada
        print(f"{self.namn} skjuter {motståndare.namn} med pil för {skada} skada!")
        return skada
    
    def specialattack(self, motståndare):
        if self.energy >= 20:
            skada = self.attackkraft + 12
            self.energy -= 20
            motståndare.hälsa -= skada
            print(f"{self.namn} skjuter GIFTPIL på {motståndare.namn} för {skada} skada! (20 energy)")
            return skada
        else:
            print(f"{self.namn} har inte tillräckligt med energy för giftpil!")
            return 0

class Arena:
    def __init__(self, karaktär1, karaktär2):
        self.karaktär1 = karaktär1
        self.karaktär2 = karaktär2
        self.runda = 0
    
    def strid(self):
        print("⚔️ STRIDEN BÖRJAR! ⚔️")
        print(f"{self.karaktär1} vs {self.karaktär2}")
        print("-" * 30)
        
        while self.karaktär1.är_vid_liv() and self.karaktär2.är_vid_liv():
            self.runda += 1
            print(f"\n--- Runda {self.runda} ---")
            
            # Karaktär 1 attackerar
            if self.karaktär1.är_vid_liv():
                self.spelare_tur(self.karaktär1, self.karaktär2)
            
            # Karaktär 2 attackerar
            if self.karaktär2.är_vid_liv():
                self.dator_tur(self.karaktär2, self.karaktär1)
        
        # Visa vinnare
        if self.karaktär1.är_vid_liv():
            print(f"\n🎉 {self.karaktär1.namn} VINNER STRIDEN!")
        else:
            print(f"\n🎉 {self.karaktär2.namn} VINNER STRIDEN!")
    
    def spelare_tur(self, attackerare, motståndare):
        print(f"\n{attackerare.namn}s tur:")
        print(f"HP: {attackerare.hälsa}/{attackerare.max_hälsa}")
        
        # Visa resurser baserat på karaktärstyp
        if isinstance(attackerare, Mage):
            print(f"Mana: {attackerare.mana}/{attackerare.max_mana}")
        elif isinstance(attackerare, Warrior):
            print(f"Styrka: {attackerare.styrka}/{100}")
        elif isinstance(attackerare, Ranger):
            print(f"Energy: {attackerare.energy}/{100}")
        
        val = input("Välj attack: 1. Vanlig attack  2. Specialattack: ")
        
        if val == "1":
            attackerare.attack(motståndare)
        elif val == "2":
            attackerare.specialattack(motståndare)
        else:
            print("Ogiltigt val, använder vanlig attack")
            attackerare.attack(motståndare)
    
    def dator_tur(self, attackerare, motståndare):
        print(f"\n{attackerare.namn}s tur:")
        
        # Enkel AI: 70% chans för vanlig attack, 30% för specialattack
        if random.random() < 0.7:
            attackerare.attack(motståndare)
        else:
            attackerare.specialattack(motståndare)

def huvudprogram():
    print("🌟 KARAKTÄRSBASERAT STRIDSSPEL 🌟")
    print("=" * 40)
    
    # Spelaren väljer karaktär
    print("\nVälj din karaktär:")
    print("1. 🔮 Mage (Magic, använder mana)")
    print("2. ⚔️ Warrior (Stark, använder styrka)") 
    print("3. 🏹 Ranger (Smidig, använder energy)")
    
    val = input("Välj karaktär (1-3): ")
    namn = input("Ange din karaktärs namn: ")
    
    if val == "1":
        spelare = Mage(namn)
    elif val == "2":
        spelare = Warrior(namn)
    elif val == "3":
        spelare = Ranger(namn)
    else:
        print("Ogiltigt val, blir Warrior")
        spelare = Warrior(namn)
    

    dator_namn = random.choice(["Drake", "Troll", "Orc", "Varg"])
    dator_typ = random.choice([Mage, Warrior, Ranger])
    dator = dator_typ(dator_namn)
    
    print(f"\nDin motståndare: {dator}")
    

    arena = Arena(spelare, dator)
    arena.strid()

# Kör spelet
if __name__ == "__main__":
    huvudprogram()
