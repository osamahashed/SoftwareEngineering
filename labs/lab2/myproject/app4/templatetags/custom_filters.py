from django import template
import random

register = template.Library()

@register.filter(name='name_encoder')
def name_encoder(value):
    """
    يقوم بتشفير الاسم بطريقة مميزة مع الحفاظ على الأحرف العربية
    """
    if not value:
        return value
    
    # قاموس التشفير (يمكنك تطويره حسب احتياجاتك)
    encoding_map = {
        'ا': 'آ', 'ب': 'بـ', 'ت': 'تـ', 'ث': 'ثـ',
        'ج': 'جـ', 'ح': 'حـ', 'خ': 'خـ', 'د': 'د',
        'ذ': 'ذ', 'ر': 'ر', 'ز': 'ز', 'س': 'سـ',
        'ش': 'شـ', 'ص': 'صـ', 'ض': 'ضـ', 'ط': 'طـ',
        'ظ': 'ظـ', 'ع': 'عـ', 'غ': 'غـ', 'ف': 'فـ',
        'ق': 'قـ', 'ك': 'كـ', 'ل': 'لـ', 'م': 'مـ',
        'ن': 'نـ', 'ه': 'هـ', 'و': 'و', 'ي': 'يـ',
        'a': 'α', 'b': 'β', 'c': '¢', 'd': '∂',
        'e': 'ε', 'f': 'ƒ', 'g': 'ɢ', 'h': 'н',
        'i': 'ι', 'j': 'נ', 'k': 'к', 'l': 'ℓ',
        'm': 'м', 'n': 'η', 'o': 'σ', 'p': 'ρ',
        'q': 'q', 'r': 'я', 's': 'ѕ', 't': 'τ',
        'u': 'υ', 'v': 'ν', 'w': 'ω', 'x': 'χ',
        'y': 'у', 'z': 'z'
    }
    
    encoded_name = []
    for char in str(value):
        lower_char = char.lower()
        if lower_char in encoding_map:
            # إضافة بعض العشوائية للتشفير
            if random.random() > 0.7:
                encoded_char = f"[{encoding_map[lower_char]}]"
            else:
                encoded_char = encoding_map[lower_char]
            
            # الحفاظ على حالة الأحرف الكبيرة
            if char.isupper():
                encoded_char = encoded_char.upper()
            encoded_name.append(encoded_char)
        else:
            encoded_name.append(char)
    
    return ' '.join(encoded_name) + ' ✦'