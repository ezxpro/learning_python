from datetime import datetime

wait_until = datetime.now().second + 2

while True:
    if datetime.now().second >=50:
        continue # put this continue here just to show that
                 # it skips one iteration
                 # This also causes a bug if wait_until > 50
                 # because the break is skipped, and since the
                 # variable is never reset it'll loop forever
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break        
