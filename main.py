import streamlit as st
import pandas as pd

from ticker import Ticker
from sendinblue import add_emails_to_list

# https://builtin.com/machine-learning/streamlit-tutorial
# https://docs.streamlit.io/library/cheatsheet
# https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514/26


spy = Ticker("spy")

st.title("HFEA & 200MA Strategy WebApp")
st.write("""
Die Idee zu diesem Projekt stammt vom exzellenten Abenteuer des ZahlGrafs, der sich tief mit gehebelte ETFs und verschiedenen Strategien beschäftigt hat. 
Ganz speziell hat er sich die HFEA-Strategie vorgenommen und in seiner Analysen festgestellt, dass auch eine 200-SMA-Strategie bei LETFs sinnvoll sein kann.
Die Serie ist hier zu finden: https://www.reddit.com/r/mauerstrassenwetten/comments/s71qds/zahlgrafs_exzellente_abenteuer_teil_1/

Diese WebApp soll verschiedene Funktionen anbieten, um die Handhabungen der zwei verschiedenen Strategien zu vereinfachen.

Folgende Funktionen sind noch geplant: 
* Mehrere Ticker erlauben 
* Benachrichtigung via E-Mail 
* Benachrichtigung via mobile PushUp Notification
* HFEA-Rebalancer-Rechner sowie Remind-Funktion
* optional: Telegram Bot
* optional: Einbindung von ZahlGrafs-Code zum selber ausprobieren durch Änderung von Parametern 

**Betreut wird das Projekt aktuell durch Finanzflunder & Spassfabrik.
Großer Dank geht natürlich an ZahlGraf und die gesamte Mauerstrassenwetten-Community**
""")

#st.write(f"Ticker: SPY")
#st.write(f"IS_CROSSED: {spy.CROSSED}")
#st.write(f"SMA200: {spy.SMA200}")
#st.write(f"PRICE: {spy.PRICE}")

st.text_input("Ticker")

with st.spinner('Getting market data...'):
    df = pd.DataFrame({"Ticker": ["SPY"], "PRICE": [spy.PRICE], "SMA200": [spy.SMA200], "CROSSED": [spy.CROSSED]})
st.success('Done!')

st.write(df)

st.write("  ")
st.markdown("### E-Mail Verteiler")
st.write("- IN BEARBEITUNG")
email = st.text_input("Deine E-Mail")
beta_pw = st.text_input("BETA Passwort")

if st.button("Gib's mir!"):
  if beta_pw == st.secrets["NEWSLETTER_PW"]:
    add_emails_to_list(list(email)) # TODO: E-Mail Format Validierung?!
    st.write("Du hast dich erfolgreich eingetragen")
  else: 
    st.write("Das BETA Password für den Newsletter ist falsch")

 
