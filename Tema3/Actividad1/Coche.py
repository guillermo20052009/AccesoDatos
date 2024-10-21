from peewee import Model, CharField,DecimalField,IntegerField
from database import db

class Coche(Model):
    marca=CharField()
    modelo=CharField()
    año=IntegerField()
    precio=DecimalField()
    color=CharField()
    motor_id=IntegerField()
    
    class Meta:
        database=db
        table_name="coches"
        
        def tabla_existe(table_name):
            consulta="""SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND
            table_name = %s"""
            
            cursor = db.execute_sql(consulta,('Guillermo1DAM','coches'))
            resultado=cursor.fetchone()
            return resultado[0] > 0
