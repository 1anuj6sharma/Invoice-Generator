# ## inferencing means that how model works on the test data , how trained model predicts on the data 
# #  This file loads the model

# import joblib
# import pandas as pd

# MODEL_PATH = "models/predict_freight_model.pkl"

# def load_model(model_path:str = MODEL_PATH):
#     """
#     Load trained freight cost prediction model.
#     """
#     with open(model_path, "rb") as f:
#         model = joblib.load(f)

#     return model


# def predict_freight_cost(input_data):
#     """
#     Predict freight cost for new vendor invoices.

#     Parameters
#     ---------
#     input_data : dict

#     Returns
#     ---------
#     pd.DataFrame with predicted freight cost
#     """
#     model = load_model()
#     input_df = pd.DataFrame(input_data)
#     input_df['Predicted_Freight'] = model.predict(input_df).round()
#     return input_df

# if __name__  == "__main__":

#     # Example inference run ( local testing)
#     sample_data = {
#         "Dollars": [18500,9000,3000,200]
#     }
#     prediction = predict_freight_cost(sample_data)
#     print(prediction)



# inferencing = using trained model on new/unseen data

import joblib
import pandas as pd

MODEL_PATH = "models/predict_freight_model.pkl"


def load_model(model_path: str = MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.

    Parameters
    ---------
    input_data : dict

    Returns
    ---------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()

    # Convert input to DataFrame
    input_df = pd.DataFrame(input_data)

    # ✅ IMPORTANT: enforce correct columns (same as training)
    expected_cols = model.feature_names_in_
    input_df = input_df[expected_cols]

    # Predict
    input_df["Predicted_Freight"] = model.predict(input_df).round(2)

    return input_df


if __name__ == "__main__":

    # ✅ Example test input (must match training features)
    sample_data = {
        "Quantity": [1200, 800, 300, 50],
        "Dollars": [18500, 9000, 3000, 200]
    }

    prediction = predict_freight_cost(sample_data)
    print(prediction)
