import streamlit as st
import pandas as pd

from ticker import Ticker
from sendinblue import add_emails_to_list
from mail import send_conf_mail

# https://builtin.com/machine-learning/streamlit-tutorial
# https://docs.streamlit.io/library/cheatsheet
# https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514/26

# Ticker Data 
spy = Ticker("^GSPC") #("%5EGSPC")  #("spy")
ndx = Ticket("^NDX") #("%5ENDX")

st.title("HFEA & 200MA Strategy WebApp")
st.write("""
Die Idee zu diesem Projekt stammt vom exzellenten Abenteuer des ZahlGrafs, der sich tief mit gehebelte ETFs und verschiedenen Strategien beschäftigt hat. 
Ganz speziell hat er sich die HFEA-Strategie vorgenommen und in seiner Analysen festgestellt, dass auch eine 200-SMA-Strategie bei LETFs sinnvoll sein kann.
Die Serie ist hier zu finden: https://www.reddit.com/r/mauerstrassenwetten/comments/s71qds/zahlgrafs_exzellente_abenteuer_teil_1/

Diese WebApp soll verschiedene Funktionen anbieten, um die Handhabungen der zwei verschiedenen Strategien zu vereinfachen.

Folgende Funktionen sind noch geplant: 
* Mehrere Ticker erlauben 
* Benachrichtigung via E-Mail (Stand: beta-version)
* Telegram Bot (Stand: alpha-version)
* HFEA-Rebalancing-Rechner inkl. Sparraten sowie Remind-Funktion (E-Mail & Telegram)

* optional: Benachrichtigung via mobile PushUp Notification
* optional: Einbindung von ZahlGrafs-Code zum selber ausprobieren durch Änderung von Parametern 


Die aktuelle API ist hier zu finden: https://ed8boq.deta.dev/v1/docs


**Betreut wird das Projekt aktuell durch Finanzflunder & Spassfabrik.
Großer Dank geht natürlich an ZahlGraf und die gesamte Mauerstrassenwetten-Community**
""")

#st.write(f"Ticker: S&P500")
#st.write(f"IS_CROSSED: {spy.CROSSED}")
#st.write(f"SMA200: {spy.SMA200}")
#st.write(f"PRICE: {spy.PRICE}")

st.text_input("Ticker")

with st.spinner('Getting market data...'):
    df = pd.DataFrame({"Ticker": ["S&P500", "Nasdaq100"], "PRICE": [spy.PRICE, ndx.PRICE], "SMA200": [spy.SMA200, ndx.SMA200], "CROSSED": [spy.CROSSED, ndx.CROSSED]})
st.success('Done!')

st.write(df)

st.write("  ")
st.markdown("### E-Mail Verteiler")
st.write("- IN BEARBEITUNG")
email = st.text_input("Deine E-Mail")
beta_pw = st.text_input("BETA Passwort")

if st.button("Gib's mir!"):
  if beta_pw == st.secrets["NEWSLETTER_PW"]:
    add_emails_to_list([email]) # TODO: E-Mail Format Validierung?!
    send_conf_mail(email)
    st.write("Du hast dich erfolgreich eingetragen! Bitte beachte, dass die E-Mail sehr wahrscheinlich im SPAM Ordner landen wird!")
  else: 
    st.write("Das BETA Password für den Newsletter ist falsch")

 
