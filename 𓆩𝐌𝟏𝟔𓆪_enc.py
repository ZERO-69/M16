# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))