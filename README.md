# ML House Price Prediction
This is a simple machine learning project for predicting the price of a house based on various features, such as house size, number of rooms, garden, and orientation. The project uses scikit-learn to train a linear regression model and streamlit to create a web interface that allows users to input their house details and receive a predicted value.

![image](https://user-images.githubusercontent.com/101446104/227769436-ad5df042-0d6b-4f03-a732-bb989e21198f.png)


## Usage
To use this project, follow the steps below:

1. Clone this repository to your local machine.

2. Install the necessary dependencies using pip install -r requirements.txt.

3. Ensure that you have the necessary data. This project assumes that you have a CSV file containing house prices and their features.

4. Train the model using the model.py script by running `python3.9 model.py`. The script loads the CSV file, preprocesses the data, trains the model, and saves the model using joblib. You can modify the script to include a test for the model.

5. Run the streamlit.py script by running `streamlit run streamlit.py` to launch the web interface. The script loads the trained model, takes user input, and outputs the predicted house value.



## Requirements
This project requires the following dependencies:

- pandas
- scikit-learn
- streamlit
- joblib

You can install these dependencies by running pip install -r requirements.txt.

## Credits
This project is based on the "Introduction to Machine Learning with Python" course at the Digital Learning Hub. The code for the linear regression model and web interface is adapted from the course materials.
