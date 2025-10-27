
layer_name = 'gis_osm_pois_free_1'
field_name = 'fclass' 

matching_layers = QgsProject.instance().mapLayersByName(layer_name)

if matching_layers:
    layer = matching_layers[0]

    category_definitions = [
        ('hospital',    '#ff0000', '8', 'Hospital'),
        ('bank',        '#009933', '6', 'Bank'),
        ('restaurant',  '#0000ff', '6', 'Restaurant'),
        ('supermarket', '#ffa500', '6', 'Supermarket')
    ]
    
    categories = []
    for value, color, size, label in category_definitions:
        symbol = QgsMarkerSymbol.createSimple({
            'name': 'square', 'color': color, 'size': size
        })
        category = QgsRendererCategory(value, symbol, label)
        categories.append(category)

    renderer = QgsCategorizedSymbolRenderer(field_name, categories)
    layer.setRenderer(renderer)

    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())
    print(f"Symbology for '{layer_name}' updated successfully.")
else:
    print(f"ERROR: Layer '{layer_name}' not found. Please check the name for typos and make sure it is loaded in your project.")