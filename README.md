# Vigenère

# Beskrivning av område
### Innehåll

Vigenèrekryptot är ett förskjutningschiffer som idag används mest till pussel och utbildning då det är relativt enkelt att knäcka och forcera. Det är en vidareutveckling av det enklare Caesar-chiffret som bara har en fast förskjutning. Vigenèrekryptot använder en nyckel som upprepas över texten, där varje bokstav bestämmer förskjutningen av motsvarande bokstav i klartexten. Traditionellt tas speciella tecken bort innan kryptering. Detta besegrar simpel frekvensanalys, då en bokstav på olika platser betyda olika bokstäver.

Krypteringen använder följande metod:

1. Välj en nyckel, t.ex. "MATEMATIK".

2. Varje bokstavs position i alfabetet används för att bestämma förskjutningen. Då "M" är den 13:e bokstaven kommer den första bokstaven i klartexten att förskjutas med 13, "A" med 1, "T" med 20, och så vidare.

3. Bokstaven i klartexten förskjuts enligt nyckelns bokstavs position, och resultatet blir den krypterade texten. Om klartexten är längre än nyckeln, upprepas nyckeln tills hela klartexten är krypterad.

4. Om förskjutningen går utanför alfabetet, så börjar den om från början av alfabetet enl. modulo 26.

# Formel för kryptering
För att kryptera en bokstav i klartexten, används följande formel:
$(C_i = (P_i + K_i) \mod 26)$