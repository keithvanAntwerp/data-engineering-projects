from datetime import datetime
import math

def jS_ts_splitter(ts):
    '''
    The Natural Emergent Ordering Schema: NEOS is spacetime.
    
    A brute force converter of a local-time javaScript Date
    WEAKNESS: Doesn't take advantage of any known date 
    stastical ranges or hard limits (limits known with 
    almost certainty)
    
    For processing many dates, not using this knowledge could
    add up? However, if ts were completely random with
    max entropy then this algorithm would not be *so* bad in
    general spirit.
    
    At any rate, it is a great way to explore the nuances of
    time and complexity and it is linked to the optimal 
    digital processing of EM radiation, my favorite.
    '''
    #magic data is January 1, 1970
    total_micro_sec = ts*(10**3)
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
        
   