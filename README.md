# 📧 Spam Email Detection using TF-IDF and Naive Bayes

This project is a simple yet effective machine learning application to detect **spam** and **ham (legitimate)** emails using **TF-IDF vectorization** and a **Multinomial Naive Bayes** classifier. It also includes a **Streamlit web app** for interactive testing.

---

## 🔍 Project Highlights

- 📄 Data Preprocessing
- ✍️ TF-IDF Feature Extraction
- 🤖 Naive Bayes Classification
- 📊 Model Evaluation
- 🌐 Interactive Streamlit App


## 📊 Dataset

We used the [190K Spam-Ham Email Dataset](https://www.kaggle.com/datasets/meruvulikith/190k-spam-ham-email-dataset-for-classification) available on Kaggle.

This dataset contains:
- 190,000 labeled email messages
- Two classes: `spam` and `ham`
- Ideal for training spam detection models

➡️ Download it directly from Kaggle.


## 🚀 How to Run

  🔧 Step 1: Install Requirements
  
   `pip install -r requirements.txt`
   
   Or install individually
   
   `pip install streamlit pandas scikit-learn joblib`


   ▶️ Step 2: Train Model (Optional)
   
   Already trained models are provided in the model/ folder.
   To retrain, use the provided Jupyter notebook or Python script.

   🖥️ Step 3: Run the Streamlit App
  
   `streamlit run app.py`
