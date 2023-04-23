
# Zero-Shot-Fake-News-Detection

In recent years, the issue of fake news has become increasingly prevalent in our society. With the widespread use of social media and the internet, false information can spread rapidly, often causing harm and confusion. The ability to detect and combat fake news is critical in ensuring that the public is well-informed and can make informed decisions. With the advancements in machine learning and natural language processing, automated fake news detection systems have become a promising solution.

The objective of our project is to create a tool for checking whether news articles are trustworthy or not.
The tool will have to perform an evaluation of the facts, events, and related information within a news article.

We acheive this in a zero shot manner by using question answer generation models and web scraping of reliable of news article.

#### Dataset Sources:

WELFake dataset which is used to train our models can be accessed from here: https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification

Datasets which are used to test our models can be accessed from here: <br>
- https://www.kaggle.com/datasets/jruvika/fake-news-detection
- https://www.kaggle.com/datasets/faisalmabood/fake-and-true-news-dataset?select=True.csv </br>

# Instructions for running

### Accessing the website:
Url: https://asmita-mukherjee-irprojectwebpage-interface-h6k2oz.streamlit.app/

### Running the Code:

#### Create conda env:
conda create --name <env_name> --file requirements.txt

conda activate <env_name>

#### Run the python file

cd "18_FinalReview"

python run.py
