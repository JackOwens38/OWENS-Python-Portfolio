import streamlit as st
import pandas as pd
from datetime import datetime

# Page heading
st.title("Summer 2025 Cycling Tracker")

# Ride info
st.write("""This summer, I will be completing a cross-country bike ride to raise funds and awareness for lung cancer patients
         and their families. The ride will take me from San Francisco to South Jersey, including a stop at Notre Dame.           
         """)
st.write("""This app allows you to follow along my journey with me! Select a day, and you will see where I expect to start and finish,
         expected ride details for that day, overall progress, photos, and more!
        """)
st.markdown("""For more info, including to support the ride, visit **rhbe.org**.
        """)

# Load the trip data
df = pd.read_csv("EoC_Final.csv")

# Reads the dataset, converts each of the days into the correct format
df['Date'] = pd.to_datetime(df['Date'] + ' 2025', format='%b %d %Y')
today = datetime.now() # Automatically updates the day

# Calculates the totals
total_miles = df['Miles'].sum()
total_ascent = df['Ascent'].sum()
total_days = len(df)

# Calculates the completed miles up to the selected day
completed_miles = df[df['Date'] < today]['Miles'].sum()
completed_ascent = df[df['Date'] < today]['Ascent'].sum()
days_completed = df[df['Date'] < today].count()

# Adds image of full route
from PIL import Image # Imports library that makes it easy to open images in Streamlit
route_map = Image.open('data/us_map.png')
st.image(route_map, caption="Route: San Francisco, CA to Ocean City, NJ", use_column_width=True)

# Button that allows users to view the full route in another link
if st.button("View Route", key='view_route_main'): 
    route_url = "https://ridewithgps.com/routes/49742853"
    st.write(f"[Open Route in Ride with GPS]({route_url})")

# Select a Day
day_options = [f"Day {int(row['Day'])}: {row['Start Day']} to {row['Finish Day']}" for _, row in df.dropna(subset=['Day']).iterrows()]
# The above row creates options for the users to select in the dropdown listed below; it creates an option for each day, including start and finish location
day_options.insert(0, "Today") # This adds an option for today, updated in real time
selected_day = st.selectbox("Select a Day", day_options)

# Determine the selected day's data
if selected_day == "Today": # Provides a default option for today
    if not df[df['Date'] == pd.to_datetime(today.strftime('%Y-%m-%d'))].empty: # This removes every row other than today
        selected_row = df[df['Date'] == pd.to_datetime(today.strftime('%Y-%m-%d'))].iloc[0] # This adds today, in the correct format
    else: # This finds out how many days there are until the start of the ride, which creates a countdown
        selected_row = df.iloc[0]  
        days_until_start = (selected_row['Date'] - today).days
        st.header(f"Countdown to Day 1: {days_until_start} days")
else:
    day_number = int(selected_day.split()[1].replace(':', '')) # This isolates the day number from the selected option
    selected_row = df[df['Day'] == day_number].iloc[0] # Gathers all of the info from the user's selected day

# Display the selected day's stats
st.header(f"Day {int(selected_row['Day'])} - {selected_row['Start Day']} to {selected_row['Finish Day']}")
with st.container(): # This uses markdown formatting to show data for the selected day
    st.markdown(f"**Start City:** {selected_row['Start Day']}")
    st.markdown(f"**End City:** {selected_row['Finish Day']}")
    st.markdown(f"**Miles:** {selected_row['Miles']} miles")
    st.markdown(f"**Elevation:** {selected_row['Ascent']} ft")

# Update overall progress based on selected day
# Copied mostly from above section
completed_miles = df[df['Day'] <= selected_row['Day']]['Miles'].sum()
completed_ascent = df[df['Day'] <= selected_row['Day']]['Ascent'].sum()
days_completed = selected_row['Day']

# Overall Progress Section
st.header("Overall Progress")
with st.container(): # Each section displays a progress bar of how far into the ride we are
    st.metric("Total Miles", f"{completed_miles} / {total_miles} miles")
    st.progress(completed_miles / total_miles)
    st.metric("Total Ascent", f"{completed_ascent} / {total_ascent} ft")
    st.progress(completed_ascent / total_ascent)
    st.metric("Total Days", f"{days_completed} / {total_days} days")
    st.progress(days_completed / total_days)

# Photo Gallery that will update upon day's completion
st.header("Photo Gallery")
pre_ride_image = Image.open('data/pre_ride.jpg')

if selected_day == "Today" or selected_row['Date'] <= today:
    # Show the default pre-ride image for before the ride
    st.image(pre_ride_image, caption="Pre-Ride Photo", use_column_width=True)
else:
    # This day has not yet occurred, so there are not pictures yet
    st.write("This day has not yet occurred, please check back after this day for pictures!")
    st.write("In the meantime, here is an image from before the ride:")
    st.image(pre_ride_image, caption="Pre-Ride Photo", use_column_width=True)

# This section includes a lot of additional information that I took from other documents I have built for the ride; I was able to format it with markdown.
st.header("Additional Information")
st.markdown("""
### **How You Can Help**

- **Donate!**  
  - Check out our [website](https://www.rhbe.org/events/rhbe-classic/) and [donate here](https://givebutter.com/RHBE2025) to support lung cancer patients.  
- **Ride with me virtually on June 22!**  
  - While I am riding across Indiana to arrive at Notre Dame on June 22, ride virtually with me! [Register here](https://forms.gle/s6qR1ZdrQS1hZstw9), share your efforts on social media, and tag RHBE. This will help to raise awareness for support of lung cancer patients.  
- **Provide a tribute!**  
  - Throughout the ride, we will honor those that have been affected by lung cancer with daily tributes. We would love to include your loved one who has battled or is battling lung cancer. To provide a tribute, fill out the [tribute form here](https://forms.gle/s6qR1ZdrQS1hZstw9).  
- **Be part of the team!**  
  - Over the next few months, we will be planning stops along the ride, figuring out SAG logistics, and much more. There are many ways to contribute, and each contribution will help to set us up for success. *"Many hands make light work!"*  
- **Market the ride!**  
  - The more widespread this mission becomes, the more lung cancer patients' lives are positively impacted. There are plenty of communications, marketing, and social media opportunities to be explored. With your support, we can spread the influence of this ride far beyond the limits of my communities. Follow RHBE on social media and share our updates!  
- **Get organizations involved!**  
  - From San Francisco to the Jersey Shore, I am fortunate to have benefitted from the support of many organizations and people. There are countless other groups out there, and each possesses unique ways to offer support; help me find these opportunities. To sponsor the ride or offer other support, contact [info@rhbe.org](mailto:info@rhbe.org).  
---

### **About Ride Hard Breathe Easy**

Lung cancer patients often face a challenging and lonely journey after receiving their diagnosis. With our partners, we passionately support the need for early detection, financially support patients and caregivers, and work towards erasing the stigma of this disease. By bringing the community together, we have raised over $1,000,000, helped over 2,000 patients, and proudly highlight that over 93% of our donations go directly to programs benefiting patients.  

We provide financial support to lung cancer patients at our partner hospitals:
- Crozer Health
- Dartmouth Cancer Center
- Duke Cancer Institute
- Fox Chase Cancer Center
- Jefferson Health
- Johns Hopkins
- Penn's Abramson Cancer Center
- Temple Health  

For more information about Ride Hard Breathe Easy, visit [www.RHBE.org](http://www.rhbe.org).  
""")