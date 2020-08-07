# Disease graph database queries

**Angel Nugroho: NCATS Data Science Intern**

Gets list of ontologies (:DATASOURCE) that make up the disease graph. Also returns the number of instances/nodes for each.
```
match (n:DATASOURCE) return n.name, n.instances;
```

Gets nodes that correspond to Tourette's syndrome based on name entries
_Note that the name property uses uppercase strings_
```
match (m:ENTITY) where any(x in m.N_Name where x =~ 'TOURETTE SYNDROME') RETURN m
```

Retrieves GARD disease nodes connected to S_ORDO disease nodes. Can replace S_ORDO and S_GARD with other ontologies.
```
match p = (m:S_GARD)-[r]-(n:S_ORDO) return p;
```

Retrieves GARD disease nodes (w/ data explanation nodes) connected to OMIM disease nodes based on identifier (I_CODE) matches
```
match (n:S_GARD)--(d:DATA) with n, d match p=(:DATA)--(n)-
[:I_CODE]-(m:S_OMIM)--(:DATA) return p;
```

Retrieves Gard disease nodes (w/ data explanation) connected to phenotype disease nodes based on any relationship
```
match (n:S_GARD)--(d:DATA)  with n, d match p =(n)-[]-(:S_HP)-
-(:DATA) return p,d;
```

Retrieves GARD disease nodes (w/ data explanation) connected to phenotype disease nodes based on R_rel with the property "has_phenotype" relationship.
Alternatively return node properties or count(node variable) to get information about nodes in a table.
```
match (n:S_GARD)--(d:DATA) with n, d match p =(n)-
[:R_rel{name: 'has_phenotype'}]-(:S_HP)--(:DATA) return p,d;
```
