import re

riesgotipo4 = "Riesgo en MPS, INS, MAVDT, Contraloría General, Procuraduría General"
riesgotipo3 = "Riesgo en el SPD"
riesgotipo2 = "Riesgo en la Alcaldía, Gobernación"
riesgotipo1 = "Persona prestadora, COVE"
prefijodeRiesgo = "El caso debe ser notificado a:"
riesgotipo0 = "Sin riesgo alguno, continuar el control y la vigilancia."

def waterQuality(state):
	
	if re.search("[|¬°\"\'!#$%&/\(\)=?¿¡+¨´*~\{\}\[\]\^\`\-,;:_\<\>]", state):
		print("\n Favor agregar un nivel de riesgo valido o numero positivo IRCA(%) valido, debe ser sin simbolos.\n Datos validos son:\n => SIN RIESGO, BAJO, MEDIO, ALTO o INVIABLE,\n=> O numero entre 0 al 100.")
		waterQuality(input('Ingrese por favor usted el tipo de riesgo, o digite un numero entre el 0 al 100, gracias:'))
		return
	elif not re.search("[a-zA-Z]|\s|\.", state):
		state = int(state)
	elif re.search("\.", state) and (not re.search("[a-zA-Z]|\s", state)):
		state = float(state)
	else:
		state = (state.strip()).upper()
	if isinstance(state, str):
		if state == "INVIABLE":
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,',',riesgotipo3,',',riesgotipo4,end=".")
		elif state == "ALTO":
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,',',riesgotipo3,end=".")
		elif state == "MEDIO":
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,',',end=".")
		elif state == "BAJO":
			print(prefijodeRiesgo,riesgotipo1,end=".")
		elif state == "SIN RIESGO":
			print(riesgotipo0)
		else:
			print("\nSiendo texto, favor colocar uno de los riesgos valido:\n=> SIN RIESGO, BAJO, MEDIO, ALTO o INVIABLE.")
			waterQuality(input('Ingrese por favor usted el tipo de riesgo, o digite un numero entre el 0 al 100, gracias:'))
	elif isinstance(state, int) or isinstance(state, float):
		if state > 80 and state <= 100:
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,',',riesgotipo3,',',riesgotipo4,end=".")
		elif state > 35 and state <= 80:
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,',',riesgotipo3,end=".")
		elif state > 14 and state <= 35:
			print(prefijodeRiesgo,riesgotipo1,',',riesgotipo2,end=".")
		elif state > 5 and state <= 14:
			print(prefijodeRiesgo,riesgotipo1,end=".")
		elif state >= 0 and state <= 5:
			print(riesgotipo0)
		else:
			print("\nSe debe ingresar al sistema un  numero positivo entre  0 a 100,\n Correspondiente a la Clasificación IRCA (%).")
			waterQuality(input('Ingrese por favor usted el tipo de riesgo, o digite un numero entre el 0 al 100, gracias:'))

waterQuality(input('Detector del nivel de la calidad del agua y a que Entidades notificar\nIngrese por favor usted el tipo de riesgo, o digite un numero entre el 0 al 100, gracias:'))