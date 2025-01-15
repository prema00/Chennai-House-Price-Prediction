from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('linear_model_pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract form inputs
            AREA = request.form['AREA']
            BUILDTYPE = request.form['BUILDTYPE']
            INT_SQFT = float(request.form['INT_SQFT'])
            AGE_OF_BUILDING = float(request.form['AGE_OF_BUILDING'])
            N_BATHROOM = int(request.form['N_BATHROOM'])

            # Encode AREA (5 one-hot encoded features)
            AREA_encoded = [0] * 5
            area_mapping = {'Karapakkam': 0, 'Adyar': 1, 'Velachery': 2, 'Anna Nagar': 3, 'T Nagar': 4}
            if AREA in area_mapping:
                AREA_encoded[area_mapping[AREA]] = 1

            # Encode BUILDTYPE (3 one-hot encoded features)
            BUILDTYPE_encoded = [0] * 3
            buildtype_mapping = {'Commercial': 0, 'Residential': 1, 'Others': 2}
            if BUILDTYPE in buildtype_mapping:
                BUILDTYPE_encoded[buildtype_mapping[BUILDTYPE]] = 1

            # Additional Placeholder Features
            # If the original model has features not included in the form, provide default/placeholder values
            PARK_FACIL = 1  # Example: Assume parking is available by default
            N_BEDROOM = 2  # Example: Default value for the number of bedrooms

            # Construct the full feature vector
            feature_vector = (
                AREA_encoded +  # 5 features for AREA
                BUILDTYPE_encoded +  # 3 features for BUILDTYPE
                [INT_SQFT, AGE_OF_BUILDING, N_BATHROOM, N_BEDROOM, PARK_FACIL]  # Remaining numerical features
            )

            # Convert the list to a numpy array
            input_data = np.array([feature_vector])

            # Check if feature vector matches expected size
            if input_data.shape[1] != 13:
                raise ValueError(f"Feature vector has {input_data.shape[1]} features; 13 features are expected.")

            # Make prediction
            prediction = model.predict(input_data)
            output = round(prediction[0], 2)

            # Display results
            return render_template(
                'index.html',
                pred=f"Predicted House Price in {AREA} ({BUILDTYPE}): ₹{output}"
            )

        except Exception as e:
            return render_template('index.html', pred=f"Error: {e}")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
