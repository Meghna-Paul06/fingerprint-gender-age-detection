# fingerprint-gender-age-detection
Gender and Age Group detection from an individual fingerprint using Machine Learning

** This work is licensed. Please don't use anything for any personal or professional approach. **

The aim of this project is to study and analyse the human fingerprint texture to determine their age and gender using a machine learning approach. 

The number of ridge terminals, the bifurcation points and the core point of the fingerprint images are considered and then the Euclidean distance between these features are calculated so as to classify the age and gender groups. 

Another key feature for this classification is the slope of the line joining the core point and the ridge terminal point and the slope of the line joining the core point and bifurcation point. Finally we train the classifier to group the data into various classes of gender and age accordingly.

This is for the first time that the classification of gender and age from a fingerprint is being done considering the Euclidean distances from core to ridge terminal and core to bifurcation point, the slope of the line joining the core point and the ridge terminal point and the slope of the line joining the core point and the bifurcation point. Our main objective is to use these simple features for the classification purpose.

'main.py' file calculates the necessary features.
'knn.py' file trains the classifier and feeds the features into the classifier. To keep a simple approach, K-Nearest Neighbour(KNN) algorithm is used here.
'gui.py' file provides an interactive user interface for gender and age detection.
