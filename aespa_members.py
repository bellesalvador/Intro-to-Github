# Assignment #3: Introduction to GitHub
# aespa_members.py
# A simple Python program used for GitHub practice

aespa = {
    "Karina": "Leader, Main Dancer, Lead Rapper, Sub Vocalist",
    "Giselle": "Main Rapper, Sub Vocalist",
    "Winter": "Lead Vocalist, Lead Dancer, Visual",
    "NingNing": "Main Vocalist, Maknae"
}

def show_members():
    print("aespa members and roles\n")
    for name, role in aespa.items():
        print(f"{name}: {role}")

# Run the function
if __name__ == "__main__":
    show_members()
