# Network Security Monitoring and Intrusion Detection Dashboard

An educational network security monitoring project using **Suricata** to detect network events and **Streamlit** to display Suricata's EVE JSON data in a dashboard.

## How it works

1. Suricata monitors a network interface and applies its detection rules.
2. Suricata writes events and alerts to an EVE JSON log.
3. The Streamlit dashboard reads that log and displays the available records.

The dashboard displays Suricata's output; Suricata and its rules perform the detection.

## Technologies

- Python
- Suricata
- Streamlit
- pandas
- EVE JSON

## Requirements

- Ubuntu or another Linux system
- Python 3
- Suricata configured to write EVE JSON
- Read access to the EVE JSON log

## Setup

Clone the repository and enter its folder:

```bash
git clone https://github.com/pulapakuraemmi/network-security-monitoring-ids.git
cd network-security-monitoring-ids
```

Create a Python environment and install the dashboard packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If creating the environment fails because `venv` is missing, install it with:

```bash
sudo apt install python3-venv
```

## Configure the Suricata log

The dashboard needs to read Suricata's EVE JSON log. A common Ubuntu location is:

```text
/var/log/suricata/eve.json
```

Check the log path configured on your system and the path used in `app.py`. Update `app.py` if they differ. The account running the dashboard also needs permission to read the log.

## Run the dashboard

With the Python environment activated, run:

```bash
streamlit run app.py
```

Open the local address shown in the Terminal, usually `http://localhost:8501`.

## Notes

- Suricata must be running and monitoring the correct network interface for live alerts.
- Network interface names can differ between computers and virtual machines.
- This project is for learning and demonstration. Only monitor networks you own or are authorized to monitor.
- Raw traffic logs may contain sensitive information; do not commit them to this repository.

## References

- [Suricata EVE JSON output](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html)
- [Streamlit documentation](https://docs.streamlit.io/)

