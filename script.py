import codecs
import re


def fix_encoding(text):
    replacements = {
        'Ã¢': 'â', 'Ã©': 'é', 'Ã¨': 'è', 'Ãª': 'ê', 'Ã«': 'ë',
        'Ã®': 'î', 'Ã¯': 'ï', 'Ã´': 'ô', 'Ã¶': 'ö', 'Ã»': 'û',
        'Ã¼': 'ü', 'Ã ': 'à', 'Ã§': 'ç', 'Ã¹': 'ù', 'Ã±': 'ñ',
        'Ã³': 'ó', 'Ã­': 'í', 'Ãº': 'ú', 'Ã¡': 'á', 'Ã½': 'ý',
        'Ã°': 'ð', 'Ã¾': 'þ', 'Ã¦': 'æ', 'Ã¸': 'ø', 'Ã¥': 'å',
        'Ã¿': 'ÿ',

        'Ã‚': 'Â', 'Ã‰': 'É', 'Ãˆ': 'È', 'ÃŠ': 'Ê', 'Ã‹': 'Ë',
        'ÃŽ': 'Î', 'Ã': 'Ï', 'Ã"': 'Ô', 'Ã–': 'Ö', 'Ã›': 'Û',
        'Ãœ': 'Ü', 'Ã€': 'À', 'Ã‡': 'Ç', 'Ã™': 'Ù', 'Ãš': 'Ú', 'Ãž': 'Þ', 'Ã†': 'Æ', 'Ã˜': 'Ø', 'Ã…': 'Å',

        'â‚¬': '€', 'â€"': '—', 'â€œ': '"', 'â€': '"', 'â€¦': '…', 'Â°': '°', 'Â²': '²', 'Â³': '³',
        'Â¹': '¹', 'Â¼': '¼', 'Â½': '½', 'Â¾': '¾', 'â„¢': '™', 'Â©': '©', 'Â®': '®', 'â†"': '↑',
        'â™ ': '♠', 'â™¥': '♥', 'â™¦': '♦', 'â™£': '♣', 'â˜…': '★', 'â˜†': '☆', 'â¯': '~', 'Â': ' ',
        'Ð': 'à', '"™': "\\'", '¢': '•',
    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    # Correction des nombres suivis d'un point d'interrogation (probablement des espaces)
    text = re.sub(r'(\d+)\?(\d+)', r'\1 \2', text)

    return text

def fix_sql_encoding(input_file, output_file):
    try:
        print('Reading input file...')
        with codecs.open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        print('Fixing encoding issues...')
        fixed_content = fix_encoding(content)

        print('Writing output file...')
        with codecs.open(output_file, 'w', encoding='utf-8') as file:
            file.write(fixed_content)

        print('Encoding correction completed successfully.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

input_file = 'old.sql'
output_file = 'new.sql'

fix_sql_encoding(input_file, output_file)