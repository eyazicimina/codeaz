
SYNONYMS = {
	'bedbah': 'kötü',
	'berbat': 'kötü',
	'iğrenç': 'kötü',
	'problem': 'kötü',
	'hata': 'kötü',
	'sıkıntı': 'kötü',
	'bela': 'kötü',
	'şikayet': 'kötü',
	'memnuniyetsizlik': 'kötü'
}


def kokAra( text: str ) -> str:
	keys = list(SYNONYMS.keys())
	for k in keys:
		if text.startswith(k):
			return SYNONYMS[k]
	return text

def downcastSting( text: str ) -> str:
	words = text.split(" ")
	for i in range( len(words) ):
		words[i] = kokAra( words[i] )

	words = [SYNONYMS[w.lower()] if w.lower() in SYNONYMS else w for w in words ]
	return " ".join(words)

print(downcastSting("verdiginiz xidmet cox berbat"))
print(downcastSting("hep problem karşılaşırım"))
print(downcastSting("hatalardan bezdim"))
