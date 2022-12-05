def get_convert_rub():
    amount_by = int(input('Введите сумму в белорусских рублях: '))
    kurs_convertation_rub = float(input('Введите курс конвертации в российских рублях: '))
    return round(amount_by * kurs_convertation_rub, 2)