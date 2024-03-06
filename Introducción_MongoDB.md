# MongoDB
## Conexión a MongoDB
### Cadena de conexión
~~~
atlas clusters connectionStrings describe NombreDelCluster
~~~
### Formato de la cadena de conexión
~~~
mongodb+srv://usuario:password@host/opciones
~~~
### Conexión
mongosh -u usuario -p bbdd CadenaDeConexión

## Inserción de datos
### insertOne() (si no existe la colección, la crea)
~~~
db.colección.insertone(documento)
~~~
### insertMany()
~~~
db.colección.insertMany([
documento1,
documento2,
documentoN
])
~~~
## Consultas sencillas
~~~
db.colección.find(consulta)
~~~
### Operadores
~~~
db.colección.find({ "campo": {operador: valor} })
~~~
#### $eq (=)
~~~
db.colección.find({ "campo": valor })
db.colección.find({ "campo": {$eq: valor} })
~~~
#### $neq (!=)
~~~
db.colección.find({ "campo": {$neq: valor} })
~~~
#### $in (in)
~~~
db.colección.find({ "campo": { $in: [valor1, valor2] } })
~~~
#### $nin (not in)
~~~
db.colección.find({ "campo": { $nin: [valor1, valor2] } })
~~~
#### $gt (<, mayor que)
~~~
db.colección.find({ "campo": {$gt: valor} })
~~~
#### $lt (>, menor que)
~~~
db.colección.find({ "campo": {$le: valor} })
~~~
#### $gte (<=, mayor o igual que)
~~~
db.colección.find({ "campo": {$gte: valor} })
~~~
#### $lte (>=, mayor o igual que)
~~~
db.colección.find({ "campo": {$lte: valor} })
~~~
		
## Consultas complejas (subconsultas): $elemMatch()
~~~
db.colección.find({
	campo: {
		$elemMatch: { campo1: { operador: valor1}, campo2: {operador: valor2}, campoN: {operador:valorN}},
	},
})
~~~

## Consultas con operadores lógicos (and, not, nor, or):
### $and (and)
~~~
db.colección.find({ "campo1": { operador: valor1}, "campo2": { operador: valor2 }, "campoN": { operador: valorN} }) (versión implícita)

db.colección.find({
  $and: [{ "campo1": { operador: valor1}, "campo2": { operador: valor2 }, "campoN": { operador: valorN} }],		
}) 
~~~
(versión explícita: necesaria cuando se usan otros operadores dentro del and.)
### $or (or)
~~~
db.colección.find({
  $or: [{ "campo1": { operador: valor1}, "campo2": { operador: valor2 }, "campoN": { operador: valorN}}],
})
~~~
## Consultas de actualización
### updateOne()
~~~
db.colección.replaceOne({filtro}, {DocumentoNuevo}, {opciones})
~~~
#### Operadores
- $set: actualiza o crea un campo
- $push: añade datos a un campo de tipo matriz existente
- $inc: incrementa un dato numérico
~~~
db.colección.replaceOne({filtro}, {operador: {campo: {$each: {[valor1, valor2, valorN]}}, {opciones})
~~~
Opción upsert: si no existe el documento que se actualiza, lo crea.
~~~
db.colección.replaceOne({filtro}, {DocumentoNuevo}, {upsert: true})
~~~
### findAndModify()
~~~
db.colección.findAndModify({
	query: {campo_filtro: valor_filtro},
	update: {operador: {campo: valor}},
	opciones,
})
~~~
Opciones: 
- new: true (muestra el documento modificado) 
- upsert: true (crea el documento si no existe)
### updateMany()
~~~
db.colección.updateMany(
	{campo_filtro: valor_filtro},
	{operador: {campo: valor}}
)
~~~
## Consultas de eliminación
### deleteOne()
~~~
db.colección.deleteOne({campo_filtro: valor filtro}, opciones)
~~~
### deleteMany()
~~~
db.colección.deleteMany({campo_filtro: valor filtro}, opciones)
~~~
## Operaciones sobre consultas
### Ordenar resultados: .sort()
~~~
db.colección.find({ "campo": valor }).sort({campo: 1 | -1})
~~~
- 1 ordena ascendentemente
- -1 ordena descendentemente
### Limitar el número de resultados: .limit()
~~~
db.colección.find({ "campo": valor }).limit(n)
~~~
n = número de entradas que se quiere mostrar
### Proyecciones (limitar el número de campos que devuelve)
~~~
db.colección.find({campo: valor},{campo: 1 | 0})
~~~
- 1 incluye el campo en el resultado
- 0 excluye el campo del resultado
### Contar resultados
~~~
db.colección.countDocuments({campo: valor}, {opciones})
~~~
## Agregación
### $match (filtra resultados)
~~~
db.colección.aggregate({$match: {campo: valor}})
~~~
### $group (= group by; agrupa resultados)
~~~
db.colección.aggregate({$group: {_id: $campo, campo: {$agregador:{}}}}})
~~~
### $out (crea una nueva colección a partir de una agregación)
- Para crear una colección en una base de datos diferente a la que se está usando:
~~~
db.colección.aggregate({$out: {db: "BaseDeDatos", coll:"Colección"}})
~~~
- Para crear una colección en la misma base de datos que se está usando:
~~~
db.colección.aggregate({$out: "colección"}
~~~
## Índices
### Índices de un sólo campo: createIndex()
~~~
db.colección.createIndex({campo:1 | -1}, {restricción:true})
~~~
- 1: ascendente
- -1: descendente

### Índices compuestos: createIndex()
~~~
db.colección.createIndex({campo1: 1 | -1, campo2: 1 | -1, campoN: 1 | -1})
~~~
- 1: ascendente
- -1: descendente

Los campos del índice deben mantener el siguiente orden:
1. Campos que se van a usar para filtrar por igualdad
2. Campos que se van a usar para ordenar
3. Campos que se van a usar para filtrar por rango (mayor que, menor que)
### Ver los índices en una colección
~~~
db.colección.getIndexes()
~~~
### Comprobar si se están usando índices en una consulta: explain()
~~~
db.colección.explain().find({campo: valor})
~~~
- IXSCAN: Está usando un índice y muestra el nombre.
- COLLSCAN: No está usando ningún índice.
- FETCH: Indica la lectura de documentos de la colección.
- SORT: Indica que hay documentos ordenados en memoria.
### Ocultar índices
~~~
db.colección.hideIndex("nombre" | {campo: 1 | -1})
~~~
### Eliminar índices
~~~
db.colección.dropindex("nombre" | {campo: 1 | -1})
~~~
Si se usa `db.colección.dropIndex()`: borra todos los índices.
