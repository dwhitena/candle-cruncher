import streamlit as st

# wax density in kg/l
density = 0.884859 

st.title('Candle Cruncher 🕯️ ⚖️')

# Fragrance Option
option = st.selectbox(
    'What fragrance are you mixing?',
    ['Christmas Day', 'Orange Grove', 'Anything Else'])

# Input Volume
volume = st.number_input('Wax volume (in liters)', min_value=0.0, 
        max_value=600.0, value=400.0, step=1.00, format=None, key=None)

# Calculate fragrance weight
if option == 'Christmas Day':
    weight = 0.08125*(volume*density)
elif option == 'Orange Grove':
    weight = 0.09375*(volume*density)
else:
    weight = 0.0875*(volume*density)

# Convert kg to lbs
weight = 2.20462*weight

# Print the result
st.success('Mix this much fragrance: %0.2f pounds (%0.2f oz)' % (weight, weight*16.0))
