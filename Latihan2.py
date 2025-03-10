"""
input:
Aku suka rajawali, bapak. Apabila wajar, aku suka
Kasur ini rusak.
Kasur Nababan rusak.
Kasur Koh Ahok rusak.
Ibu Ratna antar ubi.
Ria Irawan nawari air
Harum semar kayak rames murah.
Ira hamil lima hari.
"""

def polindrom(text):
    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False
    
    return polindrom(text[1:-1])

kalimat = input()
kalimatFix = ("".join(i for i in kalimat if i.isalpha())).lower()
print(polindrom(kalimatFix))
