# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:32:32 2025

@author: admin
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open("./traained_model.sav",'rb'))
def tumor_prediction(input_data):
    
    inputdatatonumpy=np.asarray(input_data,dtype=float)
    inputdatareshaped=inputdatatonumpy.reshape(1,-1)
    prediction=loaded_model.predict(inputdatareshaped)
    
    if(prediction):
        return 'Benign Tumor'
    else:
      return 'Malignant Tumor'
    #return prediction[0]
    
def main():
  
    st.title('Breast Cancer Detector')
    radius_mean=st.text_input("Enter radius")
    texture_mean=st.text_input("Enter texture_mean")
    perimeter_mean=st.text_input("Enter perimetermean")
    area_mean=st.text_input("Enter areamean")
    smoothness_mean=st.text_input("Enter smootnessmean")
    compactness_mean=st.text_input("Enter compactnessmean")
    concavity_mean=st.text_input("Enter concavitymean")
    concave_points_mean=st.text_input("Enter concavepointsmean")
    symmetry_mean=st.text_input("Enter symmetrymean")
    fractal_dimension_mean=st.text_input("Enter fractaldimensionmean")
    radius_se=st.text_input("Enter radiusse")
    texture_se=st.text_input("Enter texturese")
    perimeter_se=st.text_input("Enter perimeterse")
    area_se=st.text_input("Enter arease")
    smoothness_se=st.text_input("Enter smoothnesse")
    compactness_se=st.text_input("Enter compactnesse")
    concavity_se=st.text_input("Enter concavityse")
    conacave_points_se=st.text_input("Enter concavepointsse")
    symmetry_se=st.text_input("Enter symmetryse")
    fractal_dimension_se=st.text_input("Enter fractaldimensionse")
    radius_worst=st.text_input("Enter radiusworst")
    texture_worst=st.text_input("Enter textureworst")
    perimeter_worst=st.text_input("Enter perimeterworst")
    area_worst=st.text_input("Enter areaworst")
    smoothness_worst=st.text_input("Enter  smootnessworst")
    compactness_worst=st.text_input("Enter compactnessworst")
    concavity_worst=st.text_input("Enter concavityworst")
    concave_points_worst=st.text_input("Enter concavepointsworst")
    symmetry_worst=st.text_input("Enter symmetryworst")
    fractal_dimension_worst=st.text_input("Enter fractaldimesnion worst")
    result_placeholder=st.empty()
    #code for prediction
    diagnosis=''
    
    if st.button('The tumor is'):
        try:
          diagnosis=tumor_prediction([radius_mean,texture_mean,perimeter_mean,area_mean,
                                    smoothness_mean,compactness_mean,concavity_mean,
                                    concave_points_mean,symmetry_mean,fractal_dimension_mean
                                    ,radius_se,texture_se,perimeter_se,area_se,smoothness_se,
                                    compactness_se,concavity_se,conacave_points_se,symmetry_se,
                                    fractal_dimension_se,radius_worst,texture_worst,perimeter_worst
                                    ,area_worst,smoothness_worst,compactness_worst,concavity_worst,
                                    concave_points_worst,symmetry_worst,fractal_dimension_worst])
          if diagnosis == 1:
               result_placeholder.markdown(
                   f"<div style='color: red; font-size: 24px;'>The tumor is <strong>Benign</strong></div>",
                   unsafe_allow_html=True
               )
          else:
               result_placeholder.markdown(
                   f"<div style='color: green; font-size: 24px;'>The tumor is <strong>Malignant</strong></div>",
                   unsafe_allow_html=True
               )
        except ValueError:
             st.error("Please enter valid numeric values for all fields.")

        st.success(diagnosis)
if __name__=='__main__':
    main()