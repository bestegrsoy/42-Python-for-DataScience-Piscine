import time
from datetime import datetime

epoch_time = time.time()

scientific_notation = "{:.2e}".format(epoch_time)

formatted_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970:{epoch_time: .4f} or {scientific_notation} in scientific notation")
print(formatted_date)
