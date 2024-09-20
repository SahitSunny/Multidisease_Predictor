import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(
    open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(
    open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(
    open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

pco_model = pickle.load(
    open(f'{working_dir}/saved_models/model.pkl', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Polycystic Ovarian Syndrome'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'person-circle'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.error(diab_diagnosis)
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.error(heart_prediction)
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_prediction)

    

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.error(parkinsons_prediction)
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.success(parkinsons_prediction)


if selected == 'Polycystic Ovarian Syndrome':

    st.title('Polycystic Ovarian Syndrome Prediction')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age (in years)')
        weight = st.text_input('Weight (in kilograms)')
        height = st.text_input('Height (in centimeters)')
        bmi = st.text_input('BMI (Body Mass Index)')
        blood_group = st.text_input('Blood Group')
        skin_darkening = st.text_input('Skin Darkening (Yes/No)')
        hair_loss = st.text_input('Hair Loss (Yes/No)')
        avg_f_size_r = st.text_input('Average Follicle Size (Right in mm)')
        endometrium = st.text_input('Endometrium Thickness (in mm)')

    with col2:
        pulse_rate = st.text_input('Pulse Rate (beats per minute)')
        rr_breaths = st.text_input('Respiratory Rate (breaths per minute)')
        hb = st.text_input('Hemoglobin (Hb in grams per deciliter)')
        cycle = st.text_input('Cycle Regular/Irregular (R/I)')
        cycle_length = st.text_input('Cycle Length (in days)')
        pimples = st.text_input('Pimples (Yes/No)')
        fast_food = st.text_input('Fast Food Consumption (Yes/No)')

    with col3:
        marriage_status = st.text_input('Marriage Status (in years)')
        pregnant = st.text_input('Pregnant (Yes/No)')
        abortions = st.text_input('Number of Abortions')
        fsh = st.text_input('Follicle Stimulating Hormone (FSH in mIU/mL)')
        lh = st.text_input('Luteinizing Hormone (LH in mIU/mL)')
        reg_exercise = st.text_input('Regular Exercise (Yes/No)')
        bp_systolic = st.text_input('Systolic Blood Pressure (mmHg)')
        

    with col4:
        hip = st.text_input('Hip Measurement (in inches)')
        waist = st.text_input('Waist Measurement (in inches)')
        tsh = st.text_input('Thyroid Stimulating Hormone (TSH in mIU/L)')
        amh = st.text_input('Anti-Müllerian Hormone (AMH in ng/mL)')
        prl = st.text_input('Prolactin (PRL in ng/mL)')
        bp_diastolic = st.text_input('Diastolic Blood Pressure (mmHg)')
        follicle_no_l = st.text_input('Number of Follicles (Left)')

    with col5:
        vit_d3 = st.text_input('Vitamin D3 (in ng/mL)')
        prg = st.text_input('Progesterone (PRG in ng/mL)')
        rbs = st.text_input('Random Blood Sugar (RBS in mg/dL)')
        weight_gain = st.text_input('Weight Gain (Yes/No)')
        hair_growth = st.text_input('Excess Hair Growth (Yes/No)')
        follicle_no_r = st.text_input('Number of Follicles (Right)')
        avg_f_size_l = st.text_input('Average Follicle Size (Left in mm)')
        

    outcome = ''

    if st.button('Test Results'):
        user_input = [
            age,
            weight,
            height,
            bmi,
            blood_group,
            pulse_rate,
            rr_breaths,
            hb,
            cycle,
            cycle_length,
            marriage_status,
            pregnant,
            abortions,
            fsh,
            lh,
            hip,
            waist,
            tsh,
            amh,
            prl,
            vit_d3,
            prg,
            rbs,
            weight_gain,
            hair_growth,
            skin_darkening,
            hair_loss,
            pimples,
            fast_food,
            reg_exercise,
            bp_systolic,
            bp_diastolic,
            follicle_no_l,
            follicle_no_r,
            avg_f_size_l,
            avg_f_size_r,
            endometrium
        ]

        user_input = [float(x) for x in user_input]

        predict = pco_model.predict([user_input])
        
        if predict[0] == 1:
            outcome = 'The person has Polycystic Ovarian Syndrome';
            st.error(outcome)
        else:
            outcome = 'The person does not have Polycystic Ovarian Syndrome'
            st.success(outcome)

            