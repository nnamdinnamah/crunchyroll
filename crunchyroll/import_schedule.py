import schedule

def test():
    print("Test this out!")
 
schedule.every(10).seconds.do(test)
 
while True:
    schedule.run_pending()
