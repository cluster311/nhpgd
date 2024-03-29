# Nomenclador para hospitales públicos de gestión descentralizada de Argentina

Nomenclador de Prestaciones de Salud mediante el cual se establecieron los aranceles modulares para los Hospitales Públicos de Gestión Descentralizada.  

El monto pagado a los hospitales de gestión desentralizada se define por resolución del Ministerio/Secretaría de Salud.  
La calidad de los datos a los fines de sistematizar el uso de estos datos es muy pobre. Es por esto que se requiere que se carguen a mano. Esta librera reordena los datos y los disponibiliza de manera estructurada.  

Ejemplo de publciación de los datos: [Resolución 60/2015](https://www.sssalud.gob.ar/hospitales/archivos/RES_60_2015_MS.pdf).  

## Instalación

```
pip install nhpgd
```

## Uso

### Buscar en el nomeclador

#### Por código

Busca solo elementos con códigos iguales

```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
for s in n.search(codigo='5.04'):
    print(s['codigo'])
    print(' - DESCR: {}'.format(s['descripcion']))
    print(' - ARANCEL: {}'.format(s['arancel']))
    # print(' - OBSERVACIONES \n********\n{}\n********'.format(s['observaciones']))
```

```
5.04
 - DESCR: Tumores de base de craneo.Tumores tronco cerebralAneurismas cerebrales
 - ARANCEL: 31,451
5.04
 - DESCR: Lobectomia total o parcial por traumatismo o epilepsia.
 - ARANCEL: 31,451
```

#### Por texto

Busca en todos los campos, incluso codigo

```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
for s in n.search(txt='5.04'):
    print(s['codigo'])
    print(' - DESCR: {}'.format(s['descripcion']))
    print(' - ARANCEL: {}'.format(s['arancel']))
    # print(' - OBSERVACIONES \n********\n{}\n********'.format(s['observaciones']))
```

```
5.04
 - DESCR: Tumores de base de craneo.Tumores tronco cerebralAneurismas cerebrales
 - ARANCEL: 31,451
5.04
 - DESCR: Lobectomia total o parcial por traumatismo o epilepsia.
 - ARANCEL: 31,451
35.04
 - DESCR: Estudio funcional respiratorio completo: volumenes pulmonares, distensibilidad dinamica, difusion pulmonar, presion inspiratoria, respiratoria, de oclusion, transdiafragmatica, trabajo respiratorio.
 - ARANCEL: 2,629
35.05
 - DESCR: Estudio funcional respiratorio parcial: hasta tres pruebas del cod. 35.04
 - ARANCEL: 490
```

```python
for s in n.search(txt='HIV'):
    print(s['codigo'])
    print(' - DESCR: {}'.format(s['descripcion']))
    print(' - ARANCEL: {}'.format(s['arancel']))
    # print(' - OBSERVACIONES \n********\n{}\n********'.format(s['observaciones']))
```

```
38.20
 - DESCR: HIV-SIDA. Comprende 2 marcadores celulares. Citometria de flujo.
 - ARANCEL: 729
40.10
 - DESCR: CARGA VIRAL PARA HIV. (Laboratorio N° 120)
 - ARANCEL: 6,677
40.04
 - DESCR: HIV ANTIC (ELISA) (Laboratorio N° 397)
 - ARANCEL: 438
40.05
 - DESCR: HIV ANTIC (IFI) (Laboratorio N° 398)
 - ARANCEL: 608
40.08
 - DESCR: HIV ANTIC (WESTER-BLOT) (Laboratorio N° 399)
 - ARANCEL: 3,885
40.04
 - DESCR: HIV ANTIC AGLUTINACION DE PART. DE GELATINA (Laboratorio N° 400)
 - ARANCEL: 438
40.10
 - DESCR: HIV PCR (Laboratorio N° 401)
 - ARANCEL: 6,677
40.06
 - DESCR: HIV ANTIGENO P24 (CUANTIFICACION) (Laboratorio N° 402)
 - ARANCEL: 1,942
40.09
 - DESCR: HIV CULTIVO (Laboratorio N° 403)
 - ARANCEL: 5,583
40.10
 - DESCR: HIV CULTIVO DE LCR Y OTROS MATERIALES (Laboratorio N° 404)
 - ARANCEL: 6,677
40.08
 - DESCR: HIV ENVA/CORE (Laboratorio N° 405)
 - ARANCEL: 3,885
```

### Iterar por toda la lista

Pasar por todos los elementos del nomenclador
```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
for i, nom in n.tree.items():
    print(nom)
```
### Verificar si existe código

```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
print(n.code_exists('5.04'))
True
print(n.code_exists('5.05'))
False
```

## Actualizar la base de datos

Como los datos de origen son de mala calidad y se actualizan anualmente está disponible la actualizacion de los datos.
Estos se almacenan en [una planilla de Google Drive](https://docs.google.com/spreadsheets/d/15r_GRQPtYWRFcAbLNHO2yktCXj5V2-xmkkTC7eGh8TM/edit#gid=0) para su rápida corrección.  

```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
# actualizar desde la planilla con los datos en google drive
n.download_csv()
# las próximas instancias del Nomenclador estarán actualizadas
```

## Exportar la base de datos
```python
from nhpgd.nomenclador import Nomenclador
n = Nomenclador()
# exportar a CSV
n.save_csv(path='lala.csv')
```