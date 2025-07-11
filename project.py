
pairs = {

    ("ciprofloxacin", "milk"): "Avoid milk and dairy. It reduces drug absorption.",
    ("ciprofloxacin", "yogurt"): "Avoid yogurt. It interferes with absorption.",
    ("ciprofloxacin", "calcium supplements"): "Avoid calcium. It binds and reduces effectiveness.",
    ("ciprofloxacin", "antacids"): "Antacids reduce absorption. Take 2 hours apart.",

    ("warfarin", "spinach"): "High vitamin K reduces drug effectiveness.",
    ("warfarin", "broccoli"): "Rich in vitamin K. Reduces anticoagulant effect.",
    ("warfarin", "kale"): "Avoid kale. It interferes with drug effect.",
    ("warfarin", "green tea"): "Contains vitamin K. May reduce warfarin's effectiveness.",
    ("warfarin", "liver"): "High in vitamin K. Affects anticoagulant activity.",

    ("metformin", "alcohol"): "Increases risk of lactic acidosis. Avoid alcohol.",
    ("metformin", "high-fat meal"): "Delays absorption. Take with regular meal instead.",

    ("levothyroxine", "soy"): "Soy interferes with absorption.",
    ("levothyroxine", "fiber"): "High-fiber foods reduce absorption.",
    ("levothyroxine", "coffee"): "Coffee may reduce absorption. Wait 30–60 minutes.",
    ("levothyroxine", "calcium"): "Avoid calcium within 4 hours. Reduces absorption.",
    ("levothyroxine", "iron supplements"): "Iron interferes with absorption. Take separately.",

    ("atorvastatin", "grapefruit"): "Grapefruit increases drug level. Risk of side effects.",
    ("simvastatin", "grapefruit"): "Avoid grapefruit. Risk of liver and muscle damage.",
    ("lovastatin", "grapefruit"): "Increases drug levels. Risk of side effects.",
    ("pravastatin", "grapefruit"): "No significant interaction. Safe to take.",

    ("lisinopril", "banana"): "Bananas are high in potassium. Risk of hyperkalemia.",
    ("lisinopril", "orange juice"): "High in potassium. May increase levels dangerously.",
    ("lisinopril", "salt substitutes"): "Contain potassium. May cause hyperkalemia.",

    ("tetracycline", "milk"): "Dairy interferes with absorption. Avoid milk.",
    ("tetracycline", "cheese"): "Avoid cheese. It can bind with the drug.",
    ("tetracycline", "iron supplements"): "Avoid iron. Reduces absorption.",

    ("iron supplements", "tea"): "Avoid tea. It inhibits iron absorption.",
    ("iron supplements", "coffee"): "Coffee reduces iron absorption.",
    ("iron supplements", "milk"): "Calcium competes with iron. Reduces absorption.",
    ("iron supplements", "eggs"): "Eggs can inhibit iron absorption.",
    ("iron supplements", "bran"): "Bran contains phytates. Reduces iron absorption.",

    ("digoxin", "fiber"): "High-fiber meals reduce drug absorption.",
    ("digoxin", "wheat bran"): "Reduces absorption. Avoid concurrent use.",

    ("aspirin", "alcohol"): "Increases risk of stomach bleeding. Avoid alcohol.",
    ("aspirin", "caffeine"): "May increase side effects like anxiety or dizziness.",
    ("aspirin", "ginger"): "May increase bleeding risk.",

    ("ibuprofen", "alcohol"): "Increases risk of stomach ulcers and bleeding.",
    ("ibuprofen", "caffeine"): "Can increase stomach irritation.",

    ("paracetamol", "alcohol"): "Liver toxicity risk. Avoid alcohol.",

    ("diazepam", "alcohol"): "Increased drowsiness and dizziness. Avoid alcohol.",
    ("lorazepam", "grapefruit"): "May increase sedative effects.",

    ("clopidogrel", "grapefruit"): "May reduce drug activation. Avoid grapefruit.",
    ("nifedipine", "grapefruit"): "Increases blood levels. Risk of hypotension.",

    ("theophylline", "caffeine"): "Additive stimulation. Avoid excessive caffeine.",
    ("theophylline", "high-fat meal"): "Increases absorption. Monitor levels.",

    ("phenelzine", "cheese"): "Contains tyramine. Risk of hypertensive crisis.",
    ("phenelzine", "salami"): "Tyramine-rich food. Avoid to prevent high BP.",
    ("phenelzine", "soy sauce"): "High in tyramine. Dangerous interaction.",

    ("cyclosporine", "grapefruit"): "Increases drug level. Risk of kidney toxicity.",
    ("tacrolimus", "grapefruit"): "Increases drug level. Risk of toxicity.",

    ("amiodarone", "grapefruit"): "Increases drug level. Risk of serious heart effects.",

    ("fexofenadine", "grapefruit"): "Avoid grapefruit. Reduces drug absorption.",
    ("fexofenadine", "apple juice"): "Avoid apple juice. Decreases drug effect.",
    ("fexofenadine", "orange juice"): "Avoid orange juice. Lowers absorption.",

    ("carbamazepine", "grapefruit"): "Increases side effects. Avoid grapefruit.",
    ("phenytoin", "alcohol"): "Alters drug levels. Avoid alcohol.",
    ("phenytoin", "folic acid"): "May reduce drug level. Monitor closely.",

    ("sildenafil", "grapefruit"): "Increases blood level. May enhance effects.",
    ("sildenafil", "fatty meal"): "Delays onset. Avoid high-fat meals.",

    ("doxycycline", "milk"): "Milk reduces absorption. Avoid dairy.",
    ("doxycycline", "iron"): "Iron interferes with absorption.",

    ("isocarboxazid", "aged cheese"): "Tyramine reaction. Risk of hypertensive crisis.",
    ("isocarboxazid", "red wine"): "High tyramine content. Dangerous interaction.",

    ("linezolid", "cheese"): "Contains tyramine. May increase BP.",
    ("linezolid", "soy products"): "Tyramine risk. Avoid fermented soy.",

    ("selegiline", "beer"): "Tyramine reaction. Risk of high blood pressure.",

    ("methotrexate", "alcohol"): "Increases liver toxicity. Avoid alcohol.",
    ("methotrexate", "folic acid"): "Reduces side effects but may decrease efficacy.",

    ("disulfiram", "alcohol"): "Severe reaction. Nausea, vomiting, palpitations.",

    ("spironolactone", "banana"): "High potassium. Risk of hyperkalemia.",
    ("spironolactone", "orange"): "Avoid. Rich in potassium.",

    ("zidovudine", "fatty meal"): "Slows absorption. Take on empty stomach.",

    ("rifampin", "food"): "Food decreases absorption. Take on empty stomach.",

    ("alendronate", "coffee"): "Avoid for at least 30 mins. Reduces absorption.",
    ("alendronate", "orange juice"): "Avoid. Reduces drug absorption.",

    ("bisacodyl", "milk"): "Avoid milk before use. Reduces effectiveness.",

    ("levodopa", "protein"): "High-protein foods compete with absorption.",
    ("levodopa", "iron"): "Iron reduces absorption. Space out dosing.",

    ("sotalol", "milk"): "May reduce absorption. Take on empty stomach.",

    ("esomeprazole", "food"): "Take 1 hour before meals for best effect.",

    ("glipizide", "alcohol"): "Can cause low blood sugar. Avoid alcohol.",

    ("meloxicam", "alcohol"): "Increases GI bleeding risk.",

    ("ketoconazole", "cola"): "Acidic drink enhances absorption.",
    ("ketoconazole", "antacids"): "Antacids reduce absorption. Avoid together.",

    ("allopurinol", "alcohol"): "Alcohol may trigger gout attacks.",

    ("captopril", "food"): "Food reduces absorption. Take on empty stomach.",

    ("nateglinide", "grapefruit"): "Increases drug concentration.",

    ("ranitidine", "smoking"): "Smoking reduces effectiveness.",

    ("methylphenidate", "alcohol"): "Alcohol increases side effects. Avoid combination.",

    ("rosuvastatin", "antacids"): "Antacids reduce blood levels. Space out dosing.",

    ("tamoxifen", "soy"): "Soy may affect estrogen balance. Avoid excess intake."
}

drug_set = set()
food_set = set()
for drug, food in pairs.keys():
                drug_set.add(drug.lower().strip())
                food_set.add(food.lower().strip())

print("🩺 Drug-Food Interaction Checker")
print("Type 'stop' to exit.\n")

while True:
                drug = input("Enter drug name: ").lower().strip()
                if drug == "stop":
                    break
                if drug not in drug_set:
                    print(f"❌ '{drug}' is not a known drug.")
                    continue
                print(f"Drug: {drug.title()}")

                food = input("Enter food item: ").lower().strip()
                if food == "stop":
                    break
                if food not in food_set:
                    print(f"❌ '{food}' is not a known food item.")
                    continue
                print(f"Food: {food.title()}")

                x = (drug, food)


                if x in pairs:
                    print(f"\n⚠️ {drug.title()} + {food.title()} Interaction: {pairs[x]}")

                else:
                    print(f"\nℹ️ No known interaction found between {drug.title()} and {food.title()}.")
