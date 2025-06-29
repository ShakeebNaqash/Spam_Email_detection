# 📧 Spam Email Detection using TF-IDF and Naive Bayes

This project is a simple yet effective machine learning application to detect **spam** and **ham (legitimate)** emails using **TF-IDF vectorization** and a **Multinomial Naive Bayes** classifier. It also includes a **Streamlit web app** for interactive testing.

---

## 🔍 Project Highlights

- 📄 Data Preprocessing
- ✍️ TF-IDF Feature Extraction
- 🤖 Naive Bayes Classification
- 📊 Model Evaluation
- 🌐 Interactive Streamlit App


📂 Dataset
This project uses the 190K Spam-Ham Email Dataset from Kaggle for training and evaluation.

You can download the dataset directly from Kaggle using the link above.


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
