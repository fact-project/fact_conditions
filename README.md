All kinds of conditions to query the fact database.

# Excutables
* `fact_create_new_condition_set`
Creates a new condition set from a given number of conditions and condition sets.

# Condition Sets
The package comes with a vareity of conditions, which are all in `fact_conditions/conditions`.
They can be accessed by their filename like this: `@standard` or @standard.yaml. If you use the second option and a given filename with the same name exists in your filesystem, the one in the filesystem takes precedent.
