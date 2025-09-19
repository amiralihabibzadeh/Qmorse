class bimorse:
    translate = {
        '01': 'A','1000': 'B','1010': 'C','100': 'D',
        '0': 'E','0010': 'F','110': 'G','0000': 'H',
        '00': 'I','0111': 'J','101': 'K','0100': 'L',
        '11': 'M','10': 'N','111': 'O','0110': 'P',
        '1101': 'Q','010': 'R','000': 'S','1': 'T',
        '001': 'U','0001': 'V','011': 'W','1001': 'X',
        '1011': 'Y','1100': 'Z',
        '01111': '1','00111': '2','00011': '3','00001': '4','00000': '5',
        '10000': '6','11000': '7','11100': '8','11110': '9','11111': '0',
        '010101': '.', '110011': ',', '001100': '?','10010': '!',
        '011010': ':','010110': ';','10101': "'",'100101': '-',
        '101101': '/','011011': '(', '0110111': ')','111111': '@',
        '101010': '&','100011': '#','110110': '$','111010': '%',
        '101110': '^','001011': '*','011101': '+','000101': '=',
        '010011': '_','001010': '"','0101011': '`','100111': '[',
        '101111': ']','110101': '{','111001': '}','010111': '|',
        '011001': '<','011111': '>','100001': '~'
    }
    encode = {v: k for k, v in translate.items()}

    @staticmethod
    def read_text(path):
        if not path.endswith('.txt'):
            raise ValueError('File is not text')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        return content

    @staticmethod
    def read_bimorse(bimorse_path):
        if not bimorse_path.endswith('.bimorse'):
            raise ValueError('File is not bimorse')
        try:
            with open(bimorse_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'File at {bimorse_path} does not exist')
        for ch in content:
            if ch not in '01.':
                raise ValueError('File contains characters other than 0, ., 1 — corrupted')
        return content
    
    @staticmethod
    def to_bimorse(text):
        text = text.replace('    ', '\t')
        result = []
        for ch in text:
            if ch == ' ':
                result.append('..')
            elif ch == '\t':
                result.append('...')
            elif ch == '\n':
                result.append('....')
            else:
                result.append(bimorse.encode.get(ch.upper(), '-un-'))
        out = []
        for i, seq in enumerate(result):
            out.append(seq)
            if i < len(result) - 1:
                if seq not in ['..','...','....'] and result[i+1] not in ['..','...','....']:
                    out.append('.')
        return ''.join(out)

    @staticmethod
    def to_text(bimorse_content):
        result = []
        i = 0
        seq = ''
        while i < len(bimorse_content):
            if bimorse_content[i] in '01':
                seq += bimorse_content[i]
                i += 1
            elif bimorse_content[i] == '.':
                dots = 0
                while i < len(bimorse_content) and bimorse_content[i] == '.':
                    dots += 1
                    i += 1
                if seq:
                    result.append(bimorse.translate.get(seq, '-un-'))
                    seq = ''
                if dots == 2:
                    result.append(' ')
                elif dots == 3:
                    result.append('    ')
                elif dots >= 4:
                    n = dots // 4
                    result.append(n*'\n')
            else:
                i += 1
        if seq:
            result.append(bimorse.translate.get(seq, '-un-'))
        return ''.join(result)

