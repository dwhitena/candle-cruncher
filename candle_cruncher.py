import streamlit as st

# wax density in kg/l
density = 0.8810 

st.title('Candle Cruncher 🕯️ ⚖️')


#----------------
# Target Volume
#----------------

st.header('Target Volume')

# Input Pots

pots= st.number_input('Number of pots', min_value=1.0, 
        max_value=200.0, value=80.0, step=1.00, format=None, key=None)

weight_kg = pots*1.81437
target = weight_kg/0.884859

# Print the result
st.success('Your volume target is: %0.2f liters' % (target))


#-----------------
# Fragrance Weight
#-----------------

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
weight = 2.20462*weight*0.97 
weight_pounds = int(weight)
weight_ounces = weight*16.0 - float(weight_pounds)*16.0

# Print the result
st.success('Mix this much fragrance: %0.2f lbs %0.2f oz' % (weight_pounds, weight_ounces))


#--------------------
# Height Measurement
#--------------------

st.header('Manual Measurement')

# Inches
inches = st.number_input('Inches', min_value=0, 
        max_value=36, value=14, step=1, format=None, key=None)

# Fragrance Option
fraction = st.selectbox(
    'Remainder',
    ['0', '1/8', '1/4', '3/8', '1/2', '5/8', '3/4', '7/8'])

# Convert full length
if fraction != '0':
    length = inches + float(fraction.split('/')[0])/float(fraction.split('/')[1])
else:
    length = inches

# Convert to volume
manual_vol = 706.5*length*0.016

# Get fragrance dosing
if option == 'Christmas Day':
    manual_weight = 0.08125*(manual_vol*density)
elif option == 'Orange Grove':
    manual_weight = 0.09375*(manual_vol*density)
else:
    manual_weight = 0.0875*(manual_vol*density)

# Convert kg to lbs
manual_weight = 2.20462*manual_weight*0.97 
manual_weight_pounds = int(manual_weight)
manual_weight_ounces = manual_weight*16.0 - float(manual_weight_pounds)*16.0

# Print the result
st.success('Actual volume is %0.2f. Mix this much fragrance: %0.2f lbs %0.2f oz' % (manual_vol, manual_weight_pounds, manual_weight_ounces))
