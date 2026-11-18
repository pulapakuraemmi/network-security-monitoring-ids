import json
from pathlib import Path

import pandas as pd
import streamlit as st

LOG_FILE = Path("/var/log/suricata/eve.json")

st.set_page_config(
    page_title="NSM IDS Dashboard",
    page_icon="🛡️",
    layout="wide",
)

st.title("Network Security Monitoring Dashboard")
st.caption("Suricata intrusion alerts from the Ubuntu lab")

st.button("Refresh alerts")

if not LOG_FILE.exists():
    st.error(f"Suricata log not found: {LOG_FILE}")
    st.stop()

rows = []

try:
    with LOG_FILE.open("r", encoding="utf-8") as log:
        for line in log:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            if event.get("event_type") != "alert":
                continue

            alert = event.get("alert") or {}
            rows.append({
                "timestamp": event.get("timestamp", ""),
                "signature": alert.get("signature", "Unknown"),
                "severity": alert.get("severity"),
                "protocol": event.get("proto", ""),
                "source IP": event.get("src_ip", ""),
                "source port": event.get("src_port", ""),
                "destination IP": event.get("dest_ip", ""),
                "destination port": event.get("dest_port", ""),
            })
except PermissionError:
    st.error("Permission denied. Sign out of Ubuntu and sign back in, then try again.")
    st.stop()

if not rows:
    st.info("No alerts found yet. Generate test traffic, then click Refresh alerts.")
    st.stop()

df = pd.DataFrame(rows)
df["severity"] = pd.to_numeric(df["severity"], errors="coerce")

first, second, third = st.columns(3)
first.metric("Total alerts", len(df))
second.metric("Unique source IPs", df["source IP"].nunique())
third.metric("Severity 3 alerts", int((df["severity"] == 3).sum()))

st.subheader("Alerts by signature")
st.bar_chart(df["signature"].value_counts())

st.subheader("Alert details")
st.dataframe(
    df.sort_values("timestamp", ascending=False),
    use_container_width=True,
    hide_index=True,
)
