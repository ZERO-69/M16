# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))