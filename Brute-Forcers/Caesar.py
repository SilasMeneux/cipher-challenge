def decode(key, cipherText):
	key %= 26
	plaintext = []

	for character in cipherText:
		if character.isupper():
			plaintext.append(chr((ord(character) - ord("A") - key) % 26 + ord("A")))
		elif character.islower():
			plaintext.append(chr((ord(character) - ord("a") - key) % 26 + ord("a")))
		else:
			plaintext.append(character)

	return "".join(plaintext)
