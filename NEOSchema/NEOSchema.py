from datetime import datetime
import math

def jS_ts_splitter(ts: int):

    '''Return a python datetime object with the millisecond resolution of
    an input int representing the number of milliseconds since
    Midnight, January 1, 1970 local time.

    This python datetime objects maximum sample frequency is 
    1 million Hz, or 1 megahurtz.
   
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
    
    final_count_down = ts*(10**3)
    
    #step 1: count the ms in years, oh how the time passes...
    ms_in_365_year = 365*24*60*60*1000000
    ms_in_Lep_year = 366*24*60*60*1000000
    
    years1970 = 0
    #account for leap year
    while final_count_down > ms_in_365_year:
        year = 1970
        if bool(year%4):
            final_count_down -= ms_in_365_year
        else: 
            final_count_down -= ms_in_Lep_year
        
        years1970 +=1
    
    #the number of years in yearss1970loops
    fyears = int(years1970 + year)
    
    #step 2a: count the months
    ms_in_day = ms_in_365_year/365
    ######this could be made more efficent
    if bool(fyears%4):
        
        monthsy = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ms_in_month = [x*ms_in_day for x in monthsy]
        
        month_ind = 0
        
        while final_count_down > ms_in_month[month_ind]:
            final_count_down -= ms_in_month[month_ind]
            month_ind += 1
            
    else:
        monthsyl = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ms_in_month = [x*ms_in_day for x in monthsyl]
        #month_ind = 0
        while final_count_down < ms_in_month[month_ind]:
            final_count_down -= ms_in_month[month_ind]
            month_ind += 1
    ######  
    fmonth = month_ind + 1
    
    #step 2b: count the days
    ms_in_day = ms_in_365_year/365
    fdays = (math.floor(final_count_down/ms_in_day))
    final_count_down -= fdays*ms_in_day
    
    #step 3: count the hours
    ms_in_hour = ms_in_day/24
    fhour = math.floor(final_count_down/ms_in_hour)
    final_count_down -= fhour*ms_in_hour
    
    #step 4: count the minutes
    ms_in_minute = ms_in_hour/60
    fmins = math.floor(final_count_down/ms_in_minute)
    final_count_down -= fmins*ms_in_minute
    
    #step 5: seconds
    ms_in_secs = ms_in_minute/60
    fsecs = math.floor(final_count_down/ms_in_secs)
    final_count_down -= fsecs*ms_in_secs
    
    #step 6: count the microsecounds
    ms_in_ms = ms_in_secs*(10**(-6))
    fms = math.floor(final_count_down/ms_in_ms)
    final_count_down -= fms*ms_in_secs
    
    #toggle printing by uncommenting line below for now
    #print((fyears, fmonth, fdays, fhour, fmins, fsecs, fms))
    
    return datetime(fyears, fmonth, fdays, fhour, fmins, fsecs, fms)
        
   