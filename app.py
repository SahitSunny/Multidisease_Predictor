from datetime import datetime, timedelta
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from models import *
from utils import *



st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


with st.sidebar:
    selected = option_menu('Menstrual Cycle and Disease Prediction',
                           [
                               'Next Cycle Predictor',
                               'Diabetes Prediction',
                               'Heart Disease Prediction',
                               'Parkinsons Prediction',
                               'Polycystic Ovarian Syndrome',
                           ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart',
                                  'person', 'person-circle'],
                           default_index=0)


if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    diab_diagnosis = ''


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

if selected == 'Heart Disease Prediction':


    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        oldpeak = st.text_input('ST depression induced by exercise')
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        cp = st.text_input('Chest Pain types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major vessels colored by flourosopy')


    heart_diagnosis = ''


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


if selected == "Parkinsons Prediction":


    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        PPQ = st.text_input('MDVP:PPQ')
        APQ5 = st.text_input('Shimmer:APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        DDP = st.text_input('Jitter:DDP')
        APQ = st.text_input('MDVP:APQ')
        DFA = st.text_input('DFA')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        Shimmer = st.text_input('MDVP:Shimmer')
        DDA = st.text_input('Shimmer:DDA')
        spread1 = st.text_input('spread1')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')


    parkinsons_diagnosis = ''


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
        blood_group_input = (st.text_input('Blood Group'))
        blood_group = blood_group_mapper(blood_group_input)
        skin_darkening = yes_no_mapper(
            st.text_input('Skin Darkening (Yes/No)'))
        hair_loss = yes_no_mapper(st.text_input('Hair Loss (Yes/No)'))
        avg_f_size_r = st.text_input('Average Follicle Size (Right in mm)')
        endometrium = st.text_input('Endometrium Thickness (in mm)')

    with col2:
        pulse_rate = st.text_input('Pulse Rate (beats per minute)')
        rr_breaths = st.text_input('Respiratory Rate ')
        hb = st.text_input('Hemoglobin ')
        cycle = st.text_input('Cycle Regular/Irregular (R/I)')
        cycle_length = st.text_input('Cycle Length (in days)')
        pimples = yes_no_mapper(st.text_input('Pimples (Yes/No)'))
        fast_food = yes_no_mapper(st.text_input(
            'Fast Food Consumption (Yes/No)'))

    with col3:
        marriage_status = st.text_input('Marriage Status (in years)')
        pregnant = yes_no_mapper(st.text_input('Pregnant (Yes/No)'))
        abortions = st.text_input('Number of Abortions')
        fsh = st.text_input('Follicle Stimulating Hormone')
        lh = st.text_input('Luteinizing Hormone')
        reg_exercise = yes_no_mapper(
            st.text_input('Regular Exercise (Yes/No)'))
        bp_systolic = st.text_input('Systolic Blood Pressure (mmHg)')

    with col4:
        hip = st.text_input('Hip Measurement (in inches)')
        waist = st.text_input('Waist Measurement (in inches)')
        tsh = st.text_input('Thyroid Stimulating Hormone')
        amh = st.text_input('Anti-Müllerian Hormone')
        prl = st.text_input('Prolactin (PRL in ng/mL)')
        bp_diastolic = st.text_input('Diastolic Blood Pressure (mmHg)')
        follicle_no_l = st.text_input('Number of Follicles (Left)')

    with col5:
        vit_d3 = st.text_input('Vitamin D3 (in ng/mL)')
        prg = st.text_input('Progesterone (PRG in ng/mL)')
        rbs = st.text_input('Random Blood Sugar')
        weight_gain = yes_no_mapper(st.text_input('Weight Gain (Yes/No)'))
        hair_growth = yes_no_mapper(
            st.text_input('Excess Hair Growth (Yes/No)'))
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
            outcome = 'The person has Polycystic Ovarian Syndrome'
            st.error(outcome)
        else:
            outcome = 'The person does not have Polycystic Ovarian Syndrome'
            st.success(outcome)



if selected == 'Next Cycle Predictor':
    st.title('Next Cycle Prediction')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        CycteNumber = st.number_input('Cycte Number')
        Group = st.number_input('Group')
        CycteWithPeakorNot = st.selectbox(
            'Cycte With Peak or Not', [0, 1])
        ReproductiveCategory = st.number_input('Reproductive Category')

    with col2:
        EstimatedDayofOvulation = st.number_input(
            'Estimated Day of Ovulation')
        LengthofLuteatPhase = st.number_input('Length of Luteal Phase')
        FirstDayofHigh = st.number_input('First Day of High')
        TotatNumberofHighDays = st.number_input(
            'Total Number of High Days')

    with col3:
        TotatHighPostPeak = st.number_input('Total High Post Peak')
        TotatDaysofFertitity = st.number_input('Total Days of Fertility')
        TotatNumberofPeakDays = st.number_input(
            'Total Number of Peak Days')
        TotatFertitityFormuta = st.number_input(
            'Total Fertility Formula')

    with col4:

        MensesScoreDayOne = st.number_input('Menses Score Day One')
        MensesScoreDayTwo = st.number_input('Menses Score Day Two')
        MensesScoreDayThree = st.number_input('Menses Score Day Three')
        MensesScoreDayFour = st.number_input('Menses Score Day Four')
        MensesScoreDayFive = st.number_input('Menses Score Day Five')

    with col5:
        LengthofMenses = st.number_input('Length of Menses')
        TotatMensesScore = st.number_input('Total Menses Score')
        NumberofDaysofIntercourse = st.number_input(
            'Number of Days of Intercourse')
        IntercourseInFertiteWindow = st.selectbox(
            'Intercourse In Fertile Window', [0, 1])

        user_date = st.date_input('Date')

    if st.button('Predict Date'):
        user_input = [
            CycteNumber,
            Group,
            CycteWithPeakorNot,
            ReproductiveCategory,
            EstimatedDayofOvulation,
            LengthofLuteatPhase,
            FirstDayofHigh,
            TotatNumberofHighDays,
            TotatHighPostPeak,
            TotatDaysofFertitity,
            TotatNumberofPeakDays,
            TotatFertitityFormuta,
            LengthofMenses,
            MensesScoreDayOne,
            MensesScoreDayTwo,
            MensesScoreDayThree,
            MensesScoreDayFour,
            MensesScoreDayFive,
            TotatMensesScore,
            NumberofDaysofIntercourse,
            IntercourseInFertiteWindow
        ]

        user_input = [float(x) for x in user_input]

        predict_date = cycle_model.predict([user_input])

        predict_usual = ususal_model.predict([user_input])

        st.success("Next Expected Cycle on : " +
                   add_days_to_date(user_date, predict_date))

        if predict_usual == 0:
            st.success("ususal")
        else:
            st.error("unsual")

            card_style = """
                        <style>
                        .card {
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                            background-color: #f8f9fa;
                            margin-bottom: 20px;
                        }
                        .card-title {
                            font-size: 20px;
                            font-weight: bold;
                            color: #333;
                            margin-bottom: 10px;
                        }
                        .card-message {
                            font-size: 16px;
                            color: #555;
                        }
                        </style>
                        """

            st.markdown(card_style, unsafe_allow_html=True)

            st.markdown("""
        <div class="card">
            <div class="card-title">Important Message</div>
            <div class="card-message">This is a custom card displaying your message. You can use this to highlight important information or alerts in your app.</div>
        </div>
        """, unsafe_allow_html=True)
