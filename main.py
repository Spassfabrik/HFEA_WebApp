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
ndx = Ticker("^NDX") #("%5ENDX")

st.title("HFEA & 200MA Strategy WebApp")
st.write("""
Die Idee zu diesem Projekt stammt vom exzellenten Abenteuer des ZahlGrafs, der sich tief mit gehebelte ETFs und verschiedenen Strategien beschäftigt hat. 
Ganz speziell hat er sich die HFEA-Strategie vorgenommen und in seiner Analysen festgestellt, dass auch eine 200-SMA-Strategie bei LETFs sinnvoll sein kann.
Die Serie ist hier zu finden: https://www.reddit.com/r/mauerstrassenwetten/comments/s71qds/zahlgrafs_exzellente_abenteuer_teil_1/
""")

st.image("https://i.redd.it/pjvrlinxcxw81.png")

st.write("""
Diese WebApp soll verschiedene Funktionen anbieten, um die Handhabungen der zwei verschiedenen Strategien zu vereinfachen.
""")

st.text_input("Ticker")
st.write("""
Info zum SMA: SPY bezieht sich auf SMA200 und Nasdaq100 auf SMA220.
""")

with st.spinner('Getting market data...'):
    df = pd.DataFrame({"Ticker": ["S&P500", "NASDAQ100"], "PRICE": [spy.PRICE, ndx.PRICE], "SMA": [spy.SMA200, ndx.SMA220], "CROSSED": [spy.sma200_CROSSED, ndx.sma220_CROSSED], "% Diff.": [(1-(spy.SMA200/spy.PRICE))*100, (1-(ndx.SMA220/ndx.PRICE))*100]})
st.success('Done!')

st.write(df)

st.write("  ")
st.title("E-Mail Verteiler")
st.write("E-Mails erfolgen nur, wenn der 200SMA durchbrochen wurde. Die Prüfung erfolgt um 18 sowie 21:45 Uhr, und nur von Mo-Fr.")
email = st.text_input("Deine E-Mail")
beta_pw = st.text_input("BETA Passwort")

if st.button("Gib's mir!"):
  if beta_pw == st.secrets["NEWSLETTER_PW"]:
    add_emails_to_list([email]) # TODO: E-Mail Format Validierung?!
    send_conf_mail(email)
    st.write("Du hast dich erfolgreich eingetragen! Bitte beachte, dass die E-Mail sehr wahrscheinlich im SPAM Ordner landen wird!")
  else: 
    st.write("Das BETA Passwort für den Newsletter ist falsch")
   
st.write("  ")
st.title("Telegram Bot")
st.write(""" 
Der Telegram Bot ist unter **"@LETFsAbenteuerBot"** zu finden. 
Der Bot befindet sich aktuell in einer BETA-Phase und wirkliche Funktionalitäten gibt es bisher nicht. 
Von Mo. bis Fr. um jeweils 21:45 Uhr erfolgt eine Benachrichtigung mit den wichtigsten Informationen zum S&P500.
""")

st.write("  ")
st.title("API")
st.write(""" 
Die aktuelle API ist hier zu finden: https://ed8boq.deta.dev/v1/docs
""")

st.write("  ")
st.title("ToDos / Features")
st.write(""" 
* Mehrere Ticker erlauben 
* HFEA-Rebalancing-Rechner inkl. Sparraten sowie RemindMe-Funktion (E-Mail & Telegram)

* optional: Benachrichtigung via mobile PushUp Notification
* optional: Einbindung von ZahlGrafs-Code zum selber ausprobieren durch Änderung von Parametern


**Betreut wird das Projekt aktuell durch Finanzflunder & Spassfabrik. Bei Fragen gerne an uns direkt wenden.
Großer Dank geht natürlich an ZahlGraf und die gesamte Mauerstrassenwetten-Community**
""")

 
