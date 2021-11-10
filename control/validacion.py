def validacion(cadena):
	validacion = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM<>,.-{}´+¿;:_[]*¨¡?=)(/&%$#"!'
	for caracter in str(cadena):
		for caracter_v in validacion:
			if caracter == caracter_v:
				return False
	return True