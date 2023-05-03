REF_BYTE_LENGTH = 3
LENGTH_BITS = 7
OFFSET_BITS = 8 * (REF_BYTE_LENGTH - 1) - LENGTH_BITS
WINDOW_SIZE = 2**OFFSET_BITS - 1
LENGTH_THRESHOLD = 2
MAX_REF_LENGTH = 2**LENGTH_BITS - 1
CHUNK_SIZE = 65536
OFFSET_MASK = WINDOW_SIZE
LENGTH_MASK = MAX_REF_LENGTH << OFFSET_BITS