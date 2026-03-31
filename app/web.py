import json
from typing import Any

import streamlit as st

from app.extractor import extract_features


TABLE_DDL = """CREATE TABLE IF NOT EXISTS review_features (
    review_id SERIAL PRIMARY KEY,
    review_text TEXT NOT NULL,
    mentions_kitchen BOOLEAN,
    wants_storage BOOLEAN,
    mentions_light BOOLEAN,
    sentiment TEXT,
    summary TEXT
);"""


def sql_quote(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    text = str(value).replace("'", "''")
    return f"'{text}'"


def build_insert_sql(review_text: str, features: dict[str, Any]) -> str:
    return (
        "INSERT INTO review_features "
        "(review_text, mentions_kitchen, wants_storage, mentions_light, sentiment, summary)\n"
        "VALUES (\n"
        f"  {sql_quote(review_text)},\n"
        f"  {sql_quote(features.get('mentions_kitchen'))},\n"
        f"  {sql_quote(features.get('wants_storage'))},\n"
        f"  {sql_quote(features.get('mentions_light'))},\n"
        f"  {sql_quote(features.get('sentiment'))},\n"
        f"  {sql_quote(features.get('summary'))}\n"
        ");"
    )


def main() -> None:
    st.set_page_config(page_title="Flexor Mini Review → SQL", page_icon="🧠")
    st.title("🧠 Flexor Mini: Review Text to SQL Row")
    st.write("Paste a review or upload a `.txt` file, then generate SQL-ready output.")

    uploaded_file = st.file_uploader("Upload review text file", type=["txt"])
    review_text = st.text_area("Or paste review text", height=180)

    if uploaded_file is not None:
        file_text = uploaded_file.read().decode("utf-8", errors="ignore").strip()
        if file_text:
            review_text = file_text
            st.info("Loaded text from uploaded file.")

    if st.button("Generate SQL table row", type="primary"):
        cleaned_text = review_text.strip()
        if not cleaned_text:
            st.error("Please upload or paste review text first.")
            return

        with st.spinner("Extracting structured features..."):
            features = extract_features(cleaned_text)

        st.subheader("Extracted JSON")
        st.code(json.dumps(features, indent=2), language="json")

        st.subheader("Review SQL table schema")
        st.code(TABLE_DDL, language="sql")

        st.subheader("SQL INSERT statement")
        insert_sql = build_insert_sql(cleaned_text, features)
        st.code(insert_sql, language="sql")

        st.subheader("Preview row")
        st.table(
            {
                "review_text": [cleaned_text],
                "mentions_kitchen": [features.get("mentions_kitchen")],
                "wants_storage": [features.get("wants_storage")],
                "mentions_light": [features.get("mentions_light")],
                "sentiment": [features.get("sentiment")],
                "summary": [features.get("summary")],
            }
        )


if __name__ == "__main__":
    main()
