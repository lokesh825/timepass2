import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_forest(sl,sw,pl,pw):
    input=np.array([[sl,sw,pl,pw]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    sl = st.text_input("Sepal Length","Type Here")
    sw = st.text_input("Sepal Width","Type Here")
    pl = st.text_input("Petal Length","Type Here")
    pw = st.text_input("Petal Width","Type Here")

    if st.button("Predict"):
        output=predict_forest(sl,sw,pl,pw)
        st.success('Predicted Class is {}'.format(output))


if __name__=='__main__':
    main()