import streamlit as st
import pickle
import pandas as pd
mymodel = pickle.load(open(r"C:\Users\MF\Desktop\Streamlit\modelGui.sav",'rb'))


st.title ('Diabetes Prediction Web app')
st.info('Easy Application for Diabetes prediction Desease')
st.sidebar.header('Feature Selection')

Pregnancies_value = st.text_input('Pregnancies')
Glucose_value = st.text_input('Glucose')
BloodPressure_value =st.text_input('BloodPressure')
SkinThickness_value = st.text_input('SkinThickness')
Insulin_value = st.text_input('Insulin')
BMI_value = st.text_input('BMI')
DiabetesPedigreeFunction_value = st.text_input('DiabetesPedigreeFunction')
Age_value = st.text_input('Age')

if Pregnancies_value.isdigit():  # Check if the input is numeric
    Pregnancies_value = float (Pregnancies_value)
if Glucose_value.isdigit():  # Check if the input is numeric
    Glucose_value = float (Glucose_value)
if BloodPressure_value.isdigit():  # Check if the input is numeric
    BloodPressure_value =float (BloodPressure_value)
if SkinThickness_value.isdigit():  # Check if the input is numeric
    SkinThickness_value = float (SkinThickness_value)
if Insulin_value.isdigit():  # Check if the input is numeric
    Insulin_value = float (Insulin_value)
if BMI_value.isdigit():  # Check if the input is numeric
    BMI_value = float (BMI_value)
if DiabetesPedigreeFunction_value.isdigit():  # Check if the input is numeric
    DiabetesPedigreeFunction_value = float (DiabetesPedigreeFunction_value)
if Age_value.isdigit():  # Check if the input is numeric
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



Confirm = st.sidebar.button('confirm')

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
     st.sidebar.write(result)

     if result ==0 :
         st.sidebar.write("The patient is clear")
         st.sidebar.image(r'C:\Users\MF\Downloads\360_F_111755682_lL0qdCITRiPtS7Ytmr8LGydLd28nk9xM.jpg')

# Print the result
         
         st.sidebar.write('The patient has desease')
     else :
         st.siderbar.write('The patient has desease')
         st.sidebar.image(r"C:\Users\MF\Downloads\images (1).jpeg")

         
     

st.write(f"_________________________ {type(Age_value)}")
#print(df)



    
