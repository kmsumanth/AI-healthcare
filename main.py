from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from producer import KafkaProducer
app = FastAPI()
kafka_producer = KafkaProducer()
# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template rendering
templates = Jinja2Templates(directory="templates")

# Categorical variables
GENDER_CHOICES = ["Male", "Female"]
SMOKING_STATUS_CHOICES = ["Never", "Former", "Current"]
ALCOHOL_CONSUMPTION_CHOICES = ["Low", "Moderate", "High"]
PHYSICAL_ACTIVITY_LEVEL_CHOICES = ["Sedentary", "Moderate", "Active"]
DIET_QUALITY_CHOICES = ["Poor", "Average", "Good"]
STRESS_LEVEL_CHOICES = ["Low", "Medium", "High"]
SLEEP_QUALITY_CHOICES = ["Poor", "Fair", "Good"]
GENETIC_DISPOSITION_CHOICES = ["Low", "Moderate", "High"]
MENTAL_HEALTH_STATUS_CHOICES = ["Stable", "Mild Issues", "Severe Issues"]
OCCUPATION_TYPE_CHOICES = ["Sedentary", "Active", "Mixed"]
EXPOSURE_TO_ENVIRONMENTAL_FACTORS_CHOICES = ["Low", "Moderate", "High"]
FAMILY_HISTORY_CHOICES = ["No", "Yes"]

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/enter_data")
def enter_data(request: Request):
    return templates.TemplateResponse(
        "enter_data.html",
        {
            "request": request,
            "genders": GENDER_CHOICES,
            "smoking_statuses": SMOKING_STATUS_CHOICES,
            "alcohol_consumptions": ALCOHOL_CONSUMPTION_CHOICES,
            "physical_activity_levels": PHYSICAL_ACTIVITY_LEVEL_CHOICES,
            "diet_qualities": DIET_QUALITY_CHOICES,
            "stress_levels": STRESS_LEVEL_CHOICES,
            "sleep_qualities": SLEEP_QUALITY_CHOICES,
            "genetic_dispositions": GENETIC_DISPOSITION_CHOICES,
            "mental_health_statuses": MENTAL_HEALTH_STATUS_CHOICES,
            "occupation_types": OCCUPATION_TYPE_CHOICES,
            "exposure_levels": EXPOSURE_TO_ENVIRONMENTAL_FACTORS_CHOICES,
            "family_histories": FAMILY_HISTORY_CHOICES,
        },
    )

@app.post("/submit")
def submit_data(
    request: Request,
    patient_name:str = Form(...),
    Patient_Id:int = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    bmi: float = Form(...),
    blood_pressure: float = Form(...),
    cholesterol_level: float = Form(...),
    glucose_level: float = Form(...),
    insulin_level: float = Form(...),
    smoking_status: str = Form(...),
    alcohol_consumption: str = Form(...),
    physical_activity_level: str = Form(...),
    diet_quality: str = Form(...),
    stress_level: str = Form(...),
    sleep_quality: str = Form(...),
    genetic_disposition: str = Form(...),
    mental_health_status: str = Form(...),
    occupation_type: str = Form(...),
    exposure_to_environmental_factors: str = Form(...),
    family_history: str = Form(...),
    inflammatory_markers: float = Form(...),
    metabolic_rate: float = Form(...),
    vitamin_d_level: float = Form(...),
    hemoglobin_level: float = Form(...),
    kidney_function: float = Form(...),
    liver_function: float = Form(...),
    lung_function: float = Form(...),
    immune_response: float = Form(...),
    medication_usage: float = Form(...),
    hydration_level: float = Form(...),
    gut_microbiome_health: float = Form(...),
    environmental_pollution_exposure: float = Form(...),
    chronic_illnesses: float = Form(...),
    inflammation_index: float = Form(...),
    oxidative_stress_index: float = Form(...),
    # overall_health_risk: str = Form(...),
):
    data = {
        "Patient Name":patient_name,
        "Age": age,
        "Gender": gender,
        "BMI": bmi,
        "Blood Pressure": blood_pressure,
        "Cholesterol Level": cholesterol_level,
        "Glucose Level": glucose_level,
        "Insulin Level": insulin_level,
        "Smoking Status": smoking_status,
        "Alcohol Consumption": alcohol_consumption,
        "Physical Activity Level": physical_activity_level,
        "Diet Quality": diet_quality,
        "Stress Level": stress_level,
        "Sleep Quality": sleep_quality,
        "Genetic Disposition": genetic_disposition,
        "Mental Health Status": mental_health_status,
        "Occupation Type": occupation_type,
        "Exposure to Environmental Factors": exposure_to_environmental_factors,
        "Family History": family_history,
        "Inflammatory Markers": inflammatory_markers,
        "Metabolic Rate": metabolic_rate,
        "Vitamin D Level": vitamin_d_level,
        "Hemoglobin Level": hemoglobin_level,
        "Kidney Function": kidney_function,
        "Liver Function": liver_function,
        "Lung Function": lung_function,
        "Immune Response": immune_response,
        "Medication Usage": medication_usage,
        "Hydration Level": hydration_level,
        "Gut Microbiome Health": gut_microbiome_health,
        "Environmental Pollution Exposure": environmental_pollution_exposure,
        "Chronic Illnesses": chronic_illnesses,
        "Inflammation Index": inflammation_index,
        "Oxidative Stress Index": oxidative_stress_index,
        # "Overall Health Risk": overall_health_risk,
    }
    kafka_producer.produce(**data)
    return templates.TemplateResponse("result.html", {"request": request, "data": data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
