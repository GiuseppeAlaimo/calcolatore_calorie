# Calcolatore delle calorie
# Autore: Alaimo Giuseppe


#calcolare BMR = Basic Metabolic Rate
def calcolo_BMR(sesso, peso, altezza, anni):
	if (sesso == "uomo" or "maschio"):
		bmr = 66.5 + (13.75 * peso) + (5.003 * altezza) - (6.755 * anni)
	else:
		bmr = 655.1 + (9.563 * peso) + (1.850 * altezza) - (4.676 * anni)
	print("Il tuo metabolismo basale è di calorie", round(bmr, 2))
	return bmr


# Calcolo DCR (Daily Calorie Requirement)
def calcolo_dcr(BRM):
	dcr = BRM
	ti_alleni = input("Ti alleni regolarmente? Si o No? ")
	if (ti_alleni == "si"):
		quante_volte = int(input("Quante volte a settimana? "))
		if (quante_volte == 1):
			dcr = BMR * 1.2
		elif (quante_volte == 2):
			dcr = BMR * 1.375
		elif (quante_volte >=3 or quante_volte <= 5):
			dcr = BMR * 1.55
		else :
			dcr = BMR * 1.75
		print("Il tuo fabbisogno calorico sale a", round(dcr, 2), "calorie")
	else :
		print("Allenarsi fa bene alla salute!")
	return dcr


# Calcolo calorie per dimagrire o mettere massa
def dimagrire_ingrassare(dcr):
	print("Per aumentare di peso devi assumere dalle", round(dcr + 300, 2), "alle", round(dcr + 500, 2), "calorie")
	print("Per diminuire di peso devi assumere dalle", round(dcr - 500), "alle", round(dcr - 300), "calorie")


# Inserimento dati
sesso = input("Inserisci il sesso: ")
peso = int(input("Inserisci il tuo peso: "))
altezza = int(input("Inserisci la tua altezza: "))
anni = int(input("Inserisci la tua età: "))

# Calcolo di tutti i dati
BMR = calcolo_BMR(sesso, peso, altezza, anni)
DCR = calcolo_dcr(BMR)
dimagrire_ingrassare(DCR)