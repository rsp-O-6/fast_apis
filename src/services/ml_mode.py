import fitz # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    """PDF bytes se text nikalne ka function."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_job_recommendations_from_bytes(resume_bytes: bytes):
    """Resume ke bytes ke basis par jobs recommend karta hai."""
    
    # Dummy Job Descriptions (DB se aayenge)
    job_descriptions = [
        "We are looking for a Python developer with experience in FastAPI and machine learning.",
        "Angular developer needed for a frontend project using TypeScript and RxJS.",
        "Full stack developer with skills in Python, Angular, and PostgreSQL.",
        "Data Scientist with expertise in NLP, scikit-learn, and model deployment."
    ]
    job_titles = ["Python ML Engineer", "Frontend Angular Dev", "Full Stack Engineer", "Data Scientist"]

    # Resume bytes se text extract karna
    resume_text = extract_text_from_pdf_bytes(resume_bytes)
    
    # Baaki ka logic (TF-IDF, Cosine Similarity) same rahega
    documents = [resume_text] + job_descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    
    scores = list(enumerate(cosine_sim[0]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    recommendations = []
    for i, score in sorted_scores:
        if score > 0.1:
            recommendations.append({
                "job_title": job_titles[i],
                "match_score": round(score, 2)
            })
            
    return recommendations