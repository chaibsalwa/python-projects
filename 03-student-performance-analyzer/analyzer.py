"""
Student Performance Analyzer
Author: Salwa Chaib
Analyzes student data using Python & Pandas
"""

# Sample data (no pandas needed for Shipd demo)
students = [
    {"name": "Ahmed", "math": 85, "physics": 78, "english": 90},
    {"name": "Salwa", "math": 92, "physics": 88, "english": 95},
    {"name": "Fatima", "math": 70, "physics": 65, "english": 80},
    {"name": "Youssef", "math": 60, "physics": 55, "english": 70},
    {"name": "Khadija", "math": 88, "physics": 92, "english": 85},
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["english"]) / 3

def analyze():
    print("📊 Student Performance Analysis\n")
    print(f"{'Name':<10} {'Math':<6} {'Phys':<6} {'Eng':<6} {'Avg':<6} {'Status'}")
    print("-"*50)
    
    for s in students:
        avg = calculate_average(s)
        status = "✅ Pass" if avg >= 60 else "❌ Fail"
        if avg >= 85: status = "🌟 Excellent"
        elif avg >= 70: status = "👍 Good"
        print(f"{s['name']:<10} {s['math']:<6} {s['physics']:<6} {s['english']:<6} {avg:<6.1f} {status}")
    
    # Stats
    avgs = [calculate_average(s) for s in students]
    print("\n📈 Stats:")
    print(f"Class Average: {sum(avgs)/len(avgs):.1f}")
    print(f"Top Student: {max(students, key=calculate_average)['name']} ({max(avgs):.1f})")
    print(f"Pass Rate: {len([a for a in avgs if a >= 60])/len(avgs)*100:.0f}%")

if __name__ == "__main__":
    analyze()
