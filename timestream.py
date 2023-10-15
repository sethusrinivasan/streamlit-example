import streamlit as st
import awswrangler as wr
import pandas as pd
from datetime import datetime

st.title('Timestream Demo - Work in progress')

df = pd.read_csv(
    "https://raw.githubusercontent.com/awslabs/amazon-timestream-tools/mainline/sample_apps/data/sample.csv",
    names=[
        "ignore0",
        "region",
        "ignore1",
        "az",
        "ignore2",
        "hostname",
        "measure_kind",
        "measure",
        "ignore3",
        "ignore4",
        "ignore5",
    ],
    usecols=["region", "az", "hostname", "measure_kind", "measure"],
)
df["time"] = datetime.now()
df.reset_index(inplace=True, drop=False)


st.dataframe(df)  

#wr.timestream.create_database("sampleDB")
#wr.timestream.create_table("sampleDB", "sampleTable", memory_retention_hours=1, magnetic_retention_days=1)


