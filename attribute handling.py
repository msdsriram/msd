
layer_name = 'gis_osm_roads_free_1'
field = 'fclass'
value = 'primary' # Examples: 'motorway', 'secondary', 'tertiary'

layer = QgsProject.instance().mapLayersByName(layer_name)[0]

if layer:
    # The expression format is "field_name" = 'value'
    expression = f"\"{field}\" = '{value}'"
    
    layer.selectByExpression(expression, QgsVectorLayer.SetSelection)
    
    print(f"Selected {layer.selectedFeatureCount()} features in '{layer_name}' where {field} is '{value}'.")
else:
    print(f"ERROR: Layer '{layer_name}' not found. Check for typos.")