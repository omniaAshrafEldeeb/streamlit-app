import streamlit as st
import pickle
import pandas as pd
def app():
    b,n = st.columns([2,3])
    with n:st.title("Tests")
    choose = st.selectbox("",['Blood Pressure',"Diabetes", 
],)
    if choose == 'Diabetes':
        with st.spinner("Calculating......."):

            st.subheader ('Diabetes Prediction Test')
            c= st.container()
            mymodel = pickle.load(open(r"C:\Users\MF\Downloads\SVM.pkl",'rb'))


            
            st.info('Easy Application for Diabetes prediction Desease')
            st.sidebar.header('Feature Selection')

            Pregnancies_value = st.slider("How many pregnancies have you had?", 0, 20)
            Glucose_value = st.slider('Glucose', 30, 200)
            BloodPressure_value =st.number_input('BloodPressure',20,130)
            SkinThickness_value = st.number_input('SkinThickness',3,105)
            Insulin_value = st.slider('Insulin',5,900)
            BMI_value = st.number_input('BMI',10.0,150.0,step =0.01)
            DiabetesPedigreeFunction_value = st.number_input('DiabetesPedigreeFunction',0.000,4.000,step =0.001)
            Age_value = st.slider("How old are you?", 7, 130)

            Pregnancies_value = float (Pregnancies_value)
            Glucose_value = float (Glucose_value)
            BloodPressure_value =float (BloodPressure_value)
            SkinThickness_value = float (SkinThickness_value)
            Insulin_value = float (Insulin_value)
            BMI_value = float (BMI_value)
            DiabetesPedigreeFunction_value = float (DiabetesPedigreeFunction_value)
            Age_value = float (Age_value)
                




            print("_________________________",type(Age_value))
            df = pd.DataFrame({'Pregnancies':[Pregnancies_value],'Glucose': [Glucose_value],'BloodPressure': [BloodPressure_value],'SkinThickness':[SkinThickness_value], 'Insulin': [Insulin_value],
                            'BMI':[BMI_value],'DiabetesPedigreeFunction':[DiabetesPedigreeFunction_value],'Age':[Age_value]} ,index = [0])

            df["Pregnancies"] = pd.to_numeric(df["Pregnancies"], errors='coerce')
            df["Glucose"] = pd.to_numeric(df["Glucose"], errors='coerce')
            df["BloodPressure"] = pd.to_numeric(df["BloodPressure"], errors='coerce')
            df["SkinThickness"] = pd.to_numeric(df["SkinThickness"], errors='coerce')
            df["Insulin"] = pd.to_numeric(df["Insulin"], errors='coerce')
            df["DiabetesPedigreeFunction"] = pd.to_numeric(df["DiabetesPedigreeFunction"], errors='coerce')
            df["BMI"] = pd.to_numeric(df["BMI"], errors='coerce')
            df["Age"] = pd.to_numeric(df["Age"], errors='coerce')


            col1, col2, col3 = st.columns([2,0.7,2])
            v,v2 = st.columns([2,4.3], vertical_alignment="bottom")
            c.write(" ")
            with col2 :Confirm = st.button('confirm')

            if Confirm :
                
                NewBMI = pd.Series(["Underweight", "Normal", "Overweight", "Obesity1", "Obesity2","Obesity3"],dtype="category")
                
                df['NewBMI'] = NewBMI
                df.loc[df["BMI"] < 18.5, "NewBMI"] = NewBMI[0]  # Underweight
                df.loc[(df["BMI"] >= 18.5) & (df["BMI"] <= 24.9), "NewBMI"] = NewBMI[1]  # Normal
                df.loc[(df["BMI"] > 24.9) & (df["BMI"] <= 29.9), "NewBMI"] = NewBMI[2]  # Overweight
                df.loc[(df["BMI"] > 29.9) & (df["BMI"] <= 34.9), "NewBMI"] = NewBMI[3]  # Obesity 1
                df.loc[(df["BMI"] > 34.9) & (df["BMI"] <= 39.9), "NewBMI"] = NewBMI[4]  # Obesity 2
                df.loc[df["BMI"] > 39.9, "NewBMI"] = NewBMI[5]  # Obesity 3

                # if insulin>=16 & insuline<=166->normal

                def set_insuline(row):
                    if row["Insulin"]>=16 and row["Insulin"]<=166:
                        return "Normal"
                    else:
                        return "Abnormal"

                df = df.assign(catInsulin=df.apply(set_insuline, axis=1))

                df = df.assign(catInsulin=df.apply(set_insuline, axis=1))

                #  Some intervals were determined according to the glucose variable and these were assigned categorical variables.
                NewGlucose = pd.Series(["Low", "Normal", "Overweight", "Secret", "High"], dtype = "category")
                df["NewGlucose"] = NewGlucose
                df.loc[df["Glucose"] <= 70, "NewGlucose"] = NewGlucose[0]
                df.loc[(df["Glucose"] > 70) & (df["Glucose"] <= 99), "NewGlucose"] = NewGlucose[1]
                df.loc[(df["Glucose"] > 99) & (df["Glucose"] <= 126), "NewGlucose"] = NewGlucose[2]
                df.loc[df["Glucose"] > 126 ,"NewGlucose"] = NewGlucose[3]

                from sklearn.preprocessing import LabelEncoder

                # Columns to encode
                columns_to_encode = ["NewBMI", "catInsulin", "NewGlucose"]

                # Initialize LabelEncoder
                label_encoder = LabelEncoder()

                # Apply Label Encoding to each column
                for column in columns_to_encode:
                    df[column] = label_encoder.fit_transform(df[column])
                result = mymodel.predict(df)
                #st.sidebar.write(result)

                if result ==0 :
                    v2.subheader("The patient is clear")
                    i,b =st.columns([2,20])
                    b.image(r'C:\Users\MF\Downloads\360_F_111755682_lL0qdCITRiPtS7Ytmr8LGydLd28nk9xM.jpg')

            # Print the result
                    
                    
                else :
                    st.write('The patient has desease')
                    st.image(r"C:\Users\MF\Downloads\images (1).jpeg")

                    
                

            #st.write(f"_________________________ {type(Age_value)}")
            #print(df)



                
