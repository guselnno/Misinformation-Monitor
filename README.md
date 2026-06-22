# Misinformation Monitor

## Projektbeskrivning

Misinformation Monitor är en data-driven applikation som använder maskininlärning för att identifiera potentiell desinformation i nyhetsartiklar. Projektet utvecklades inom ramen för kursen TIG326 och utgår från grand challenge-området **Misinformation**.

## Syfte

Syftet med projektet är att hjälpa användare att bedöma trovärdigheten hos digitala nyhetsartiklar genom att använda en maskininlärningsmodell som klassificerar artiklar som trovärdiga eller potentiellt vilseledande.

## Teknologier

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Streamlit
* Jupyter Notebook

## Dataset

Projektet använder **Fake and Real News Dataset** från Kaggle:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Projektstruktur

* `rapport.ipynb` – Projektrapport och analys
* `app.py` – Streamlit-applikation
* `model.pkl` – Tränad maskininlärningsmodell
* `vectorizer.pkl` – Sparad TF-IDF-vektoriserare
* `Bild_app.png`, `Bild_desinformation.png`, `Bild_trovärdig information.png` – Skärmdumpar av applikationen

## Hur man kör projektet

1. Installera beroenden:

```bash
pip install pandas scikit-learn streamlit
```

2. Starta applikationen:

```bash
streamlit run app.py
```

3. Öppna:

```text
http://localhost:8501
```

## Resultat

Modellen uppnådde en accuracy på **98,64 %** på testdatan och kunde med hög träffsäkerhet skilja mellan falska och riktiga nyhetsartiklar.

## Författare

Grupprojekt inom kursen TIG326 – Design Thinking och Data-driven Innovation.
