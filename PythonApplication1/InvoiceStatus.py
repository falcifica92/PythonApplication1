from enum import Enum

class InvoiceStatus(Enum):
    PROCESSING = 1
    SENT = 2
    REJECTED = 3
    CANCELLED = 4
