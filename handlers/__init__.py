from .start import start_router
from .transactions import add_transaction_router


all_routers = [
    start_router,
    add_transaction_router
]