def get_convert_usd():
    amount_by = int(input('Введите сумму в белорусских рублях: '))
    kurs_convertation_usd = float(input('Введите курс конвертации в долларах: '))
    return round(amount_by* kurs_convertation_usd, 2)