# Vigenère

# Beskrivning av område
### Innehåll

Vigenèrekryptot är ett förskjutningschiffer som idag används mest till pussel och utbildning då det är relativt enkelt att knäcka och forcera. Det är en vidareutveckling av det enklare Caesar-chiffret som bara har en fast förskjutning. Vigenèrekryptot använder en nyckel som upprepas över texten, där varje bokstav bestämmer förskjutningen av motsvarande bokstav i klartexten. Traditionellt tas speciella tecken bort innan kryptering. Detta besegrar simpel frekvensanalys, då en bokstav på olika platser betyda olika bokstäver.

Krypteringen använder följande metod:

1. Välj en nyckel, t.ex. "MATEMATIK".

2. Varje bokstavs position i alfabetet används för att bestämma förskjutningen. Då "M" är den 13:e bokstaven kommer den första bokstaven i klartexten att förskjutas med 13, "A" med 1, "T" med 20, och så vidare.

3. Bokstaven i klartexten förskjuts enligt nyckelns bokstavs position, och resultatet blir den krypterade texten. Om klartexten är längre än nyckeln, upprepas nyckeln tills hela klartexten är krypterad.

4. Om förskjutningen går utanför alfabetet, så börjar den om från början av alfabetet enl. modulo 29.

**Krypteringsformel**
$$C_i = (P_i + K_i) \pmod{29}$$

Där:
- $C_i$ är den slutgiltiga, krypterade bokstaven.
- $P_i$ är bokstavsvärdet för den $i$:te bokstaven i klartexten, där $\lbrace P_i \in \mathbb{Z} \mid 0 \le P_i \le 28\rbrace$
- $K_i$ är bokstavsvärdet för den $i$:te bokstaven i nyckeln, där $\lbrace K_i \in \mathbb{Z} \mid 0 \le K_i \le 28 \rbrace$

### Exempel
> **Klartext:** "TEXT"  
> **Nyckel:** "KEY"

$$
\begin{aligned}
P &\to \textbf{T}\text{EXT} \implies P_0 = 19 \\
K &\to \textbf{K}\text{EY} \implies K_0 = 10
\end{aligned}
$$

$$
\begin{align*}
C_0 &= (P_0 + K_0) \pmod{29} \\
    &= (19 + 10) \pmod{29} \\
    &= 29 \pmod{29} \\
    &\equiv 0 \implies C \to \textbf{A}
\end{align*}
$$

**Dekrypteringsformel**\
$$P_i = (C_i - K_i) \pmod{29}$$

Kod för att automatisera denna process finns i `encrypt.py` samt `decrypt.py`.

## Användning av AI
AI har under fördjupningens gång använts för att hjälpa till att strukturera och revidera innehållet. Större delen av LaTeX-koden har skrivits för hand, med smärre förslag från AI. AI har även använts för att till stor del skriva koden i Python. AI har inte använts för att skriva någon av de teoretiska delarna, teorin är sammanställd från Wikipedia.
