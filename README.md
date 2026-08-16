📧 Intelligent Email Spam Detection Using Machine Learning and Deep Learning Approaches

CCS3356 — Natural Language Processing | Group Assignment

A complete NLP pipeline that classifies emails as Spam or Ham (legitimate), built and evaluated across six independent models — three classical Machine Learning and three Deep Learning — and deployed as a working interactive application.

👥 Team — Group 42
Member	                Student ID            	Models
Sisal Tilshan	        Cit-24-01-0374	   Naive Bayes (ML) + LSTM (DL)
Kavindu Thidakshana	  Cit-24-01-0589	   SVM (ML) + CNN (DL)
Lasitha Weerasooriya	Cit-24-01-0528	   XGBoost (ML) + DistilBERT (DL)

🎯 Problem Statement

Spam and phishing emails expose users to fraud, wasted time, and security risks as email volume continues to grow. Manual filtering doesn't scale. This project applies Natural Language Processing to automatically classify email content as spam or legitimate, improving inbox security and productivity.

📊 Dataset

Source: SMS Spam Collection Dataset — a public, well-established academic dataset.
	
Total messages	5,572
Ham	4,825 (~87%)
Spam	747 (~13%)
Classes	2 (spam, ham)

Adopted to ensure a complete, fully-evaluated end-to-end pipeline within the project timeline.

🧠 Model Summary & Results

All six models were evaluated on the same held-out test split using Accuracy and F1-Score.

Model	      Type	    Accuracy	    F1-Score
SVM 🏆	     ML	        0.98	        0.94
CNN	         DL	        0.98	        0.93
DistilBERT	 DL	        0.97	        0.91
LSTM	       DL	        0.97	        0.90
Naive Bayes	 ML	        0.96	        0.85
XGBoost	     ML	        0.94	        0.77

Best model: SVM (linear kernel, TF-IDF features) — selected for the highest F1-score, low computational cost, and stable decision boundaries.

🗂️ Project Structure
NLP_Group_42/
├── data/              # Dataset (spam_dataset.csv)
├── notebooks/         # One notebook per member's models
├── models/            # Saved model artifacts
├── src/                 # Final application source (app.py)
├── reports/            # Final report
├── screenshots/     # Evaluation & evidence screenshots
├── requirements.txt
└── README.md
⚙️ Setup
bash
git clone https://github.com/Sisaltilshan/NLP_Group_42.git
cd NLP_Group_42
pip install -r requirements.txt
▶️ How to Run

Model notebooks: open any notebook in notebooks/ in Google Colab or Jupyter to view preprocessing, training, and evaluation for that member's models.

Final application:

bash
cd src
streamlit run app.py

Paste any email text into the interface and click Analyze to get an instant Spam / Ham classification.

🧪 NLP Pipeline
Data Collection — load labeled dataset
Preprocessing — lowercasing, HTML/URL removal, text cleaning
Feature Extraction — TF-IDF, handcrafted features, or embeddings depending on model
Model Training — six models trained independently
Evaluation — Accuracy, Precision, Recall, F1-Score, Confusion Matrix
⚖️ Ethical Considerations

This system may reflect dataset bias, produce false positives (legitimate emails blocked) or false negatives (spam missed), and should be used as a decision-support tool rather than a fully autonomous filter. Full discussion in the Final Report.

🔗 Links
Final Report: reports/
Live Application: run locally via src/app.py

Developed for CCS3356 — Natural Language Processing, Sri Lanka Technology Campus.
