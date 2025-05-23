
from datetime import datetime

with open("output.txt", "w") as f:
    f.write(f"Hello, World! - aggiornato alle {datetime.utcnow()} UTC\n")
