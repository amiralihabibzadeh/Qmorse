class bimorse:
    """
    A class to encode and decode text into "bimorse" (a Morse-like binary encoding) 
    and save/read both text and bimorse files.

    Attributes:
        translate (dict): Maps bimorse sequences (like '01', '1000') to characters.
        encode (dict): Reverse mapping from characters to bimorse sequences.
    """
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

    bit_table = {
    '0': '00',
    '1': '01',
    '.': '10',
    '█': '11'
    }

    encode = {v: k for k, v in translate.items()}
    reverse_table = {v: k for k, v in bit_table.items()}

    @staticmethod
    def read_text(path):
        """
        Read a text file and normalize line endings.

        Args:
            path (str): Path to a .txt file.

        Returns:
            str: Content of the text file with '\n' line endings.

        Raises:
            ValueError: If the file does not end with '.txt'.
        """
        if not path.endswith('.txt'):
            raise ValueError('File is not text')
        with open(path, 'r', encoding='utf-8') as q:
            content = q.read()
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        return content

    @staticmethod
    def read_bimorse(path):
        """
        Read a bimorse file and validate its content.

        Args:
            path (str): Path to a .bimorse file.

        Returns:
            str: Content of the bimorse file.

        Raises:
            ValueError: If the file contains invalid characters.
            FileNotFoundError: If the file does not exist.
        """
        if not path.endswith('.bimorse'):
            raise ValueError('File is not bimorse')
        with open(path, 'rb') as f:
            data = f.read()
        bits = ''.join(f'{byte:08b}' for byte in data)
        decoded = ''

        for i in range (0 , len(bits) , 2):
            pair = bits[i:i+2]
            if pair in bimorse.reverse_table:
                decoded += bimorse.reverse_table[pair]
        return decoded
    
    @staticmethod
    def to_bimorse(text):
        """
        Convert normal text to bimorse encoding.

        Args:
            text (str): Text to convert.

        Returns:
            str: Bimorse encoded string.
        """
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

        out.insert(0,'█')
        out.append('█')

        return ''.join(out)

    @staticmethod
    def to_text(bimorse_content):
        """
        Convert bimorse content back to normal text.

        Args:
            bimorse_content (str): Bimorse encoded string.

        Returns:
            str: Decoded normal text.
        """
        result = []
        i = 1
        seq = ''
        while i+1 < len(bimorse_content):
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
                else :
                    n = dots // 4
                    result.append(n*'\n')
            else:
                i += 1
        if seq:
            result.append(bimorse.translate.get(seq, '-un-'))
        return ''.join(result)

    @staticmethod
    def save_file(var: str, filename: str) -> None:
        """
        Save a string `var` to a file, either as text or bimorse.
    
        Args:
            var (str): The string to save. Can be:
                - Plain text (like 'Hello world')
                - Bimorse string (like '01.0.1...')
            filename (str): The target filename. Must end with:
                - '.txt' to save as plain text
                - '.bimorse' to save as bimorse
    
        Returns:
            None
    
        Raises:
            ValueError: If file extension is unsupported or content cannot be converted.
    
        Examples:
            >>> bimorse.save_file('Hello', 'hello.bimorse')
            >>> bimorse.save_file('01.0.1', 'output.txt')
        """

        if var.startswith('█') and var.endswith('█'):
            var_type = 'bimorse'
        else:
            var_type = 'text'
        
        if '.' not in filename:
            file_type = 'bimorse'
            filename = filename+ '.bimorse'

        elif filename.endswith('.bimorse'):
            file_type = 'bimorse'

        elif filename.endswith('.txt'):

            file_type = 'text'
        else :
            raise ValueError('File extension must be .txt or .bimorse')


        if var_type == 'bimorse':

            if file_type == 'bimorse':
                bis = ''.join(bimorse.bit_table[c] for c in var)

                if len(bis) %8 != 0:
                    bis += '0' * (8 - len(bis)%8)

                var = int(bis, 2).to_bytes(len(bis) // 8, byteorder ='big')

            elif file_type == 'text':
                var = bimorse.to_text(var)
            
        elif var_type == 'text':

            if file_type == 'text':
                pass

            elif file_type == 'bimorse':
                var = bimorse.to_bimorse(var)
                bis = ''.join(bimorse.bit_table[c] for c in var)

                if len(bis) %8 != 0:
                    bis += '0' * (8 - len(bis)%8)

                var = int(bis, 2).to_bytes(len(bis) // 8, byteorder ='big')

        mode = 'wb' if isinstance(var, bytes) else 'w'
        encoding = None if isinstance(var, bytes) else 'utf-8'

        with open(filename, mode, encoding=encoding) as q:
            q.write(var)
