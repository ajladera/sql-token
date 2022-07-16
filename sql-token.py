# Databricks notebook source
import hashlib
from datetime import date
import pandas as pd


fecha = date.today().strftime('%Y-%m-%d')
md5_hash = hashlib.md5()
variable = md5_hash.update(fecha.encode('utf8'))
variable = md5_hash.hexdigest()
data = {f'Futurum':variable}
data = pd.DataFrame.from_dict(data, orient='index')
data.reset_index(inplace=True)
data.rename(columns = {'index':'usuario', 0:'contraseña'}, inplace = True)
