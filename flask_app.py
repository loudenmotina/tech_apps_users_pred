from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
app = Flask(__name__)

# Load your trained RandomForest model
# You should replace 'your_model.pkl' with the actual filename of your trained model
model = pickle.load(open("model.pkl", "rb"))  # Load your trained model here

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        data = {
            'opted_in_to_mailing_list':int(request.form['opted_in_to_mailing_list']),
            'enabled_for_marketing_drip':int(request.form['enabled_for_marketing_drip']),
            'year':int(request.form['year']),
            'month':int(request.form['month']),
            'period_usage':int(request.form['period_usage']),
            'GUEST_INVITE':int(request.form['GUEST_INVITE']),
            'ORG_INVITE':int(request.form['ORG_INVITE']), 
            'PERSONAL_PROJECTS':int(request.form['PERSONAL_PROJECTS']), 
            'SIGNUP':int(request.form['SIGNUP']), 
            'SIGNUP_GOOGLE_AUTH':int(request.form['SIGNUP_GOOGLE_AUTH']),
            'category_of_invited_user':int(request.form['category_of_invited_user']),
            'category_of_group_org':int(request.form['category_of_group_org'])
            
            # Add more features as needed
        }
        input_data = pd.DataFrame(data, index=[0])

        # Make predictions using the loaded model
        prediction = model.predict(input_data)

       # return render_template('home.html', prediction=f'Predicted Class: {prediction[0]}')
    #except Exception as e:
        #return render_template('home.html', prediction=f'Error: {str(e)}')
        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="App user is . {}".format(output))


    except Exception as e:
        return render_template('home.html', prediction=f'Error: {str(e)}')
   
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8000)


