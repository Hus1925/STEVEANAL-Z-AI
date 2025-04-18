
from utils import calculate_score

if __name__ == "__main__":
    companies = [
        {"name": "TechNova", "revenue": 120, "growth": 0.25, "rd_spending": 15},
        {"name": "DataWave", "revenue": 80, "growth": 0.32, "rd_spending": 12},
        {"name": "NextAI", "revenue": 95, "growth": 0.29, "rd_spending": 18},
    ]

    for company in companies:
        score = calculate_score(company)
        print(f"{company['name']} → Skor: {score:.2f}")
