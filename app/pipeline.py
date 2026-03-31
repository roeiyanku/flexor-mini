from app.repository import (
    create_tables,
    reset_tables,
    insert_interview,
    get_all_interviews,
    insert_features,
    get_all_features
)
from app.extractor import extract_features


def run_pipeline():
    create_tables()
    reset_tables()

    insert_interview("participant_3", "The bedroom is too small and lacks closet space.")
    insert_interview("participant_4", "I really like the open layout between the kitchen and living room.")
    insert_interview("participant_5", "The bathroom needs better ventilation.")
    insert_interview("participant_6", "There’s a lot of noise from the street outside.")
    insert_interview("participant_7", "I enjoy the balcony, it’s very relaxing.")
    insert_interview("participant_8", "The lighting in the hallway is too dim.")
    insert_interview("participant_9", "I wish the kitchen had more counter space.")
    insert_interview("participant_10", "The apartment feels very spacious and comfortable.")
    insert_interview("participant_11", "Storage space in general is limited.")

    interviews = get_all_interviews()

    for interview_id, speaker, transcript in interviews:
        features = extract_features(transcript)
        insert_features(interview_id, features)

    print("INTERVIEWS:")
    for row in interviews:
        print(row)

    print("\nFEATURES:")

    columns = [
        "interview_id",
        "mentions_kitchen",
        "wants_storage",
        "mentions_light",
        "sentiment",
        "summary"
    ]

    print(" | ".join(columns))

    for row in get_all_features():
        print(" | ".join(str(x) for x in row))