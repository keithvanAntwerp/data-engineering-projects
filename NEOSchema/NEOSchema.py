from datetime import datetime

def jS_ts_splitter(ts: int):

    '''Return a python datetime object with the millisecond resolution of
    an input int representing the number of milliseconds since
    January 1, 1970 UTC.

    Matches datatime.fromtimestamp(ints/1000)

    1 microsecond is associated with maximum sample frequency of
    1 million Hz, or 1 megaHz.
   
    This is an inefficient brute force converter of 
    a local-time javaScript Date in int form with the
    intention of learning and applying algorithms.
    
    WEAKNESSES: Doesn't take advantage of any known time 
    stastics or hard limits (limits known with 
    almost certainty) e.g. knowing the year and pruning.
    
    If the time-samples were completely random (max entropy) then 
    this basic algorithm would not be *so* bad in spirit. 

    At any rate, it is a neat and informative way to explore the nuances of
    time and algorithmic complexity.
    '''
    #total_micro_sec = ts*(10**3)
    
    #correct for January 1, 1970 UTC time
    us_corr = 8*60*60*1000000
    
    final_count_down = ts*(10**3)
    if (final_count_down - us_corr) > 0:
        final_count_down = final_count_down - us_corr
    else: final_count_down = 0
        
    print(final_count_down)
    #step 1: count the ms in years, oh how the time passes...
    us_in_365_year = 365*24*60*60*1000000
    us_in_Lep_year = 366*24*60*60*1000000
    
    year = 1970
    
    #account for leap year
    while final_count_down > us_in_365_year:
        
        if bool(year%4):
            final_count_down -= us_in_365_year
        elif not bool(year%4): 
            final_count_down -= us_in_Lep_year
        
        year +=1
    
    #the number of years in yearss1970loops
    fyears = int(year)
    
    #step 2a: count the months
    us_in_day = int(us_in_365_year/365)
    print(us_in_day)
   
    ######this could be made more efficent
    if bool(fyears%4):
        monthsy = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else: monthsy = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    us_in_month = [x*us_in_day for x in monthsy]
    month_ind = 0
        
    while final_count_down > us_in_month[month_ind]:
        final_count_down -= us_in_month[month_ind]
        
        month_ind += 1
    ######  
    fmonth = month_ind + 1
    
    #step 2b: count the days
    fdays = int(final_count_down//us_in_day)
    final_count_down -= fdays*us_in_day
    fdays += 1
    
    #step 3: count the hours
    us_in_hour = int(us_in_day/24)
    fhour = int(final_count_down//us_in_hour)
    final_count_down -= fhour*us_in_hour
    
    #step 4: count the minutes
    us_in_minute = int(us_in_hour/60)
    fmins = int(final_count_down//us_in_minute)
    final_count_down -= fmins*us_in_minute
    
    #step 5: seconds
    us_in_secs = us_in_minute/60
    fsecs = int(final_count_down//us_in_secs)
    final_count_down -= fsecs*us_in_secs
    
    #step 6: count the microsecounds
    us_in_us = int(us_in_secs*(10**(-6)))
    fus = int(final_count_down//us_in_us)
    final_count_down -= fus*us_in_secs
    
    #toggle printing by uncommenting line below for now
    #print((type(fyears), type(fmonth), type(fdays), type(fhour), type(fmins), type(fsecs), type(fus)),
          #(fyears, fmonth, fdays, fhour, fmins, fsecs, fus))
    
    return datetime(fyears, fmonth, fdays, fhour, fmins, fsecs, fus)
        
   
        
   