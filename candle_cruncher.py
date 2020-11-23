import streamlit as st

# wax density in kg/l
density = 0.8842 

st.title('Candle Cruncher 🕯️ ⚖️')

st.header('Fragrance Weight')

# Fragrance Option
option = st.selectbox(
    'What fragrance are you mixing?',
    ['Christmas Day', 'Orange Grove', 'Anything Else'])

# Input Volume
volume = st.number_input('Wax volume (in liters)', min_value=0.0, 
        max_value=600.0, value=270.0, step=1.00, format=None, key=None)

# Calculate fragrance weight
if option == 'Christmas Day':
    weight = 0.08125*(volume*density)
elif option == 'Orange Grove':
    weight = 0.09375*(volume*density)
else:
    weight = 0.0875*(volume*density)

# Convert kg to lbs
weight = 2.20462*weight
weight_pounds = int(weight)
weight_ounces = weight*16.0 - float(weight_pounds)*16.0

# Print the result
st.success('Mix this much fragrance: %0.2f lbs %0.2f oz' % (weight_pounds, weight_ounces))

st.header('Target Volume')

# Input Pots

pots= st.number_input('Number of pots', min_value=1.0, 
        max_value=110.0, value=80.0, step=1.00, format=None, key=None)

weight_kg = pots*1.81437
target = weight_kg/0.884859

# Print the result
st.success('Your volume target is: %0.2f liters' % (target))
