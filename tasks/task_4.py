"""
	1.	Vytvorte dekorátor cache, ktorý:
	•	Použije vnútorný slovník (dict) na ukladanie výsledkov na základe argumentov funkcie.
	•	Skontroluje, či boli rovnaké argumenty už použité. Ak áno, vráti uložený výsledok.
	•	Ak argumenty ešte neboli použité, zavolá pôvodnú funkciu, uloží výsledok a vráti ho.
	2.	Dekorátor nepoužije functools.wraps.
	3.	Otestujte dekorátor na jednoduchej funkcii add(a, b), ktorá sčíta dve čísla.
	4.	Skontrolujte, ako sa zmenili metadáta funkcie add (napríklad __name__ a __doc__).
	5.	Vytvorte novú funkciu fib(n), ktorá počíta Fibonacciho číslo, a použite na ňu dekorátor cache.
	6.	Skontrolujte, či má každá funkcia svoju vlastnú cache.
"""

# Krok 1: Vytvorte dekorátor cache
# printujme cache hit (argumenty sa nachadzaju v cache)
# printujem cache miss (argumenty sa nenachadzaju v cache)
def cache(fn):
    _cache = {}

    def cacher(*args):
        if args in _cache:
            pass
            print("cache hit!")
        else:
            pass
            print("cache miss :(")

    return cacher


def add(a, b):
    return a + b

# zobrzenie metadat funkcie, skuste pridat @functools.wraps(func)
print(add.__name__)


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib(10))

print(add(1, 2))
print(add(1, 2))
print(add(5, 78))
print(add(5, 78))

# skusit vypisat cache