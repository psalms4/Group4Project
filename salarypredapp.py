#Loading streamlit library necessary for web application creation 
import streamlit as st
#Loading numpy library used for numerical operations
import numpy as np
#Loading datetime library necessary for handling date and time  
import datetime
#Loading sklearn library for supervised machine learnig (Regression)
import sklearn
#Display the message
print("Scikit learn has been imported successfully")
#Loading panda necessary for data analysis and manipulation
import pandas as pd
#Giving the app a title
st.title("Title: Salary Predictor App")
#The introductory message
st.write("This is my first web app.")
#Data Collection of user
#Text to input first and last name
first_name=st.text_input("First Name")
last_name=st.text_input("Last Name")
#Dropdown to select gender
gender=st.selectbox("Gender",["Male", "Female"])
#Number input for age
age=st.number_input("Your Age", 0, 100, 30, 1)
#Date input for date of birth
dob=st.date_input("Your Birthday",
                  min_value=datetime.date(1900, 1, 1),
                  max_value=datetime.date.today()
                  )
#Radio to select Marital status
marital_status=st.radio("Marital Status",["Single", "Married"])
#Slider to input years of experience
experience=st.slider("Years of Experience", 0, 40)
#Creating a submission button
if st.button("Submit", key="submit_button"):
    st.success("Here is your bio data:")
#line of codes to display user input values on the web app
st.write(f"Name:{first_name}{last_name}")
st.write(f"Gender:{gender}")
st.write(f"Age:{age}")
st.write(f"Date of Birth:{dob}")
st.write(f"Marital Status:{marital_status}")
st.write(f"Years of Experience:{experience}")
#Creating a dictionary with all the user's input
if st.button("Submit"):
    user_data={"First Name":first_name,
               "Last Name":last_name,
               "Gender":gender,
               "Age":age,
               "Date Of Birth":dob,
               "Marital Status":marital_status,
               "Years of Experience":experience
               }
    #Changing the dictonary to pandas dataframe
    df=pd.DataFrame([user_data])
    #saving the data entry to the csv file
    df.to_csv("user_data.csv", mode="a",header=False, index=False)
    #Displaying a success message on the app
    st.success("Your data has been saved")
 #Importing LinearRegression from sklearn for model training    
from sklearn.linear_model import LinearRegression
#Manually adding data  
data={
    "Years of Experience":[1,3,5,7,10,12,15,18,20],
    "Salary":[30000,45000,60000,75000,90000,105000,120000,135000,150000]

}
#Creating a dataframe from the dictionary data
df=pd.DataFrame(data)
#Creating an instance of the LinearRegression model
model=LinearRegression()
x=df[["Years of Experience"]]
y=df[["Salary"]]
model.fit(x,y)
#Statement to use the trained model to predict salary
if st.button("Predict Salary", key="salary_button"):
    predicted_salary=model.predict(np.array([[experience]]))[0]
    st.success(f"Estimated Salary: ${predicted_salary[0]:,.2f}")