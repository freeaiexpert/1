import datetime

# --- Knowledge Base ---
# Define rules as a list of dictionaries.
# Each rule has 'conditions' (a set of symptoms) and a 'diagnosis' (potential condition).
# Using sets for conditions allows easy checking if user symptoms contain all required conditions.

knowledge_base = [
    {
        "conditions": {"fever", "cough", "fatigue", "body_aches"},
        "diagnosis": "Possible Influenza (Flu)",
        "advice": "Rest, fluids, consider over-the-counter pain relievers. See a doctor if symptoms are severe or persist."
    },
    {
        "conditions": {"runny_nose", "sneezing", "sore_throat", "mild_cough"},
        "diagnosis": "Possible Common Cold",
        "advice": "Rest, fluids, over-the-counter cold remedies may help symptoms. Usually resolves on its own."
    },
    {
        "conditions": {"severe_sore_throat", "fever", "swollen_tonsils"},
        "diagnosis": "Possible Strep Throat",
        "advice": "Requires a doctor's visit for testing (rapid strep test/throat culture) and potentially antibiotics."
    },
     {
        "conditions": {"fever", "difficulty_breathing", "chest_pain", "persistent_cough"},
        "diagnosis": "Possible Pneumonia / Serious Respiratory Issue",
        "advice": "Seek medical attention urgently. Requires chest X-ray and professional evaluation."
    },
    {
        "conditions": {"sneezing", "itchy_eyes", "runny_nose", "watery_eyes"},
        "diagnosis": "Possible Allergies",
        "advice": "Consider antihistamines. Identify and avoid triggers if possible. Consult a doctor if severe or persistent."
    },
     {
        "conditions": {"headache", "nausea", "sensitivity_to_light"},
        "diagnosis": "Possible Migraine",
        "advice": "Rest in a dark, quiet room. Over-the-counter or prescription migraine medication may be needed. See a doctor for recurring episodes."
    },
    {
        "conditions": {"rash", "itchiness"},
        "diagnosis": "Possible Skin Condition / Allergic Reaction",
        "advice": "Avoid scratching. Over-the-counter creams may help. See a doctor for diagnosis and appropriate treatment, especially if severe or spreading."
    },
    # --- Add more rules as needed ---
]

# --- List of known symptoms (for user interface) ---
# Extract all unique symptoms mentioned in the rules
all_symptoms = set()
for rule in knowledge_base:
    all_symptoms.update(rule["conditions"])

# Sort for consistent display
known_symptoms_list = sorted(list(all_symptoms))

# --- Inference Engine ---
def get_possible_diagnoses(patient_symptoms, rules):
    """
    Applies rules from the knowledge base to the patient's symptoms.
    Uses forward chaining: If all conditions for a rule are met by the patient's symptoms,
    the diagnosis is considered possible.

    Args:
        patient_symptoms (set): A set of symptoms reported by the patient.
        rules (list): The knowledge base (list of rule dictionaries).

    Returns:
        list: A list of dictionaries, each containing a 'diagnosis' and 'advice'
              for rules whose conditions were met.
    """
    possible_diagnoses = []
    for rule in rules:
        # Check if all conditions required by the rule are present in the patient's symptoms
        if rule["conditions"].issubset(patient_symptoms):
            possible_diagnoses.append({
                "diagnosis": rule["diagnosis"],
                "advice": rule["advice"]
            })
    return possible_diagnoses

# --- User Interface ---
def run_expert_system():
    """
    Handles the command-line interaction with the user.
    """
    print("\n--- Simple Medical Symptom Checker (Demonstration) ---")
    print("=======================================================")
    print("DISCLAIMER: Not for actual medical diagnosis. Always consult a doctor.")
    print("Current Date:", datetime.date.today().strftime("%Y-%m-%d")) # Using current date
    print("-------------------------------------------------------")

    print("Please select the symptoms you are experiencing by entering their numbers, separated by commas.")
    print("Available Symptoms:")
    for i, symptom in enumerate(known_symptoms_list):
        print(f"  {i + 1}. {symptom.replace('_', ' ').title()}") # Make symptoms more readable

    print("-------------------------------------------------------")

    while True:
        try:
            user_input = input("Enter the numbers of your symptoms (e.g., 1, 3, 5): ")
            if not user_input:
                print("No symptoms entered. Exiting.")
                return

            selected_indices = [int(x.strip()) - 1 for x in user_input.split(',')]

            patient_symptoms = set()
            valid_input = True
            for index in selected_indices:
                if 0 <= index < len(known_symptoms_list):
                    patient_symptoms.add(known_symptoms_list[index])
                else:
                    print(f"Error: Invalid symptom number {index + 1}. Please try again.")
                    valid_input = False
                    break

            if not valid_input:
                continue # Ask for input again if invalid number found

            if not patient_symptoms:
                 print("You didn't select any valid symptoms from the list. Please try again.")
                 continue

            print("\n--- Processing Symptoms ---")
            print(f"You reported: {', '.join(s.replace('_', ' ').title() for s in sorted(list(patient_symptoms)))}")

            # Run the inference engine
            results = get_possible_diagnoses(patient_symptoms, knowledge_base)

            print("\n--- Possible Assessment ---")
            if results:
                for result in results:
                    print(f"- Diagnosis Suggestion: {result['diagnosis']}")
                    print(f"  Advice: {result['advice']}\n")
            else:
                print("Based on the symptoms provided, no specific condition suggestion could be made from the limited knowledge base.")
                print("Advice: Please consult a healthcare professional for any health concerns.")

            print("-------------------------------------------------------")
            # Ask if the user wants to run again
            run_again = input("Check another set of symptoms? (yes/no): ").strip().lower()
            if run_again != 'yes':
                break # Exit the loop

        except ValueError:
            print("Error: Invalid input. Please enter numbers separated by commas (e.g., 1, 5).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break # Exit on other errors

    print("\nExiting the system. Remember to consult a doctor for actual medical advice.")

# --- Main execution ---
if __name__ == "__main__":
    run_expert_system()