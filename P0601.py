# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:00:05 2017

@author: carlos.arana
"""

'''
Descripcion:
Creacion de dataset P0601 "Denuncias recibidas en materia ambiental"
'''

# Librerias Utilizadas
import pandas as pd

# Directorios locales
DirFuente = r'D:\PCCS\01_Analysis\01_DataAnalysis\00_Parametros\scripts\BS01'
DirDestino = r'D:\PCCS\01_Analysis\01_DataAnalysis\06_BienesAmbientalesYServiciosPublicos\Scripts'

# Dataset Inicial
dataset = pd.read_excel(DirFuente + r'\BS01.xlsx', sheetname="DATOS", dtype={'CVE_MUN':str})
dataset.set_index('CVE_MUN', inplace = True)

# Columnas de Denuncias
Denuncias = [x for x in list(dataset) if 'Denuncias recibidas en materia amb' in x]

# Metadatos
descripcion = {
    'Nombre del Dataset'   : 'Denuncias Recibidas en Materia Ambiental',
    'Descripcion del dataset' : 'Numero de denuncias recibidas en materia ambiental, por municipio, de 1993 a 2014',
    'Fuente'    : 'SIMBAD - Sistema Estatal y municipal de Base de Datos (INEGI)',
    'URL_Fuente': 'http://sc.inegi.org.mx/cobdem/',
    'Obtencion de dataset' : 'Mineria de datos disponible en https://github.com/INECC-PCCS/BS01' ,
    'Desagregacion' : 'Municipal',
    'Disponibilidad temporal' : '1994 a 2013',
    'Repositorio de mineria' : '',
    'Notas' : 'Para las columnas con nombres repetidos, la primer aparicion corresponde a 1994'
}

# Dataset limpio
anios = list(range(1993, 2014))
registros = []

# renombrar columnas al año que corresponden
for i in anios:
    registros.append('DENUNNCIAS_AMB_{}'.format(i))

denuncias_ma = dataset[Denuncias]
denuncias_ma.columns = registros

# Total de denuncias por municipios.
denuncias_ma['DENUNCIAS_AMB'] = denuncias_ma.sum(axis=1)

# Exportar a Excel
writer = pandas.ExcelWriter(DirDestino + r'\P0601.xlsx')
dataset_b.to_excel(writer, sheet_name = 'DATOS')
metadatos.to_excel(writer, sheet_name = 'Metadatos')
writer.close()