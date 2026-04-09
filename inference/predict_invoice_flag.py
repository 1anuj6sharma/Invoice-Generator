# # it for invoice_flag


# ## inferencing means that how model works on the test data , how trained model predicts on the data 
# #  This file loads the model

# import joblib
# import pandas as pd

# MODEL_PATH = "models/predict_flag_invoice.pkl"

# def load_model(model_path:str = MODEL_PATH):
#     """
#     Load trained freight cost prediction model.
#     """
#     with open(model_path, "rb") as f:
#         model = joblib.load(f)

#     return model


# def predict_invoice_flag(input_data):
#     """
#     Predict invoice flag for new vendor invoices.

#     Parameters
#     ---------
#     input_data : dict

#     Returns
#     ---------
#     pd.DataFrame with predicted flag
#     """
#     model = load_model()
#     input_df = pd.DataFrame(input_data)
#     input_df['Predicted_Flag'] = model.predict(input_df).round()
#     return input_df

# if __name__  == "__main__":

#     # Example inference run ( local testing)
#     sample_data = {
#         "Dollars": [18500,9000,3000,200]
#     }
#     prediction = predict_invoice_flag(sample_data)
#     print(prediction)


# inferencing = using trained model on new/unseen data

import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"


def load_model(model_path: str = MODEL_PATH):
    """
    Load trained invoice flag prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.

    Parameters
    ---------
    input_data : dict

    Returns
    ---------
    pd.DataFrame with predicted flag
    """
    model = load_model()

    # Convert input to DataFrame
    input_df = pd.DataFrame(input_data)

    # Predict
    input_df["Predicted_Flag"] = model.predict(input_df.values).round()

    return input_df


if __name__ == "__main__":

    # ✅ Correct sample data (matches training FEATURES exactly)
    sample_data = {
        "invoice_quantity": [50, 100, 200, 30],
        "invoice_dollars": [352.95, 1200.50, 5000.0, 150.0],
        "Freight": [1.73, 5.2, 10.5, 0.8],
        "total_item_quantity": [162, 300, 800, 100],
        "total_item_dollars": [2476.0, 5000.0, 12000.0, 900.0]
    }

    prediction = predict_invoice_flag(sample_data)
    print(prediction)
