
def calculate_score(company):
    # Basit bir skor algoritması: gelir + büyüme*100 + Ar-Ge harcaması
    revenue = company.get("revenue", 0)
    growth = company.get("growth", 0)
    rd_spending = company.get("rd_spending", 0)
    return revenue + (growth * 100) + rd_spending
