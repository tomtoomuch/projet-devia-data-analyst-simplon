import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Quantité vendue par région
qte_region = px.pie(données, values='qte', names='region', title='quantité vendue par région')
# Ventes par produit
qte_produit = px.pie(données, values='qte', names='produit', title='ventes par produit')
# CA par produit
données['ca'] = données['prix'] * données['qte']
ca_produit = px.pie(données, values='ca', names='produit', title='CA par produit')

qte_region.write_html('ventes-par-region.html')
qte_produit.write_html('ventes-par-produit.html')
ca_produit.write_html('ca-par-produit.html')

print('ventes-par-région.html, ventes-par-produit.html, ca-par-produit.html générés avec succès !')
