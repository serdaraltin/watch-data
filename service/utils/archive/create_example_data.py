from datetime import datetime, timedelta
import random
import pandas as pd

def create_full_sample_data(start_date, end_date, num_samples=1000):
    
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    delta = end - start
    all_days = [start + timedelta(days=i) for i in range(delta.days + 1)]

    random_dates = [random.choice(all_days) + timedelta(seconds=random.randint(0, 86400)) for _ in range(num_samples)]
    random_datetimes = [random.choice(all_days) + timedelta(seconds=random.randint(0, 86400)) for _ in range(num_samples)]
    random_datetimes_iso = [dt.isoformat() for dt in random_datetimes]
    camera_ids = [random.choice([1]) for i in range(num_samples)]
    labels = [random.choice(["person counter"]) for i in range(num_samples)]
    confidences = [round(random.uniform(0.5, 1.0), 2) for _ in range(num_samples)]
    event_types = [random.choice(["enter", "exit"]) for i in range(num_samples)]
    genders = [random.choice([0, 1]) for i in range(num_samples)]
    gender_confidences = [round(random.uniform(0.5, 1.0), 2) for _ in range(num_samples)]
    age_ranges = [random.choice(["20-25", "30-40"]) for i in range(num_samples)]
    age_confidences = [round(random.uniform(0.5, 1.0), 2) for _ in range(num_samples)]

    sample_data = pd.DataFrame({
        'id': range(1, num_samples + 1),
        'camera_id': camera_ids,
        'detection_time': random_datetimes_iso,
        'label': labels,
        'confidence': confidences,
        'event_time': random_datetimes_iso, 
        'event_type': event_types,
        'gender': genders,
        'gender_confidence': gender_confidences,
        'age_range': age_ranges,
        'age_confidence': age_confidences
    })

    sample_data.to_excel("dde.xlsx")
    return sample_data

start_date = "2024-01-01"
end_date = "2024-12-31"
full_sample_data = create_full_sample_data(start_date, end_date)