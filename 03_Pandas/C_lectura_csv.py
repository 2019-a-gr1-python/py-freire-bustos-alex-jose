#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:53:23 2019

@author: usrdel
"""

import pandas as pd
import os

# Archivos texto -> JSON, CSV, HTML, XML....
# Binary Files -> (asdasdadasdasdasd)
# Relational Databases


path = '/Users/usrdel/Documents/GitHub/py-eguez-sarzosa-vicente-adrian/03_Pandas/data/csv/artwork_data.csv'

df = pd.read_csv(
        path,
        nrows=100,
        usecols=['id','artist'],
        index_col='id'
        )

columnas_a_usar = ['id','artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units']

df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id'
        )


path_guardado = '/Users/usrdel/Documents/GitHub/py-eguez-sarzosa-vicente-adrian/03_Pandas/data/csv/artwork_data.pickle'

df_completo.to_pickle(path_guardado)

df_completo_pickle = pd.read_pickle(path_guardado)

df_completo.shape






























