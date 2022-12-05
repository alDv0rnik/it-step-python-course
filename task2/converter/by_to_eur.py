def get_convert_eur():
    amount_by = int(input('Введите сумму в белорусских рублях: '))
    kurs_convertation_eur = float(input('Введите курс конвертации в евро: '))
    return round(amount_by * kurs_convertation_eur, 2)