# 🏠 House Price Prediction – FastAPI Backend

## 📌 Project Overview

This project is a Machine Learning-based House Price Prediction API developed using Python, Scikit-learn and FastAPI.

The application predicts house prices based on property details such as area, number of bedrooms, bathrooms, property age, location, property type and parking availability.

The trained Machine Learning model is integrated with FastAPI and deployed on Render, making predictions accessible through a REST API.

## 🎯 Project Objectives

- Build a Machine Learning model for house price prediction.
- Develop a REST API using FastAPI.
- Accept house details as JSON input.
- Generate predictions using a trained ML model.
- Deploy the API online using Render.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest Regressor
- Joblib
- FastAPI
- Pydantic
- Uvicorn
- GitHub
- Render

## 📊 Input Features

| Feature | Description |
|---|---|
| area_sqft | Property area in square feet |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| property_age_years | Age of the property |
| location | Property location |
| property_type | Type of property |
| parking | Parking availability |

## ⚙️ Project Structure

```text
House-Price-Prediction/
│
├── main.py
├── model.py
├── house_price_model.joblib
├── house_price_prediction.ipynb
├── house_price_sample_dataset.csv
├── requirements.txt
└── .gitignore
```

## 🚀 Installation and Setup

Clone the repository:

```bash
git clone https://github.com/lathikagaddam/House_price_prediction_deployemnent.git
```

Navigate to the project folder:

```bash
cd House_price_prediction_deployemnent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

## 🔗 API Endpoints

**Base URL:**

https://house-price-prediction-pa9n.onrender.com

**Available endpoints:**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/predict` | Predict house price |
| GET | `/docs` | Interactive Swagger documentation |

## 🧪 Sample API Request

```json
{
  "area_sqft": 1534,
  "bedrooms": 5,
  "bathrooms": 3,
  "property_age_years": 20,
  "location": "Hyderabad",
  "property_type": "Apartment",
  "parking": "Yes"
}
```

## 📤 Sample API Response

```json
{
  "predicted_price": 0000000.00
}
```

The actual predicted value depends on the input details.

## ☁️ Deployment

The FastAPI backend is deployed on **Render**.

- Live API: https://house-price-prediction-pa9n.onrender.com
- Swagger Docs: https://house-price-prediction-pa9n.onrender.com/docs

## 🔮 Future Improvements

- Connect a frontend application.
- Improve model performance using real-world datasets.
- Add user input validation and error handling.
- Explore additional regression algorithms.
- Integrate a database for storing prediction history.

## 👩‍💻 Author

**GADDAM LATHIKA**

Aspiring AI Engineer | Machine Learning | Python | FastAPI

---

*Note: This project uses synthetic practice data for demonstrating the Machine Learning and API deployment workflow. Predictions are not intended for real-world property valuation.*
