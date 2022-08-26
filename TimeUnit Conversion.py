while True:
    tp = int(input('1.hour to seconds\n2.seconds to hour\n1 or 2: '))

    if tp == 1:
        hours = int(input('hours: '))
        minutes = int(input('minutes: '))
        seconds = int(input('seconds: '))
        secondsToHours = (hours * 3600) + (minutes * 60) + seconds
        print(secondsToHours, 'seconds')
        print('Exit')
        break
    elif tp == 2:
        secs = int(input('seconds: '))
        hr = int(secs / 3600)
        min = int((secs - (hr * 3600)) / 60)
        sec = int(((secs - (hr * 3600) - min * 60) / 60) * 60)
        print(hr,':', min,':', sec)
        print('Exit')
        break


    ## elif tp == "3" or "Exit" : ##
        ## break ##


