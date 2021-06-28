"""
Otrzymujesz ciąg zawierający szczegółową listę plików. Twoim zadaniem jest ocena prostego zapytania dotyczącego pliku
pewien podzbiór tych plików.

Ciąg składa się z N wierszy oddzielonych znakami końca wiersza (kod ASCII 10). Każda linia
zawiera informacje o jednym pliku, pogrupowane w pięciu kolumnach: właściciel, uprawnienie, data, rozmiar i nazwa w
to zamówienie). Kolumny (z wyjątkiem ostatniej) mają stałą długość i są oddzielone jednym
przestrzeń. Mają następujące formaty i znaczenia:

• Uprawnienia do kolumny mają długość 3 i zawierają informacje o uprawnieniach. Zawiera
trzy znaki: sterują odpowiednio, czy czytają, piszą i wykonują
plik jest dozwolony. Znaki to odpowiednio r, różdżka x, jeśli te operacje
są dozwolone; w przeciwnym razie są -.
• Właściciel kolumny ma długość 6 i zawiera ciąg reprezentujący nazwę użytkownika
kto utworzył plik. W nazwie rozróżniana jest wielkość liter i wyrównana do lewej.
• Rozmiar kolumny ma długość 10 i zawiera rozmiar pliku w bajtach. Rozmiar jest mniejszy
niż 231 bajtów i jest wyrównany do prawej strony.
• Data kolumny ma długość 11 i zawiera datę ostatniej modyfikacji pliku w formacie
format „dd MMM rrrr”. Nazwy miesięcy to styczeń, luty, marzec, kwiecień, maj, czerwiec,
Lipiec, sierpień, wrzesień, październik, listopad i grudzień
• Nazwa kolumny ma zmienną długość i zawiera nazwę pliku. Nazwa
plik zawiera maksymalnie 255 drukowalnych znaków ASCII i zawiera co najmniej jeden
znak kropki.

Interesują nas tylko pliki spełniające następujące kryteria:
• Są wykonywalne. Mówimy, że plik jest wykonywalny, jeśli wykonanie pliku to
dozwolony.
• Zostały utworzone przez użytkownika o imieniu admin.
• Ich rozmiar jest mniejszy niż 14 * 2 ^ 20 bajtów.

Oblicz najwcześniejszą datę ostatniej modyfikacji tych plików.

Napisz funkcję:
rozwiązanie (a) def
że mając napis S opisujący listę plików, zwraca odpowiedź na zapytanie, zakodowaną jako łańcuch.
Datę należy zwrócić w formacie „dd MMM rrrr”.

Jeśli nie ma plików spełniających powyższe kryteria, funkcja powinna zwrócić „BRAK PLIKÓW”.

Na przykład dla danego ciągu S z N = 8 wierszami (zawartymi między „” ”):

funkcja powinna zwrócić „29 września 1983”.

Zakładać, że:
• N jest liczbą całkowitą z zakresu [1..100);
• ciąg S składa się tylko z drukowalnych znaków ASCII i znaków końca linii;
• ciąg S jest poprawną listą plików zgodnie z powyższą specyfikacją. Pliki mogą mieć te same nazwy.
W swoim rozwiązaniu skup się na poprawności. Ocena rozwiązania nie będzie przedmiotem oceny

"""